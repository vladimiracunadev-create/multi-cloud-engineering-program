const REPO = "https://github.com/vladimiracunadev-create/multi-cloud-engineering-program";
const PROGRESS_KEY = "multicloud-progress-v2";
const SAVED_KEY = "multicloud-saved-v1";
const THEME_KEY = "multicloud-theme";

const state = {
  catalog: [],
  done: new Set(JSON.parse(localStorage.getItem(PROGRESS_KEY) || localStorage.getItem("multicloud-progress") || "[]")),
  saved: new Set(JSON.parse(localStorage.getItem(SAVED_KEY) || "[]")),
  view: location.hash.slice(1) || "dashboard",
  query: "",
  part: "all",
  level: "all",
  lab: "all",
  status: "all",
  sort: "sequence",
  route: null,
  visibleLessons: 60,
};

const partColors = ["#59c88b", "#e4ad4d", "#62bcc9", "#df7b72", "#c3b36a"];
const stageColors = ["#59c88b", "#e4ad4d", "#62bcc9", "#df7b72", "#c3b36a"];
const $ = (selector) => document.querySelector(selector);

const routes = [
  { id: "cloud", title: "Cloud Engineer", parts: ["00", "01", "02", "05", "07", "10", "11", "14"], color: "#59c88b" },
  { id: "devops", title: "DevOps Engineer", parts: ["00", "05", "06", "07", "08", "10", "11"], color: "#62bcc9" },
  { id: "platform", title: "Platform Engineer", parts: ["05", "06", "07", "08", "10", "11", "14"], color: "#e4ad4d" },
  { id: "sre", title: "Site Reliability Engineer", parts: ["00", "05", "06", "08", "10", "12", "14"], color: "#df7b72" },
  { id: "architect", title: "Cloud Architect", parts: ["01", "02", "03", "04", "09", "11", "12", "13", "14"], color: "#c3b36a" },
];

const roadmapStages = [
  { name: "Base", subtitle: "Comprender antes de aprovisionar", parts: ["00", "01"] },
  { name: "Proveedores", subtitle: "Tres implementaciones comparables", parts: ["02", "03", "04"] },
  { name: "Plataforma", subtitle: "Portabilidad y entrega", parts: ["05", "06", "07", "08"] },
  { name: "Operación", subtitle: "Datos, SRE y gobierno", parts: ["09", "10", "11", "12"] },
  { name: "Experto", subtitle: "Continuidad y defensa", parts: ["13", "14"] },
];

const capstoneLabels = ["Servicio local", "ADR cloud", "AWS", "Azure", "GCP", "OCI", "Kubernetes", "IaC", "Entrega", "Eventos", "SRE", "Guardrails", "Arquitectura", "DR", "Defensa"];

function toast(message) {
  const element = $("#toast");
  element.textContent = message;
  element.classList.add("show");
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => element.classList.remove("show"), 1800);
}

function saveState() {
  localStorage.setItem(PROGRESS_KEY, JSON.stringify([...state.done].sort()));
  localStorage.setItem(SAVED_KEY, JSON.stringify([...state.saved].sort()));
  updateGlobalProgress();
}

function applyTheme(theme) {
  document.documentElement.dataset.theme = theme;
  localStorage.setItem(THEME_KEY, theme);
  drawCharts();
}

function lessonPath(item) { return `classes/${item.id}.html`; }
function sourceFolder(item) { return `classes/part-${item.part}-${item.part_slug}/${item.id}-${item.slug}`; }
function labCommand(item) { return `python ${sourceFolder(item)}/lab.py --seed 42`; }

function nextLesson() {
  return state.catalog.find((item) => !state.done.has(item.id)) || state.catalog.at(-1);
}

function updateGlobalProgress() {
  if (!state.catalog.length) return;
  const percent = Math.round((state.done.size / state.catalog.length) * 100);
  $("#hero-progress").value = state.done.size;
  $("#hero-progress-label").textContent = `${percent}%`;
  $("#hero-progress-detail").textContent = `${state.done.size} de ${state.catalog.length} clases`;
  $("#curriculum-progress").textContent = `${percent}%`;
  const next = nextLesson();
  if (next) {
    $("#continue-course").href = lessonPath(next);
    $("#next-title").textContent = `Clase ${next.id}`;
    $("#next-description").textContent = next.title;
    $("#next-meta").innerHTML = `<span>Parte ${next.part}</span><span>${next.level}</span><span>${next.lab_kind}</span><span>${next.estimated_hours} h</span>`;
    $("#next-command").textContent = labCommand(next);
    $("#next-link").href = lessonPath(next);
  }
}

