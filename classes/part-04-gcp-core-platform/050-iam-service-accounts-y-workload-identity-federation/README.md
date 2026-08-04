# 050 — IAM, service accounts y Workload Identity Federation

> [← 049 · Organización, folders, proyectos, billing y cuotas](../../part-04-gcp-core-platform/049-organizacion-folders-proyectos-billing-y-cuotas/README.md) · [Índice de la parte](../README.md) · [051 · VPC global, subredes regionales, firewall y Cloud NAT →](../../part-04-gcp-core-platform/051-vpc-global-subredes-regionales-firewall-y-cloud-nat/README.md)

**Parte:** 04 — Google Cloud: plataforma esencial<br>
**Nivel:** intermedio · **Horas estimadas:** 4<br>
**Laboratorio:** `iam` · **Estado:** `EXECUTABLE_CORE`

## 🎯 Propósito

Dominar el modelo de identidad de Google Cloud, cuya pieza central no tiene equivalente exacto en las otras dos plataformas: la cuenta de servicio es **a la vez una identidad y un recurso**, así que hay dos preguntas de permiso en vez de una —qué puede hacer y quién puede usarla—. De ahí sale el camino de escalada más habitual de la plataforma, la fuga de credenciales más repetida y la razón por la que aquí el privilegio mínimo se revisa con datos de uso en vez de con criterio.

## 📚 Resultados de aprendizaje

Al finalizar podrás:

1. **Distinguir** los permisos de una cuenta de servicio de los permisos para suplantarla, y detectar la escalada que produce la segunda.
2. **Sustituir** claves de cuenta de servicio por identidad adjunta, suplantación y federación de identidad de carga de trabajo.
3. **Acotar** una federación con una condición de atributo y demostrar con una prueba negativa que la acotación funciona.
4. **Aplicar** políticas de denegación de IAM y condiciones con caducidad, y saber en qué orden se evalúa todo.
5. **Reducir** privilegios a partir del uso observado en vez de por estimación.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `cuenta de servicio` | Identidad **y recurso** a la vez. Tiene permisos propios sobre otros recursos y una política propia que dice quién puede usarla. Confundir las dos caras es la causa de la escalada más común de la plataforma. |
| `suplantación` | Obtener un testigo de corta duración de una cuenta de servicio. Sustituye a las claves para personas y para automatización, y deja rastro de **quién** suplantó a quién. |
| `clave de cuenta de servicio` | Fichero JSON con credenciales de larga duración. Es la fuga más frecuente de Google Cloud: acaba en repositorios, portátiles e imágenes de contenedor. |
| `rol básico` | `Owner`, `Editor` y `Viewer`. `Editor` permite modificar casi todo en el proyecto, y es lo que las cuentas de servicio por defecto reciben automáticamente. |
| `condición de atributo` | Filtro sobre las afirmaciones del testigo externo en una federación. Sin ella, **cualquier repositorio del proveedor externo puede obtener credenciales**. |
| `política de denegación de IAM` | Regla que quita permisos y se evalúa **antes** que las concesiones. Es lo que resta en un modelo aditivo, y convive con las políticas de organización sin sustituirlas. |

## 🧠 Modelo mental

Un proyecto de Google Cloud es la unidad práctica de API, cuota, IAM y facturación; la organización aporta la política heredable.

Aplicado a esta clase, separa siempre cuatro planos: **intención** (qué necesita el usuario),
**configuración** (qué declaramos), **estado observado** (qué existe de verdad) y
**evidencia** (cómo sabemos que cumple). Confundirlos produce diseños que se ven correctos
en un diagrama pero fallan al operar.

## 🗺️ Flujo de razonamiento

