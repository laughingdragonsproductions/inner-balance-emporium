/* Shared layout + mock commerce behavior */
(function () {
  const path = window.location.pathname.replace(/\\/g, "/");
  const depth = (path.match(/\//g) || []).length - (path.endsWith("/") ? 1 : 0);
  // Approximate root-relative prefix from nested folders
  const parts = path.split("/").filter(Boolean);
  const file = parts[parts.length - 1] || "index.html";
  const nested = parts.length > 1 ? "../".repeat(parts.length - 1) : "";
  const root = nested || "./";

  const page = document.body.dataset.page || "home";

  function isActive(key) {
    return page === key ? ' aria-current="page"' : "";
  }

  const wipBanner = `
  <div class="wip-banner" role="status">
    <strong>Proof of concept</strong> — layout preview only. Purchases are disabled. Work in progress.
  </div>`;

  const header = `
  <header class="site-header">
    <div class="container header-inner">
      <a class="brand" href="${root}index.html">
        <div class="brand-mark" aria-hidden="true">☽</div>
        <div class="brand-text">
          <strong>InnerBalancEmporium</strong>
          <span>by Eyvette</span>
        </div>
      </a>
      <button class="icon-btn menu-toggle" type="button" aria-label="Open menu" data-menu-toggle>☰</button>
      <nav class="nav" data-nav>
        <a href="${root}index.html"${isActive("home")}>Home</a>
        <a href="${root}shop.html"${isActive("shop")}>Shop</a>
        <a href="${root}studio.html"${isActive("studio")}>Studio</a>
        <a href="${root}faq.html"${isActive("faq")}>FAQ</a>
        <a href="${root}contact.html"${isActive("contact")}>Contact</a>
      </nav>
      <div class="header-actions">
        <a class="icon-btn" href="${root}search.html" aria-label="Search">⌕</a>
        <a class="icon-btn" href="${root}wishlist.html" aria-label="Wishlist">♡</a>
        <a class="icon-btn" href="${root}cart.html" aria-label="Cart">
          👜<span class="badge">0</span>
        </a>
      </div>
    </div>
  </header>`;

  const footer = `
  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <div class="brand" style="margin-bottom:0.85rem">
          <div class="brand-mark" aria-hidden="true">☽</div>
          <div class="brand-text">
            <strong>InnerBalancEmporium</strong>
            <span>by Eyvette</span>
          </div>
        </div>
        <p class="muted" style="color:rgba(249,245,240,0.65);max-width:28ch">
          Handmade resin art for everyday beauty, meaningful moments, and a kinder world.
        </p>
      </div>
      <div>
        <h4>Stay in Touch</h4>
        <p style="margin:0 0 0.85rem;color:rgba(249,245,240,0.7);font-size:0.9rem">
          Get studio updates, new creations, and a little inspiration.
        </p>
        <form class="form-row" data-mock-subscribe>
          <input class="input" type="email" placeholder="Your email address" required />
          <button class="btn btn-gold" type="submit">Subscribe →</button>
        </form>
      </div>
      <div>
        <h4>Explore</h4>
        <div class="footer-links">
          <a href="${root}index.html">Home</a>
          <a href="${root}shop.html">Shop</a>
          <a href="${root}studio.html">Studio</a>
          <a href="${root}journal/index.html">Studio Journal</a>
          <a href="${root}faq.html">FAQ</a>
          <a href="${root}contact.html">Contact</a>
          <a href="${root}shipping.html">Shipping</a>
          <a href="${root}privacy.html">Privacy</a>
        </div>
        <p class="script" style="margin-top:1rem;font-size:1.35rem">Handmade with Intention ♡</p>
      </div>
    </div>
    <div class="container footer-bottom">
      <span>© 2026 InnerBalancEmporium by Eyvette. All rights reserved.</span>
      <span>CREATE · BALANCE · BELONG · Mock storefront</span>
    </div>
  </footer>
  <div class="toast" data-toast role="status" aria-live="polite"></div>`;

  const headerMount = document.querySelector("[data-header]");
  const footerMount = document.querySelector("[data-footer]");
  if (headerMount) headerMount.outerHTML = wipBanner + header;
  if (footerMount) footerMount.outerHTML = footer;

  document.querySelector("[data-menu-toggle]")?.addEventListener("click", () => {
    document.querySelector("[data-nav]")?.classList.toggle("open");
  });

  function toast(message) {
    const el = document.querySelector("[data-toast]");
    if (!el) return;
    el.textContent = message;
    el.classList.add("show");
    clearTimeout(toast._t);
    toast._t = setTimeout(() => el.classList.remove("show"), 2800);
  }

  document.addEventListener("click", (e) => {
    const purchase = e.target.closest("[data-mock-purchase]");
    if (purchase) {
      e.preventDefault();
      toast("Mock site — purchases are disabled. Explore the pages freely.");
      return;
    }
    const wish = e.target.closest("[data-mock-wish]");
    if (wish) {
      e.preventDefault();
      toast("Wishlist is a mock action for this preview.");
    }
  });

  document.querySelectorAll("[data-mock-subscribe]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      toast("Thanks — newsletter signup is mocked for this preview.");
      form.reset();
    });
  });

  document.querySelectorAll("[data-mock-form]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      toast("Message captured locally only — contact form is mocked.");
      form.reset();
    });
  });

  document.querySelectorAll("[data-mock-search]").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const q = new FormData(form).get("q") || "";
      toast(`Search mock: “${q}” — try the Shop categories instead.`);
    });
  });
})();
