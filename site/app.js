const state = {
  catalog: [],
  query: "",
  part: "all",
  level: "all",
  progress: "all",
  done: new Set(JSON.parse(localStorage.getItem("multicloud-progress") || "[]")),
};

const partColors = ["#58c58a", "#e3a84d", "#62b8c7", "#dd7b75", "#a0c76a"];
const $ = (selector) => document.querySelector(selector);

function lessonUrl(item) {
  return `../classes/part-${item.part}-${item.part_slug}/${item.id}-${item.slug}/README.md`;
}

function saveProgress() {
  localStorage.setItem("multicloud-progress", JSON.stringify([...state.done].sort()));
  $("#progress").value = state.done.size;
  $("#progress-label").textContent = `${state.done.size} / ${state.catalog.length}`;
}

function options() {
  const parts = [...new Map(state.catalog.map((item) => [item.part, item.part_title]))];
  for (const [id, title] of parts) {
    $("#part-filter").insertAdjacentHTML("beforeend", `<option value="${id}">${id} · ${title}</option>`);
  }
  const levels = [...new Set(state.catalog.map((item) => item.level))];
  for (const level of levels) {
    $("#level-filter").insertAdjacentHTML("beforeend", `<option value="${level}">${level}</option>`);
  }
}

function filtered() {
  const query = state.query.trim().toLocaleLowerCase("es");
  return state.catalog.filter((item) => {
    const haystack = `${item.title} ${item.part_title} ${item.keywords.join(" ")}`.toLocaleLowerCase("es");
    const progressMatch = state.progress === "all" || (state.progress === "done") === state.done.has(item.id);
    return (!query || haystack.includes(query))
      && (state.part === "all" || item.part === state.part)
      && (state.level === "all" || item.level === state.level)
      && progressMatch;
  });
}

function render() {
  const items = filtered();
  const list = $("#class-list");
  list.replaceChildren();
  for (const item of items) {
    const row = document.createElement("article");
    row.className = `class-row${state.done.has(item.id) ? " done" : ""}`;
    row.style.setProperty("--part-color", partColors[Number(item.part) % partColors.length]);
    row.innerHTML = `
      <input class="class-check" type="checkbox" aria-label="Marcar clase ${item.id} como completada" ${state.done.has(item.id) ? "checked" : ""}>
      <span class="class-id">${item.id}</span>
      <a class="class-title" href="${lessonUrl(item)}">${item.title}</a>
      <span class="class-part">Parte ${item.part}<br>${item.lab_kind}</span>
      <span class="class-hours">${item.estimated_hours} h</span>`;
    row.querySelector(".class-check").addEventListener("change", (event) => {
      event.target.checked ? state.done.add(item.id) : state.done.delete(item.id);
      saveProgress();
      render();
    });
    list.append(row);
  }
  $("#visible-count").textContent = items.length;
  $("#hours-count").textContent = items.reduce((sum, item) => sum + item.estimated_hours, 0);
  $("#empty").hidden = items.length !== 0;
}

async function start() {
  const response = await fetch("catalog.json");
  if (!response.ok) throw new Error(`No se pudo cargar el catálogo: ${response.status}`);
  state.catalog = await response.json();
  options();
  saveProgress();
  render();

  $("#search").addEventListener("input", (event) => { state.query = event.target.value; render(); });
  $("#part-filter").addEventListener("change", (event) => { state.part = event.target.value; render(); });
  $("#level-filter").addEventListener("change", (event) => { state.level = event.target.value; render(); });
  document.querySelectorAll("[data-progress]").forEach((button) => {
    button.addEventListener("click", () => {
      document.querySelectorAll("[data-progress]").forEach((item) => item.classList.remove("active"));
      button.classList.add("active");
      state.progress = button.dataset.progress;
      render();
    });
  });
}

start().catch((error) => {
  $("#empty").hidden = false;
  $("#empty").textContent = error.message;
});