function setView(view, updateHash = true) {
  if (!document.querySelector(`[data-view="${view}"]`)) view = "dashboard";
  state.view = view;
  document.querySelectorAll(".app-view").forEach((element) => element.classList.toggle("active", element.dataset.view === view));
  document.querySelectorAll(".nav-tab").forEach((button) => button.classList.toggle("active", button.dataset.viewTarget === view));
  if (updateHash) history.replaceState(null, "", `#${view}`);
  renderView(view);
  scrollTo({ top: 0, behavior: "auto" });
}

function groupByPart(items = state.catalog) {
  const grouped = new Map();
  for (const item of items) {
    if (!grouped.has(item.part)) grouped.set(item.part, []);
    grouped.get(item.part).push(item);
  }
  return [...grouped.entries()];
}

function populateFilters() {
  for (const [part, items] of groupByPart()) {
    $("#part-filter").insertAdjacentHTML("beforeend", `<option value="${part}">${part} · ${items[0].part_title}</option>`);
  }
  for (const level of [...new Set(state.catalog.map((item) => item.level))]) {
    $("#level-filter").insertAdjacentHTML("beforeend", `<option value="${level}">${level}</option>`);
  }
  const labKinds = [...new Set(state.catalog.map((item) => item.lab_kind))].sort();
  for (const lab of labKinds) $("#lab-filter").insertAdjacentHTML("beforeend", `<option value="${lab}">${lab}</option>`);
}

function renderRoutes() {
  $("#route-grid").innerHTML = routes.map((route) => {
    const lessons = state.catalog.filter((item) => route.parts.includes(item.part));
    const complete = lessons.filter((item) => state.done.has(item.id)).length;
    return `<button class="route-card" data-route="${route.id}" style="--route-color:${route.color}"><strong>${route.title}</strong><span>${lessons.length} clases · ${route.parts.length} partes</span><b>${complete}/${lessons.length} completadas →</b></button>`;
  }).join("");
}

function filteredLessons() {
  const query = state.query.trim().toLocaleLowerCase("es");
  const items = state.catalog.filter((item) => {
    const haystack = `${item.title} ${item.part_title} ${item.keywords.join(" ")} ${item.lab_kind}`.toLocaleLowerCase("es");
    const statusMatch = state.status === "all"
      || (state.status === "done" && state.done.has(item.id))
      || (state.status === "pending" && !state.done.has(item.id))
      || (state.status === "saved" && state.saved.has(item.id));
    return (!query || haystack.includes(query))
      && (state.part === "all" || item.part === state.part)
      && (state.level === "all" || item.level === state.level)
      && (state.lab === "all" || item.lab_kind === state.lab)
      && (!state.route || state.route.parts.includes(item.part))
      && statusMatch;
  });
  if (state.sort === "title") items.sort((a, b) => a.title.localeCompare(b.title, "es"));
  if (state.sort === "hours") items.sort((a, b) => b.estimated_hours - a.estimated_hours || a.number - b.number);
  return items;
}