```mermaid
flowchart TB
    P["persona o carga de trabajo"] --> Q{"¿cómo obtiene credenciales?"}
    Q -->|"peor: fichero de larga duración"| K["clave de cuenta de servicio"]
    Q -->|"cargas dentro de Google Cloud"| A["cuenta de servicio ADJUNTA"]
    Q -->|"personas y automatización interna"| I["suplantación · testigo corto"]
    Q -->|"CI externo"| W["federación de identidad<br/>de carga de trabajo"]
    W --> C{"¿hay condición de atributo?"}
    C -->|"no"| X["CUALQUIER repositorio<br/>obtiene credenciales"]
    C -->|"sí"| OK["solo el sujeto declarado"]
    A --> SA["cuenta de servicio"]
    I --> SA
    OK --> SA
    SA --> D1["qué PUEDE HACER<br/>sus roles sobre recursos"]
    SA --> D2["quién puede USARLA<br/>su propia política de IAM"]
    D2 -.->|"serviceAccountTokenCreator<br/>= todos sus permisos"| ESC["escalada"]
```

## 📖 Desarrollo

### 1. La cuenta de servicio tiene dos caras y solo se mira una

En AWS un rol se asume; en Azure una identidad administrada se asocia a un recurso. En Google Cloud la cuenta de servicio es las dos cosas a la vez, y de ahí sale casi todo lo interesante de esta clase:

```text
cara 1 · es una IDENTIDAD
  tiene una dirección: despliegue@cls-tienda-prod.iam.gserviceaccount.com
  tiene roles sobre otros recursos: qué PUEDE HACER

cara 2 · es un RECURSO
  tiene su propia política de IAM: quién puede USARLA
```

La revisión de permisos habitual mira la primera cara —qué roles tiene cada persona— y se salta la segunda. Y la segunda es la que concede de verdad:

```bash
$ gcloud projects get-iam-policy cls-tienda-prod-euw1-01 \
    --flatten="bindings[].members" --filter="bindings.members:ana@cloudshop.example" \
    --format="value(bindings.role)"
roles/viewer
```

Parece que Ana solo puede leer. Pero:

```bash
$ gcloud iam service-accounts get-iam-policy \
    despliegue@cls-tienda-prod-euw1-01.iam.gserviceaccount.com \
    --format="value(bindings.role,bindings.members)"
roles/iam.serviceAccountTokenCreator   user:ana@cloudshop.example
```

```bash
$ gcloud storage ls --impersonate-service-account \
    despliegue@cls-tienda-prod-euw1-01.iam.gserviceaccount.com
# lista todo lo que puede la cuenta de despliegue, que tiene roles/editor
```

**Ana tiene, en la práctica, los permisos de la cuenta de despliegue.** Su rol propio es irrelevante. Los dos permisos que producen esto:

```text
roles/iam.serviceAccountTokenCreator   genera testigos: acceso completo a la cuenta
roles/iam.serviceAccountUser           permite ADJUNTARLA a un recurso nuevo
                                       → crear una máquina con esa cuenta y
                                         ejecutar código con sus permisos
```

El segundo es más sutil y no menos potente: quien puede crear una máquina virtual y adjuntarle una cuenta de servicio privilegiada puede ejecutar lo que quiera con esos permisos. Por eso `serviceAccountUser` sobre una cuenta con `Editor` **equivale a `Editor`**.

La regla operativa que se deduce, y que cambia cómo se audita:

```text
el permiso efectivo de una persona es la UNIÓN de:
  sus propios roles
  + los roles de TODA cuenta de servicio que pueda suplantar o adjuntar
  + (recursivamente) las que esas cuentas puedan suplantar a su vez
```

La palabra «recursivamente» no es teórica: una cadena de dos saltos —Ana suplanta a la cuenta A, que puede suplantar a la cuenta B, que es `Owner`— es un camino real y ninguna revisión que mire una sola tabla lo encuentra. La herramienta que lo resuelve es el analizador de políticas, que responde a la pregunta inversa: quién puede llegar a este recurso, por cualquier camino.

```bash
$ gcloud asset analyze-iam-policy --organization=$ORG_ID \
    --analyze-service-account-impersonation \
    --identity="user:ana@cloudshop.example"
```

### 2. Las cuentas por defecto ya vienen con Editor

Este es el hecho más importante de la clase para una organización recién abierta, porque el riesgo está puesto de fábrica.

Al habilitar Compute Engine o App Engine, el proyecto recibe **cuentas de servicio por defecto** y —salvo que se impida— se les concede automáticamente `roles/editor` sobre el proyecto:

```bash
$ gcloud projects get-iam-policy cls-tienda-prod-euw1-01 \
    --flatten="bindings[].members" --filter="bindings.role:roles/editor" \
    --format="value(bindings.members)"
serviceAccount:418293047512-compute@developer.gserviceaccount.com
```

Y esa cuenta es la que se adjunta por omisión a cualquier máquina virtual creada sin especificar otra. Es decir:

```text
cualquier máquina creada sin pensar
  → ejecuta con una identidad que puede modificar casi todo el proyecto
  → una dependencia comprometida en esa máquina hereda ese poder
  → y el servicio de metadatos entrega el testigo sin pedir nada
```

La comprobación desde dentro de la máquina, que conviene hacer una vez para entender la magnitud:

```bash
$ curl -s -H "Metadata-Flavor: Google" \
    "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email"
418293047512-compute@developer.gserviceaccount.com
```

Las dos medidas, en este orden:

```bash
# 1. que las cuentas por defecto dejen de recibir Editor automáticamente
$ gcloud resource-manager org-policies enable-enforce \
    constraints/iam.automaticIamGrantsForDefaultServiceAccounts --organization $ORG_ID

# 2. una cuenta dedicada por carga de trabajo, con los roles mínimos
$ gcloud iam service-accounts create sa-tienda-web --project cls-tienda-prod-euw1-01
$ gcloud projects add-iam-policy-binding cls-tienda-prod-euw1-01 \
    --member "serviceAccount:sa-tienda-web@cls-tienda-prod-euw1-01.iam.gserviceaccount.com" \
    --role roles/secretmanager.secretAccessor --condition=None
```

Y hay una complicación heredada que confunde a quien depura permisos en máquinas antiguas: los **ámbitos de acceso**. Son un mecanismo previo a IAM que sigue existiendo en Compute Engine, y el permiso efectivo de una máquina es la **intersección** de ambos:

```text
permiso efectivo = roles de la cuenta de servicio  ∩  ámbitos de la máquina
```

Eso produce el desconcierto clásico: la cuenta tiene el rol, la llamada falla, y añadir más roles no cambia nada porque el ámbito no lo incluye. La guía vigente es fijar el ámbito en `cloud-platform` y controlar exclusivamente con IAM, que es donde hay granularidad y auditoría:

```bash
$ gcloud compute instances create web-01 --zone europe-west1-b \
    --service-account sa-tienda-web@cls-tienda-prod-euw1-01.iam.gserviceaccount.com \
    --scopes cloud-platform
```

Y los **roles básicos** merecen una frase propia. `Editor` incluye modificar prácticamente cualquier recurso del proyecto; `Owner` añade gestionar los permisos, que es lo que convierte cualquier acceso en permanente. Ninguno de los tres debería aparecer en una concesión nueva. Su equivalente correcto son los roles predefinidos —hay cientos, muy específicos— y, cuando ninguno encaja, un rol personalizado:

```bash
$ gcloud iam roles create tiendaOperador --organization $ORG_ID \
    --permissions run.services.get,run.services.update,logging.logEntries.list \
    --stage GA
```

### 3. Las claves: por qué desaparecen y por qué no

Una clave de cuenta de servicio es un fichero JSON con una credencial que **no caduca**. Es la fuga de credenciales más frecuente de Google Cloud, y no por descuido excepcional: es que resulta cómoda.

```json
{"type": "service_account", "project_id": "cls-tienda-prod-euw1-01",
 "private_key_id": "…", "private_key": "-----BEGIN PRIVATE KEY-----\n…",
 "client_email": "despliegue@cls-tienda-prod-euw1-01.iam.gserviceaccount.com"}
```

Cuatro sitios donde acaban, en orden de frecuencia: un repositorio, la máquina de alguien, una imagen de contenedor y un gestor de secretos de otro sistema desde el que se copia a mano.

Las cuatro alternativas, por caso de uso, ordenadas de mejor a peor:

```text
carga dentro de Google Cloud     cuenta de servicio ADJUNTA al recurso
                                 no hay credencial: el servicio de metadatos
                                 entrega un testigo corto
persona                          suplantación con el propio inicio de sesión
                                 gcloud --impersonate-service-account
CI externo o nube ajena          federación de identidad de carga de trabajo
caso sin alternativa             clave, con caducidad y rotación automatizada
                                 y con la justificación escrita
```

