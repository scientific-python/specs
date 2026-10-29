// Style chart versions whose drop date has passed as critical.
// Runs before Mermaid renders, so the chart source is still available.
const taskLine = /^.+ : ([^,]+),\d{4}-\d\d-\d\d,(\d{4}-\d\d-\d\d)$/gm;
const now = new Date();

for (const pre of document.querySelectorAll("pre.mermaid")) {
  const past = [...pre.textContent.matchAll(taskLine)]
    .filter(([, , dropDate]) => new Date(`${dropDate}T00:00`) <= now)
    .map(([, id]) => id);
  if (!past.length) continue;

  new MutationObserver((_, observer) => {
    const svg = pre.querySelector(":scope > svg");
    if (!svg) return;
    observer.disconnect();
    for (const id of past) {
      const rect = svg.getElementById(`${svg.id}-${id}`);
      const section = [...(rect?.classList ?? [])].find((c) =>
        /^task\d+$/.test(c),
      );
      if (!section) continue;
      const n = section.slice("task".length);
      rect.classList.replace(section, `crit${n}`);
      rect.classList.remove("task");
      const text = svg.getElementById(`${rect.id}-text`);
      if (text?.classList.contains(`taskText${n}`)) {
        text.classList.add(`critText${n}`);
      }
    }
  }).observe(pre, { childList: true });
}