function renderCurriculum() {
  const items = filteredLessons();
  const visibleItems = items.slice(0, state.visibleLessons);
  const root = $("#curriculum-list");
  root.innerHTML = groupByPart(visibleItems).map(([part, lessons]) => {
    const color = partColors[Number(part) % partColors.length];
    return `<section class="part-group" style="--part-color:${color}">
      <header class="part-group-header"><span class="part-number">P${part}</span><div><h2>${lessons[0].part_title}</h2><p>${lessons.length} clases visibles</p></div><a href="parts/${part}.html">Abrir parte →</a></header>
      <div class="class-table">${lessons.map((item) => `<article class="class-row${state.done.has(item.id) ? " done" : ""}" data-class-id="${item.id}">
        <input type="checkbox" data-complete="${item.id}" aria-label="Marcar clase ${item.id}" ${state.done.has(item.id) ? "checked" : ""}>
        <span class="class-id">${item.id}</span>
        <a class="class-title" href="${lessonPath(item)}">${item.title}</a>
        <span class="class-lab">${item.lab_kind}</span>
        <span class="class-level">${item.level}</span>
        <span class="class-hours">${item.estimated_hours} h</span>
        <div class="class-actions"><button data-save="${item.id}" class="${state.saved.has(item.id) ? "saved" : ""}" title="Guardar clase" aria-label="Guardar clase">★</button><a href="${lessonPath(item)}#assessment" title="Evaluación" aria-label="Evaluación">✓</a><a href="${REPO}/blob/main/${sourceFolder(item)}/lab.py" title="Laboratorio" aria-label="Laboratorio">⌘</a></div>
      </article>`).join("")}</div>
    </section>`;
  }).join("");
  $("#result-count").textContent = `${items.length} clases`;
  $("#result-hours").textContent = `${items.reduce((sum, item) => sum + item.estimated_hours, 0)} horas`;
  $("#empty-state").hidden = items.length !== 0;
  const loadMore = $("#load-more");
  const remaining = Math.max(0, items.length - visibleItems.length);
  loadMore.hidden = remaining === 0;
  loadMore.textContent = `Mostrar ${Math.min(60, remaining)} clases más`;
}

function renderRoadmap() {
  const grouped = new Map(groupByPart());
  $("#roadmap").innerHTML = roadmapStages.map((stage, stageIndex) => `<section class="roadmap-stage" style="--stage-color:${stageColors[stageIndex]}"><header><span class="eyebrow">Etapa ${stageIndex + 1}</span><h2>${stage.name}</h2><small>${stage.subtitle}</small></header><div class="roadmap-stage-list">${stage.parts.map((part) => {
    const items = grouped.get(part);
    const done = items.filter((item) => state.done.has(item.id)).length;
    return `<a class="roadmap-node" href="parts/${part}.html"><span>PARTE ${part}</span><strong>${items[0].part_title}</strong><small>${done}/12 · ${items.reduce((sum, item) => sum + item.estimated_hours, 0)} h</small></a>`;
  }).join("")}</div></section>`).join("");
  $("#capstone-timeline").innerHTML = capstoneLabels.map((label, index) => `<div class="timeline-item" style="--timeline-color:${partColors[index % partColors.length]}"><strong>P${String(index).padStart(2, "0")}</strong><span>${label}</span></div>`).join("");
}

function renderView(view) {
  if (view === "dashboard") renderRoutes();
  if (view === "curriculum") renderCurriculum();
  if (view === "roadmap") renderRoadmap();
  if (view === "analytics" || view === "dashboard") requestAnimationFrame(drawCharts);
}

function refreshCurriculum() {
  state.visibleLessons = 60;
  renderCurriculum();
}

function chartColors() {
  const styles = getComputedStyle(document.documentElement);
  return { text: styles.getPropertyValue("--text").trim(), muted: styles.getPropertyValue("--muted").trim(), line: styles.getPropertyValue("--line").trim(), surface: styles.getPropertyValue("--surface-2").trim(), green: styles.getPropertyValue("--green").trim(), amber: styles.getPropertyValue("--amber").trim(), cyan: styles.getPropertyValue("--cyan").trim(), coral: styles.getPropertyValue("--coral").trim() };
}

function setupCanvas(canvas) {
  if (!canvas || canvas.clientWidth === 0) return null;
  const ratio = devicePixelRatio || 1;
  const width = canvas.clientWidth;
  const height = canvas.clientHeight;
  canvas.width = width * ratio;
  canvas.height = height * ratio;
  const context = canvas.getContext("2d");
  context.scale(ratio, ratio);
  context.clearRect(0, 0, width, height);
  return { context, width, height };
}