La suplantación para personas cambia además lo que dice la auditoría, que es la mitad del valor:

```text
con clave         el registro dice: actuó despliegue@…
                  quién la usó: se desconoce
con suplantación  el registro dice: ana@cloudshop.example actuó
                  COMO despliegue@…
```

La primera forma hace imposible responder «quién hizo esto» durante un incidente. La segunda lo responde sola.

```bash
$ gcloud config set auth/impersonate_service_account \
    despliegue@cls-tienda-prod-euw1-01.iam.gserviceaccount.com
$ gcloud storage ls gs://cls-tienda-facturas
```

Y el interruptor que hace que todo lo anterior se cumpla de verdad, en lugar de quedarse en una recomendación:

```bash
$ gcloud resource-manager org-policies enable-enforce \
    constraints/iam.disableServiceAccountKeyCreation --organization $ORG_ID
```

Con él activo, la vía cómoda deja de existir y los equipos adoptan las otras tres. Sin él, siempre habrá un caso urgente que justifique una clave más. Es el mismo argumento de la clase 046 sobre por qué una directiva vale más que una norma: **el control que no se puede saltar no depende de la disciplina de nadie**.

Y para las claves que ya están en circulación, el inventario primero y la prueba negativa después:

```bash
$ gcloud asset search-all-resources --scope organizations/$ORG_ID \
    --asset-types iam.googleapis.com/ServiceAccountKey \
    --query "NOT name:*/keys/system-managed*" --format="value(name)" | wc -l
14
```

Las gestionadas por el sistema se excluyen del recuento porque son internas y rotan solas. Las catorce restantes son las creadas por personas, y cada una necesita un destino: sustituirla, o quedar documentada con responsable y fecha.

### 4. Federación: la tercera vez que aparece la misma condición

La federación de identidad de carga de trabajo permite que un sistema externo —una canalización de GitHub, una carga en otra nube, un servidor propio— obtenga credenciales sin ninguna clave. Es el mismo contrato de las clases 026 y 038, así que aquí interesa **lo que cambia y lo que no**.

Lo que no cambia: la pieza crítica sigue siendo acotar quién puede usarla.

```bash
$ gcloud iam workload-identity-pools create cls-ci --location global \
    --display-name "CI de CloudShop"

$ gcloud iam workload-identity-pools providers create-oidc github \
    --workload-identity-pool cls-ci --location global \
    --issuer-uri "https://token.actions.githubusercontent.com" \
    --attribute-mapping "google.subject=assertion.sub,\
attribute.repository=assertion.repository,\
attribute.ref=assertion.ref" \
    --attribute-condition "assertion.repository == 'cloudshop/tienda' && \
assertion.ref == 'refs/heads/main'"
```

**Sin `--attribute-condition`, cualquier repositorio de GitHub del mundo puede obtener credenciales de tu organización.** Es exactamente el mismo fallo que en AWS con un `sub` sin acotar y en Azure con un `subject` vacío, y es la tercera confirmación del mismo contrato: la parte peligrosa de una federación nunca es el emisor, es **el sujeto**.

Lo que sí cambia es la forma de conceder, que aquí es más expresiva. En vez de asociar la federación a una única identidad, se conceden roles a un **conjunto de principales**:

```bash
$ gcloud iam service-accounts add-iam-policy-binding \
    despliegue@cls-tienda-prod-euw1-01.iam.gserviceaccount.com \
    --role roles/iam.workloadIdentityUser \
    --member "principalSet://iam.googleapis.com/projects/$NUM/locations/global/\
workloadIdentityPools/cls-ci/attribute.repository/cloudshop/tienda"
```

Ese formato permite conceder por atributo —todo lo que venga de un repositorio, o de una rama— sin enumerar identidades una a una. Es cómodo y es la misma cuerda de la que colgarse: un `principalSet` con un atributo demasiado amplio concede a más de lo previsto.

Y la prueba negativa, que es la única evidencia aceptable y ya se ha ejecutado en tres plataformas:

```text
desde otro repositorio                    permiso denegado    ✓
desde cloudshop/tienda, rama de trabajo   permiso denegado    ✓
desde cloudshop/tienda, rama main         testigo emitido     ✓
```

Dos mecanismos más completan el modelo, y conviene situarlos:

**Condiciones en las concesiones.** Una concesión puede llevar una expresión que la limite en el tiempo o por nombre de recurso. Es el privilegio mínimo **en el tiempo** de la clase 038, más simple que la activación con aprobación de allí y suficiente para un acceso temporal:

```bash
$ gcloud projects add-iam-policy-binding cls-tienda-prod-euw1-01 \
    --member "user:ana@cloudshop.example" --role roles/run.admin \
    --condition "expression=request.time < timestamp('2026-08-15T00:00:00Z'),\
title=incidente-4821,description=acceso temporal"
```

La concesión **caduca sola**. Eso elimina la deuda de accesos que nadie retira, que es de donde salen la mitad de los permisos excesivos de cualquier organización con dos años de vida.

**Políticas de denegación.** Se evalúan **antes** que las concesiones y ganan siempre, y se adjuntan a la organización, la carpeta o el proyecto:

```text
orden de evaluación
  1. políticas de denegación   ¿hay una regla que quite este permiso? → fin
  2. concesiones               ¿hay alguna que lo dé? → permitido
  3. políticas de organización ¿la configuración resultante está permitida?
```

Son la pieza que faltaba para acotar un rol amplio sin rehacerlo: negar `iam.serviceAccounts.getAccessToken` sobre las cuentas de producción a todo el mundo salvo a un grupo, por ejemplo. Y conviven con las políticas de organización sin sustituirlas, porque responden preguntas distintas: la denegación dice **qué permisos no tienes**; la política de organización dice **qué configuraciones no son válidas**, tengas el permiso que tengas.

### 5. Reducir privilegios con datos en vez de con criterio

Todas las plataformas del programa han pedido privilegio mínimo y ninguna ha ofrecido hasta ahora una forma no subjetiva de conseguirlo. Aquí sí la hay, y merece ser el cierre de la clase porque cambia la conversación.

El recomendador observa el uso real de los últimos 90 días y propone el rol ajustado:

```bash
$ gcloud recommender recommendations list \
    --project cls-tienda-prod-euw1-01 --location global \
    --recommender google.iam.policy.Recommender \
    --format "table(content.overview.member, content.overview.removedRole,
                    content.overview.addedRole)"
```

```text
miembro                       rol retirado    rol propuesto
sa-tienda-web@…               roles/editor    roles/run.invoker
                                              roles/secretmanager.secretAccessor
sa-informes@…                 roles/editor    roles/bigquery.dataViewer
user:carlos@cloudshop.example roles/owner     roles/viewer
```

Esto convierte una discusión —«¿de verdad necesitas Editor?»— en un dato: durante 90 días esa identidad usó tres permisos de los cientos que tenía. Y tiene dos límites que hay que decir en voz alta para no crear una falsa confianza:

```text
1. una acción que solo ocurre una vez al trimestre no aparece en 90 días
   → aplicar la recomendación puede romper el cierre anual
2. mide lo USADO, no lo NECESARIO
   → un permiso usado por error sigue apareciendo como usado
```

La forma responsable de aplicarlo es por pasos y con vuelta atrás preparada:

```text
1. aplicar en no producción y observar dos semanas
2. en producción, empezar por identidades de carga de trabajo
   (su comportamiento es más predecible que el de las personas)
3. conservar el permiso para procesos periódicos conocidos aunque
   no aparezcan en la ventana
4. registrar los errores de permiso en un panel: son la señal
   de que se recortó de más, y aparecen en minutos
```

El punto 4 es el que hace segura la operación. Un `PERMISSION_DENIED` es visible, inmediato y reversible; un permiso de más es invisible durante años. **La asimetría favorece recortar**, y esa es la razón por la que conviene hacerlo con datos y no esperar a tener certeza.

Y para diagnosticar un acceso denegado concreto, el orden que acota el problema, con la misma estructura de las clases 038 y 026:

```bash
# 1. ¿por qué se deniega ESTA llamada a ESTE recurso para ESTA identidad?
$ gcloud policy-intelligence troubleshoot-policy iam \
    --principal-email sa-tienda-web@cls-tienda-prod-euw1-01.iam.gserviceaccount.com \
    --resource-name //storage.googleapis.com/projects/_/buckets/cls-tienda-facturas \
    --permission storage.objects.get
```

La respuesta indica si falta la concesión, si hay una política de denegación que gana o si una condición no se cumple. Y si nada de eso explica el fallo, el error no es de IAM: es de una política de organización, y el mensaje lo dirá con otro texto. Tres plataformas, tres vocabularios y **la misma pregunta**: ¿en qué sistema está la regla que me impide esto?

## 🔬 Ejemplo trabajado

**CloudShop configura la identidad de su plataforma en Google Cloud. Llega con el contrato de las clases 026 y 038 y lo aplica en un día. Después aparecen cuatro cosas que ese contrato no cubría, y tres de ellas son la misma pieza vista desde ángulos distintos: la cuenta de servicio como recurso.**

**Hallazgo 1 — todas las máquinas ejecutan con Editor.**

La revisión inicial de permisos sobre el proyecto de tienda:

```bash
$ gcloud projects get-iam-policy cls-tienda-prod-euw1-01 \
    --flatten="bindings[].members" --filter="bindings.role:roles/editor" \
    --format="value(bindings.members)"
serviceAccount:418293047512-compute@developer.gserviceaccount.com
```

Seis máquinas y dos grupos de instancias usaban esa cuenta por omisión. Cualquier dependencia comprometida en cualquiera de ellas podía leer todos los secretos del proyecto, modificar la base de datos y crear recursos.

```text                                        antes           después
cuentas con roles/editor                        2                0
cuentas de servicio dedicadas                   0                7
roles por carga de trabajo                  editor      3,1 roles de media
concesiones automáticas por defecto        activas    desactivadas por política
ámbito de acceso de las máquinas          heredado      cloud-platform + IAM
```

**Hallazgo 2 — Ana era «Viewer» y podía desplegar en producción.**

Una auditoría de accesos cruzada con el analizador de políticas:

```bash
$ gcloud asset analyze-iam-policy --organization=$ORG_ID \
    --analyze-service-account-impersonation \
    --identity="user:ana@cloudshop.example" --format="value(…)"
ana@cloudshop.example → despliegue@cls-tienda-prod (tokenCreator)
                      → despliegue tiene roles/editor
```

El rol propio de Ana era `roles/viewer`. Su permiso efectivo era `Editor` sobre producción, por un camino que ninguna tabla de roles de usuario mostraba. Y no era un caso aislado:

```text                                        antes         después
personas con acceso efectivo a producción       11              3
caminos de suplantación no previstos             7              0
concesiones de tokenCreator                     11    3, con caducidad de 8 h
revisión de permisos                    tabla de roles   analizador de políticas
```

La corrección de fondo no fue quitar permisos: fue **cambiar qué se revisa**. Una revisión que mira solo los roles directos no puede encontrar esto.

**Hallazgo 3 — catorce claves, una en un repositorio público.**

```bash
$ gcloud asset search-all-resources --scope organizations/$ORG_ID \
    --asset-types iam.googleapis.com/ServiceAccountKey \
    --query "NOT name:*/keys/system-managed*" --format="value(name)" | wc -l
14
```

Una de ellas apareció en un repositorio público de un antiguo becario, con la cuenta `informes@`, que tenía `roles/bigquery.dataViewer` sobre el conjunto de datos de ventas. Estuvo accesible cuatro meses.

La migración, por casos de uso y en este orden:

```text                            antes              después
canalizaciones de CI            5 claves      federación con condición de atributo
cargas en Compute y Cloud Run   6 claves      cuenta de servicio adjunta
herramientas de personas        3 claves      suplantación con el propio acceso
claves restantes                  14                    0
creación de claves nuevas      permitida      bloqueada por política
```

Y la prueba negativa de la federación, la tercera vez que se ejecuta la misma prueba en este programa:

```text
desde otro repositorio                       permiso denegado    ✓
desde cloudshop/tienda, rama de trabajo      permiso denegado    ✓
desde cloudshop/tienda, rama main            testigo emitido     ✓
```

**Hallazgo 4 — el recomendador dice que sobra el 96 % de los permisos.**

Tras 90 días de operación con las cuentas dedicadas ya creadas:

```text
identidad             permisos concedidos   usados en 90 días
sa-tienda-web                    412                7
sa-procesador                    412               11
sa-informes                      189                4
```

Las recomendaciones se aplican por pasos, empezando por las cuentas de carga de trabajo, y con el panel de errores de permiso vigilando:

```text                            antes        después
permisos concedidos (suma)        1.013            34
errores PERMISSION_DENIED
  en las 2 semanas siguientes        —              3
de los cuales, recortes de más     —      2, restaurados en 20 min
el tercero                         —      un proceso trimestral no visible
                                          en la ventana de 90 días
```

El tercero es el interesante y confirma el límite que había que declarar: un cierre trimestral no aparece en una ventana de noventa días. Se restauró su permiso con una condición que lo limita a los cinco primeros días de cada trimestre.

**Resumen del modelo de identidad:**

```text                                          antes         después
cuentas con rol básico                            2               0
claves de cuenta de servicio                     14               0
personas con acceso efectivo a producción        11               3
caminos de suplantación no previstos              7               0
permisos concedidos (suma de las tres cuentas) 1.013              34
concesiones con caducidad                         0               6
prueba negativa de la federación                 no        sí, tres casos
```

**La lección que esta clase traslada al resto de la parte 04**: el contrato de identidad de las partes 02 y 03 se reutilizó entero —sin secretos, federación acotada por sujeto, privilegio mínimo, prueba negativa— y aun así hubo cuatro hallazgos, porque **la cuenta de servicio es un recurso además de una identidad y eso duplica las preguntas de permiso**. Una auditoría que mire solo quién tiene qué rol es correcta y está incompleta: en Google Cloud hay que preguntar además a quién puede suplantar cada quien, y responderlo requiere una herramienta, no una hoja de cálculo.

## 🧪 Laboratorio guiado

Ejecuta desde la raíz:

```bash
python classes/part-04-gcp-core-platform/050-iam-service-accounts-y-workload-identity-federation/lab.py
```

El laboratorio selecciona el motor de práctica **`iam`** y produce
`lab_result.json`. El escenario, sus comprobaciones y el artefacto esperado corresponden a
esta clase; no requiere credenciales y deja explícito qué debe revalidarse en un sandbox real.

1. Lee `exercise.steps` y formula una predicción antes de ejecutar.
2. Ejecuta la práctica y verifica todos los elementos de `checks`.
3. Provoca el caso de `negative_test` y explica la señal observada.
4. Materializa `identidad-gcp` en `evidence/` usando la plantilla indicada.
5. Para proveedor real, sigue `sandbox.requires`, registra costo y ejecuta `destroy`.

### Evidencia esperada

El artefacto principal es una matriz de acceso mínimo con prueba de denegación. Además, la entrega debe incluir el comando ejecutado,
la salida estructurada y una conclusión que no exceda lo observado.

## 🏆 Reto verificable

Construye **`identidad-gcp`** para el caso CloudShop. Incluye una alternativa descartada,
un supuesto que pueda falsarse, una prueba de fallo y una decisión de rollback.

## ✅ Criterio de aceptación

