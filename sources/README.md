# Registro de fuentes

`bibliography.json` es el registro de todas las obras que citan las clases del programa.
No se redacta a mano: se **recoge** de los bloques `## 🔗 Referencias` de las 288 clases.

## Por que existe

Las clases citaban fuentes reales, pero no habia forma de comprobarlo sin abrir las 288.
El registro convierte esas citas en una lista con localizador resoluble, y el verificador
convierte esa lista en una condicion de CI.

## Regla unica

Cada entrada necesita un **localizador resoluble**, en una de tres formas:

| Tipo | Localizador | Forma canonica |
|---|---|---|
| `book` | ISBN-13 con digito de control valido | `https://openlibrary.org/isbn/{isbn13}` |
| `paper` | DOI | `https://doi.org/{doi}` |
| `standard`, `reference`, `dataset` | URL https de la fuente primaria | la propia URL, con `accessed` |

Lo que no se resuelve **no se borra ni se rellena**: queda con `"status": "pendiente"` y un
`pending_reason` que dice por que. Un hueco declarado es informacion; uno rellenado por
intuicion es una invencion con formato de bibliografia.

## Las tres herramientas

```bash
python scripts/extract-sources     # recoge las citas de las clases y reconstruye el registro
python scripts/verify-sources      # offline, determinista, bloquea en CI
python scripts/refresh-sources     # en red, manual, NO bloquea
```

Estan separadas a proposito. `verify-sources` no abre una sola conexion: si la red entrara
en el CI, el CI se volveria inestable y se acabaria ignorando. `refresh-sources` es la unica
que sale a Internet, se ejecuta a mano o programada, y reporta lo que dejo de resolver
**sin borrarlo**.

## Campos de una entrada

| Campo | Que es |
|---|---|
| `id` | kebab-case estable, derivado de autoridad y titulo |
| `identity` | clave de deduplicacion: URL canonica, o autor + titulo para libros |
| `type` | `book`, `paper`, `standard`, `reference`, `dataset` |
| `locator` | el localizador resoluble; `null` mientras este pendiente |
| `source_url` | el enlace tal como lo cita la clase |
| `authority` | organismo que responde por la fuente |
| `accessed` | fecha de la ultima comprobacion en red (obligatoria en documentacion) |
| `used_in` | rutas de las clases que la citan |
| `usage` | por clase, el uso concreto que esa clase hace de la obra |
| `status` | `verificada` o `pendiente` |
| `pending_reason` | por que sigue pendiente |

## Que comprueba el verificador

1. el registro parsea y cumple el esquema;
2. todo `book` verificado tiene ISBN-13 valido; todo `paper`, DOI;
3. el `locator` coincide con la forma canonica de su tipo;
4. toda obra usada en una clase existe en el registro;
5. ninguna entrada del registro queda sin usar;
6. ningun bloque de fuentes se repite entre clases;
7. cada cita declara el uso que la clase hace de la obra;
8. las cifras del README coinciden con el recuento del registro.

Las cifras que muestra el README las produce `verify-sources --write`. No se escriben a mano.