function drawProgressChart() {
  const setup = setupCanvas($("#progress-chart")); if (!setup) return;
  const { context: ctx, width, height } = setup; const colors = chartColors();
  const stageValues = roadmapStages.map((stage) => {
    const lessons = state.catalog.filter((item) => stage.parts.includes(item.part));
    return { name: stage.name, value: lessons.filter((item) => state.done.has(item.id)).length / lessons.length };
  });
  const barWidth = Math.min(62, (width - 70) / stageValues.length - 16); const base = height - 34; const maxHeight = height - 66;
  ctx.font = "11px Inter, sans-serif"; ctx.textAlign = "center";
  stageValues.forEach((item, index) => {
    const x = 48 + index * ((width - 70) / stageValues.length); const h = Math.max(3, maxHeight * item.value);
    ctx.fillStyle = colors.surface; ctx.fillRect(x, base - maxHeight, barWidth, maxHeight);
    ctx.fillStyle = stageColors[index]; ctx.fillRect(x, base - h, barWidth, h);
    ctx.fillStyle = colors.text; ctx.fillText(`${Math.round(item.value * 100)}%`, x + barWidth / 2, base - h - 7);
    ctx.fillStyle = colors.muted; ctx.fillText(item.name, x + barWidth / 2, base + 18);
  });
}

function drawDonut() {
  const setup = setupCanvas($("#completion-donut")); if (!setup) return;
  const { context: ctx, width, height } = setup; const colors = chartColors();
  const ratio = state.catalog.length ? state.done.size / state.catalog.length : 0; const x = width / 2; const y = height / 2; const radius = Math.min(width, height) * .31;
  ctx.lineWidth = 22; ctx.lineCap = "butt"; ctx.strokeStyle = colors.surface; ctx.beginPath(); ctx.arc(x, y, radius, 0, Math.PI * 2); ctx.stroke();
  ctx.strokeStyle = colors.green; ctx.beginPath(); ctx.arc(x, y, radius, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * ratio); ctx.stroke();
  ctx.fillStyle = colors.text; ctx.font = "700 34px Inter, sans-serif"; ctx.textAlign = "center"; ctx.fillText(`${Math.round(ratio * 100)}%`, x, y + 4);
  ctx.fillStyle = colors.muted; ctx.font = "11px Inter, sans-serif"; ctx.fillText(`${state.done.size} de ${state.catalog.length}`, x, y + 25);
}

function drawHorizontalBars(canvas, data, colorAccessor) {
  const setup = setupCanvas(canvas); if (!setup) return;
  const { context: ctx, width, height } = setup; const colors = chartColors(); const left = 74; const right = 35; const rowHeight = (height - 28) / data.length; const max = Math.max(...data.map((item) => item.value), 1);
  ctx.font = "10px Inter, sans-serif";
  data.forEach((item, index) => {
    const y = 14 + index * rowHeight; const barWidth = (width - left - right) * item.value / max;
    ctx.fillStyle = colors.surface; ctx.fillRect(left, y, width - left - right, Math.max(8, rowHeight - 8));
    ctx.fillStyle = colorAccessor(item, index); ctx.fillRect(left, y, barWidth, Math.max(8, rowHeight - 8));
    ctx.fillStyle = colors.muted; ctx.textAlign = "right"; ctx.fillText(item.label, left - 8, y + Math.max(8, rowHeight - 8) / 2 + 3);
    ctx.fillStyle = colors.text; ctx.textAlign = "left"; ctx.fillText(item.value, Math.min(width - 24, left + barWidth + 7), y + Math.max(8, rowHeight - 8) / 2 + 3);
  });
}

function drawCharts() {
  if (!state.catalog.length) return;
  drawProgressChart(); drawDonut();
  const hours = groupByPart().map(([part, items]) => ({ label: `P${part}`, value: items.reduce((sum, item) => sum + item.estimated_hours, 0) }));
  drawHorizontalBars($("#hours-bars"), hours, (_, index) => partColors[index % partColors.length]);
  const labCounts = new Map();
  for (const item of state.catalog) labCounts.set(item.lab_kind, (labCounts.get(item.lab_kind) || 0) + 1);
  const counts = [...labCounts.entries()].map(([label, value]) => ({ label, value })).sort((a, b) => b.value - a.value).slice(0, 10);
  drawHorizontalBars($("#labs-bars"), counts, (_, index) => stageColors[index % stageColors.length]);
}

