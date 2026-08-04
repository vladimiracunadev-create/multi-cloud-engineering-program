const root = document.documentElement;
const progressKey = "multicloud-progress-v2";
const themeKey = "multicloud-theme";
const done = new Set(JSON.parse(localStorage.getItem(progressKey) || "[]"));

function applyTheme(theme) {
  root.dataset.theme = theme;
  localStorage.setItem(themeKey, theme);
}

applyTheme(localStorage.getItem(themeKey) || (matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark"));

document.querySelectorAll("[data-lesson-complete]").forEach((input) => {
  const id = input.dataset.lessonComplete;
  input.checked = done.has(id);
  input.addEventListener("change", () => {
    input.checked ? done.add(id) : done.delete(id);
    localStorage.setItem(progressKey, JSON.stringify([...done].sort()));
    document.querySelectorAll(`[data-lesson-complete="${id}"]`).forEach((peer) => { peer.checked = input.checked; });
  });
});

document.querySelector("#theme-toggle")?.addEventListener("click", () => {
  applyTheme(root.dataset.theme === "dark" ? "light" : "dark");
});

document.querySelector("#copy-link")?.addEventListener("click", async (event) => {
  await navigator.clipboard.writeText(location.href);
  event.currentTarget.textContent = "✓";
  setTimeout(() => { event.currentTarget.textContent = "⛓"; }, 1200);
});

document.querySelectorAll("[data-copy]").forEach((button) => {
  button.addEventListener("click", async () => {
    await navigator.clipboard.writeText(button.dataset.copy);
    const label = button.textContent;
    button.textContent = "Copiado";
    setTimeout(() => { button.textContent = label; }, 1200);
  });
});

// Los diagramas llegan ya renderizados como SVG desde el generador: no hay
// que traer Mermaid de un CDN, asi que tambien se ven sin conexion y en la
// aplicacion Android. Si quedara algun bloque sin renderizar, se deja legible
// como codigo en vez de dejar un hueco.
document.querySelectorAll("pre > code.language-mermaid").forEach((code) => {
  code.parentElement.classList.add("mermaid-source");
});

// Salto entre clases con las flechas del teclado, salvo al escribir en un campo.
document.addEventListener("keydown", (event) => {
  if (event.defaultPrevented || event.metaKey || event.ctrlKey || event.altKey) return;
  const target = event.target;
  if (target instanceof HTMLElement && (target.isContentEditable || ["INPUT", "TEXTAREA", "SELECT"].includes(target.tagName))) return;
  const rel = event.key === "ArrowLeft" ? "prev" : event.key === "ArrowRight" ? "next" : null;
  if (!rel) return;
  const link = document.querySelector(`a.pager-link[rel="${rel}"]`) || document.querySelector(`a.nav-link[rel="${rel}"]`);
  if (link) window.location.href = link.getAttribute("href");
});
