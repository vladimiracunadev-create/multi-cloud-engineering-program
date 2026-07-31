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
  const container = document.createElement("pre");
  container.className = "mermaid";
  container.textContent = code.textContent;
  code.parentElement.replaceWith(container);
});

if (document.querySelector(".mermaid")) {
  import("https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs").then(({ default: mermaid }) => {
    mermaid.initialize({ startOnLoad: true, theme: root.dataset.theme === "dark" ? "dark" : "neutral", securityLevel: "strict" });
  }).catch(() => {});
}