function exportProgress() {
  const payload = { program: "multi-cloud-engineering-program", version: 1, exported_at: new Date().toISOString(), completed: [...state.done].sort(), saved: [...state.saved].sort() };
  const url = URL.createObjectURL(new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" }));
  const link = document.createElement("a"); link.href = url; link.download = "multi-cloud-progress.json"; link.click(); URL.revokeObjectURL(url); toast("Progreso exportado");
}

async function importProgress(file) {
  const payload = JSON.parse(await file.text());
  if (payload.program !== "multi-cloud-engineering-program" || !Array.isArray(payload.completed)) throw new Error("Archivo de progreso no válido");
  state.done = new Set(payload.completed); state.saved = new Set(payload.saved || []); saveState(); renderAll(); toast("Progreso importado");
}

function renderAll() { updateGlobalProgress(); renderView(state.view); }

function bindEvents() {
  document.addEventListener("click", async (event) => {
    const viewButton = event.target.closest("[data-view-target]"); if (viewButton) setView(viewButton.dataset.viewTarget);
    const statusButton = event.target.closest("[data-status]"); if (statusButton) { document.querySelectorAll("[data-status]").forEach((button) => button.classList.remove("active")); statusButton.classList.add("active"); state.status = statusButton.dataset.status; refreshCurriculum(); }
    const saveButton = event.target.closest("[data-save]"); if (saveButton) { const id = saveButton.dataset.save; state.saved.has(id) ? state.saved.delete(id) : state.saved.add(id); saveState(); renderCurriculum(); }
    const routeButton = event.target.closest("[data-route]"); if (routeButton) { const route = routes.find((item) => item.id === routeButton.dataset.route); state.route = route; state.part = "all"; state.query = ""; state.status = "all"; state.visibleLessons = 60; $("#part-filter").value = "all"; setView("curriculum"); $("#global-search").value = ""; toast(`Ruta activa: ${route.title}`); }
    if (event.target.closest("#load-more")) { state.visibleLessons += 60; renderCurriculum(); }
  });
  document.addEventListener("change", (event) => {
    if (event.target.matches("[data-complete]")) { event.target.checked ? state.done.add(event.target.dataset.complete) : state.done.delete(event.target.dataset.complete); saveState(); renderAll(); }
  });
  $("#global-search").addEventListener("input", (event) => { state.query = event.target.value; state.visibleLessons = 60; if (state.query && state.view !== "curriculum") setView("curriculum"); else if (state.view === "curriculum") renderCurriculum(); });
  $("#part-filter").addEventListener("change", (event) => { state.route = null; state.part = event.target.value; refreshCurriculum(); });
  $("#level-filter").addEventListener("change", (event) => { state.level = event.target.value; refreshCurriculum(); });
  $("#lab-filter").addEventListener("change", (event) => { state.lab = event.target.value; refreshCurriculum(); });
  $("#sort-control").addEventListener("change", (event) => { state.sort = event.target.value; refreshCurriculum(); });
  $("#theme-toggle").addEventListener("click", () => applyTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark"));
  $("#data-menu-toggle").addEventListener("click", () => { $("#data-menu").hidden = !$("#data-menu").hidden; });
  $("#export-progress").addEventListener("click", exportProgress); $("#analytics-export").addEventListener("click", exportProgress);
  $("#import-progress").addEventListener("click", () => $("#progress-file").click());
  $("#progress-file").addEventListener("change", async (event) => { try { await importProgress(event.target.files[0]); } catch (error) { toast(error.message); } event.target.value = ""; });
  $("#reset-progress").addEventListener("click", () => { if (confirm("¿Reiniciar todo el progreso y las clases guardadas?")) { state.done.clear(); state.saved.clear(); saveState(); renderAll(); toast("Progreso reiniciado"); } });
  $("#copy-next-command").addEventListener("click", async () => { await navigator.clipboard.writeText($("#next-command").textContent); toast("Comando copiado"); });
  addEventListener("hashchange", () => setView(location.hash.slice(1), false));
  addEventListener("resize", () => requestAnimationFrame(drawCharts));
}

async function start() {
  applyTheme(localStorage.getItem(THEME_KEY) || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark"));
  const response = await fetch("catalog.json", { cache: "no-cache" }); if (!response.ok) throw new Error(`No se pudo cargar el catálogo: ${response.status}`);
  state.catalog = await response.json();
  populateFilters(); bindEvents(); updateGlobalProgress(); setView(state.view, false);
  if ("serviceWorker" in navigator && location.protocol.startsWith("http")) {
    navigator.serviceWorker.register("service-worker.js", { updateViaCache: "none" })
      .then((registration) => registration.update())
      .catch(() => {});
  }
}

start().catch((error) => { toast(error.message); console.error(error); });