- [ ] `lab.py` termina con código 0 y genera JSON válido.
- [ ] La entrega conecta al menos tres requisitos con mecanismos verificables.
- [ ] Existe una prueba positiva y una prueba negativa con evidencia.
- [ ] Seguridad, costo y operación aparecen como decisiones, no como anexos.
- [ ] Se declara una limitación y una condición que obligaría a revisar el diseño.
- [ ] Otra persona puede repetir el recorrido sin conocimiento tácito.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Una persona con rol de solo lectura despliega en producción | Tiene permiso para suplantar o adjuntar una cuenta de servicio privilegiada | Audita con el analizador de políticas incluyendo suplantación, y limita `serviceAccountTokenCreator` y `serviceAccountUser` con concesiones caducas. |
| Una máquina virtual puede modificar casi todo el proyecto | Usa la cuenta de servicio por defecto, que recibe `roles/editor` automáticamente | Desactiva las concesiones automáticas por política y crea una cuenta dedicada por carga con roles mínimos. |
| La cuenta tiene el rol correcto y la llamada sigue fallando en una máquina antigua | Los ámbitos de acceso de Compute Engine intersecan con IAM y no incluyen esa API | Fija el ámbito en `cloud-platform` y controla exclusivamente con roles de IAM. |
| Una credencial filtrada sigue siendo válida meses después | Es una clave de cuenta de servicio, que no caduca | Sustituye por identidad adjunta, suplantación o federación, y bloquea la creación de claves con una política de organización. |
| Un repositorio ajeno obtiene credenciales de la organización | El proveedor de identidad federada no tiene condición de atributo | Acota con `--attribute-condition` sobre repositorio y rama, y verifica con las tres pruebas negativas. |
| Aplicar las recomendaciones de privilegio rompe un proceso trimestral | El recomendador observa 90 días y un proceso trimestral puede no aparecer | Conserva los permisos de procesos periódicos conocidos, vigila los errores de permiso y restaura con una concesión condicionada a su ventana. |

## 🛡️ Seguridad, ética y costo

Trabaja con cuentas propias o sandboxes autorizados. No publiques secretos, identificadores
reales ni datos personales. Antes de crear recursos pagos define presupuesto, etiquetas y
comando de destrucción; después verifica que no queden recursos huérfanos. Los ejemplos
locales enseñan contratos, pero no certifican cumplimiento ni disponibilidad de producción.

## ❓ Preguntas de comprobación

1. ¿Cuáles son las dos caras de una cuenta de servicio y qué pregunta se salta una auditoría que solo mira los roles de las personas?
2. ¿Por qué `serviceAccountUser` sobre una cuenta con `Editor` equivale a tener `Editor`?
3. ¿Qué se concede automáticamente al habilitar Compute Engine y cómo se impide?
4. Enumera las cuatro alternativas a una clave de cuenta de servicio y en qué caso corresponde cada una.
5. ¿En qué orden se evalúan las políticas de denegación, las concesiones y las políticas de organización?

## 🔗 Referencias

- Google Cloud (2025). *Service accounts overview* — identidad y recurso, suplantación y adjunción. <https://cloud.google.com/iam/docs/service-account-overview>
- Google Cloud (2025). *Best practices for using service accounts* — claves, alternativas y cuentas por defecto. <https://cloud.google.com/iam/docs/best-practices-service-accounts>
- Google Cloud (2025). *Workload Identity Federation* — grupos, proveedores, mapeo y condición de atributo. <https://cloud.google.com/iam/docs/workload-identity-federation>
- Google Cloud (2025). *IAM deny policies* — reglas de denegación y orden de evaluación. <https://cloud.google.com/iam/docs/deny-overview>
- Google Cloud (2025). *Role recommendations* — reducción de privilegios a partir del uso observado y sus límites. <https://cloud.google.com/policy-intelligence/docs/role-recommendations-overview>
- Documentación oficial vigente del servicio implementado; registra URL y fecha de consulta.

---

> [Evaluación](assessment.md) · [Contrato de clase](lesson.yaml) · [Índice de la parte](../README.md)

**📥 Descargar:** [Parte 04 en PDF](../../../site/downloads/partes/manual-parte-04-gcp-core-platform.pdf) · [Recorrido de Google Cloud en PDF](../../../site/downloads/nubes/manual-google-cloud.pdf) · [Manual integral](../../../site/downloads/multi-cloud-engineering-manual-v2.0.pdf)

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 049 · Organización, folders, proyectos, billing y cuotas](../../part-04-gcp-core-platform/049-organizacion-folders-proyectos-billing-y-cuotas/README.md) | [Parte 04](../README.md) · [Programa](../../README.md) | [051 · VPC global, subredes regionales, firewall y Cloud NAT →](../../part-04-gcp-core-platform/051-vpc-global-subredes-regionales-firewall-y-cloud-nat/README.md) |
