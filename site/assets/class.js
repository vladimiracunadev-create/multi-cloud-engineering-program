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

document.querySelectorAll("pre > code.language-mermaid").forEach((code) => {
  const container = document.createElement("div");
  container.className = "mermaid";
  container.setAttribute("role", "img");
  container.setAttribute("aria-label", "Diagrama del contenido de la clase");
  container.textContent = code.textContent;
  code.parentElement.replaceWith(container);
});

if (document.querySelector(".mermaid")) {
  import("https://cdn.jsdelivr.net/npm/mermaid@11.15.0/dist/mermaid.esm.min.mjs").then(async ({ default: mermaid }) => {
    mermaid.initialize({ startOnLoad: false, theme: root.dataset.theme === "dark" ? "dark" : "neutral", securityLevel: "strict" });
    await mermaid.run({ nodes: document.querySelectorAll(".mermaid") });
  }).catch((error) => {
    document.querySelectorAll(".mermaid").forEach((diagram) => {
      diagram.classList.add("mermaid-error");
      diagram.setAttribute("role", "alert");
    });
    console.error("No se pudo renderizar Mermaid", error);
  });
}

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
