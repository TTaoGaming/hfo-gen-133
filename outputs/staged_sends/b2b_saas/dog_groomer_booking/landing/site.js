(async function () {
  const script = document.currentScript;
  const configPath = script?.dataset?.config || "./site.json";
  const response = await fetch(configPath, { cache: "no-store" });
  if (!response.ok) throw new Error(`Site configuration unavailable: ${response.status}`);
  const site = await response.json();
  document.documentElement.style.setProperty("--accent", site.accent);
  document.documentElement.style.setProperty("--accent-dark", site.accent_dark);
  document.title = site.title;
  const description = document.querySelector('meta[name="description"]');
  if (description) description.content = site.description;
  const setText = (id, value) => { const node = document.getElementById(id); if (node) node.textContent = value; };
  setText("eyebrow", site.eyebrow);
  setText("headline", site.headline);
  setText("subheadline", site.subheadline);
  setText("buyer-signal", site.buyer_signal);
  setText("outcome", site.outcome);
  setText("before-copy", site.before);
  setText("after-copy", site.after);
  setText("provenance", `Starter adapter: ${site.base_repo_label} · ${site.license_label}`);

  const workflow = document.getElementById("workflow");
  site.steps.forEach((step) => {
    const item = document.createElement("li");
    const title = document.createElement("h3");
    const copy = document.createElement("p");
    title.textContent = step.name;
    copy.textContent = step.detail;
    item.append(title, copy);
    workflow.appendChild(item);
  });

  const benefits = document.getElementById("benefits");
  site.benefits.forEach((benefit, index) => {
    const card = document.createElement("article");
    const number = document.createElement("span");
    const title = document.createElement("h3");
    const copy = document.createElement("p");
    number.textContent = String(index + 1).padStart(2, "0");
    title.textContent = benefit.title;
    copy.textContent = benefit.detail;
    card.append(number, title, copy);
    benefits.appendChild(card);
  });

  const faq = document.getElementById("faq-list");
  site.faq.forEach((entry) => {
    const details = document.createElement("details");
    const summary = document.createElement("summary");
    const copy = document.createElement("p");
    summary.textContent = entry.question;
    copy.textContent = entry.answer;
    details.append(summary, copy);
    faq.appendChild(details);
  });

  if (site.cal_link && !site.cal_link.startsWith("REPLACE_")) {
    (function (C, A, L) {
      const push = (api, args) => api.q.push(args);
      const doc = C.document;
      C.Cal = C.Cal || function () {
        const cal = C.Cal;
        const args = arguments;
        if (!cal.loaded) {
          cal.ns = {};
          cal.q = cal.q || [];
          const tag = doc.createElement("script");
          tag.src = A;
          doc.head.appendChild(tag);
          cal.loaded = true;
        }
        if (args[0] === L) {
          const api = function () { push(api, arguments); };
          const namespace = args[1];
          api.q = api.q || [];
          cal.ns[namespace] = cal.ns[namespace] || api;
          push(cal.ns[namespace], args);
          push(cal, ["initNamespace", namespace]);
          return;
        }
        push(cal, args);
      };
    })(window, "https://app.cal.com/embed/embed.js", "init");
    window.Cal("init", "demo", { origin: "https://cal.com" });
    document.getElementById("cal-inline").replaceChildren();
    window.Cal.ns.demo("inline", { elementOrSelector: "#cal-inline", calLink: site.cal_link, config: { layout: "month_view" } });
  }
})().catch((error) => {
  const main = document.getElementById("main");
  if (main) main.setAttribute("data-config-error", error.message);
});
