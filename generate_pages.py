#!/usr/bin/env python3
"""Generate InnerBalancEmporium mock HTML pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BRAND = "InnerBalancEmporium"

PRODUCTS = [
    ("celestial-moon-coaster-set", "Celestial Moon Coaster Set", "$38.00", "Home Decor", "Bestseller", "ph-1",
     "Four hand-poured coasters with moon phases, gold leaf, and soft galaxy swirls."),
    ("amethyst-realm-pyramid", "Amethyst Realm Pyramid", "$48.00", "Keepsakes", "One of a Kind", "ph-2",
     "A luminous resin pyramid inspired by amethyst light and quiet evenings."),
    ("moonlit-trinket-dish", "Moonlit Trinket Dish", "$28.00", "Keepsakes", None, "ph-3",
     "Crescent catchall for rings, charms, and everyday magic."),
    ("lunar-keepsake-jar", "Lunar Keepsake Jar", "$52.00", "Keepsakes", "Gift Ready", "ph-4",
     "Moon-etched jar with crystal-kissed lid for treasures and tiny notes."),
    ("pressed-flower-moon-necklace", "Pressed Flower Moon Necklace", "$42.00", "Jewelry", "New", "ph-5",
     "Botanical pendant sealed in crystal-clear resin with a moon motif."),
    ("galaxy-vanity-tray", "Galaxy Vanity Tray", "$65.00", "Home Decor", "Bestseller", "ph-6",
     "Deep-space tray for perfume, candles, and ritual tools."),
    ("celestial-keychain", "Celestial Keychain", "$18.00", "Jewelry", None, "ph-1",
     "Pocket-sized charm with gold flecks and a tiny crescent."),
    ("blooming-heart-paperweight", "Blooming Heart Paperweight", "$36.00", "Home Decor", None, "ph-2",
     "Heart-shaped resin bloom for desks that need a softer glow."),
]

CATEGORIES = [
    ("home-decor", "Home Decor", "Coasters & Trays", "ph-1",
     "Surfaces that feel like little altars — coasters, trays, and glowing accents."),
    ("keepsakes", "Keepsakes", "Jars & Containers", "ph-2",
     "Jars, dishes, and vessels for the things you hold dear."),
    ("jewelry", "Jewelry, Keychains & Accessories", "Wearable Magic", "ph-3",
     "Pendants, keychains, and small wearable pieces with botanicals and moons."),
    ("tabletop-games", "Tabletop Games", "DnD Dice, Dominoes & More", "ph-4",
     "Playful resin sets for campaign nights and cozy game tables."),
]

JOURNAL = [
    ("testing-new-mold", "Testing a New Mold", "Apr 18, 2025",
     "A crystal tray mold arrived this week — first pour notes and edge cleanup tips."),
    ("new-color-story", "A New Color Story", "Apr 12, 2025",
     "Indigo, plum, and gold leaf experiments for the next celestial collection."),
    ("nothing-goes-to-waste", "Nothing Goes to Waste", "Apr 5, 2025",
     "Scrap pours become moon charms — small joys from leftover magic."),
]


def shell(title, page, depth, body, extra_head=""):
    prefix = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} | {BRAND}</title>
  <meta name="description" content="Handmade resin art by Eyvette — mock storefront preview." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Great+Vibes&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{prefix}css/styles.css" />
  {extra_head}
</head>
<body data-page="{page}">
  <div data-header></div>
  {body}
  <div data-footer></div>
  <script src="{prefix}js/main.js"></script>
</body>
</html>
"""


def product_cards(ids=None, prefix=""):
    items = PRODUCTS if ids is None else [p for p in PRODUCTS if p[0] in ids]
    cards = []
    for slug, name, price, _cat, tag, ph, _desc in items:
        tag_html = f'<span class="tag">{tag}</span>' if tag else ""
        cards.append(f"""
        <article class="product-card">
          <a class="media" href="{prefix}products/{slug}.html"><div class="ph {ph}"></div>{tag_html}
            <button class="icon-btn wish" type="button" data-mock-wish aria-label="Wishlist">♡</button>
          </a>
          <div class="body">
            <h3><a href="{prefix}products/{slug}.html">{name}</a></h3>
            <div class="price">{price}</div>
            <div class="stars">★★★★★ <span class="muted">(12)</span></div>
            <button class="btn btn-dark" type="button" data-mock-purchase>Add to Cart</button>
          </div>
        </article>""")
    return "\n".join(cards)


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("wrote", rel)


# --- Pages ---

home = shell(
    "Home",
    "home",
    0,
    f"""
  <section class="hero-split">
    <div class="hero-copy">
      <p class="eyebrow">Handmade art for a</p>
      <h1>More Balanced, Brighter World</h1>
      <p>Unique resin creations for everyday beauty, meaningful moments, and playful adventures.</p>
      <div><a class="btn btn-gold" href="shop.html">Shop Now →</a></div>
      <div class="hero-values"><span>Create</span><span>·</span><span>Balance</span><span>·</span><span>Belong</span></div>
    </div>
    <div class="hero-media">
      <span class="script script-note">Art A Kinder World ♡</span>
    </div>
  </section>

  <section class="section section-cream">
    <div class="container">
      <div class="ornament">✦ Shop by Category ✦</div>
      <h2 class="center">Unique creations for everyday life</h2>
      <div class="cat-grid" style="margin-top:2rem">
        {"".join(f'''
        <a class="cat-card" href="categories/{slug}.html">
          <div class="thumb"><div class="ph {ph}"></div></div>
          <h3>{name}</h3>
          <p>{sub}</p>
        </a>''' for slug, name, sub, ph, _ in CATEGORIES)}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <div>
          <p class="eyebrow">Featured</p>
          <h2>Best Sellers</h2>
        </div>
        <a class="btn btn-outline" href="shop.html">View All →</a>
      </div>
      <div class="product-grid">
        {product_cards(["celestial-moon-coaster-set","moonlit-trinket-dish","pressed-flower-moon-necklace","celestial-keychain"])}
      </div>
    </div>
  </section>

  <section class="section section-cream">
    <div class="container about-split">
      <div class="about-photo" role="img" aria-label="Studio workbench"></div>
      <div class="about-copy">
        <p class="eyebrow">From the Studio</p>
        <h2>Hi, I'm Eyvette.</h2>
        <p class="muted">I create resin art inspired by balance, beauty, and a little everyday magic — small objects meant to brighten the spaces we live in.</p>
        <a class="btn btn-gold" href="studio.html">Read More →</a>
        <span class="script">Small Joys, Brighter Days. ♡</span>
      </div>
    </div>
  </section>

  <div class="moon-strip">Small Batch ✦ Big Intention ✦ Always Handmade</div>
""",
)
write("index.html", home)

shop = shell(
    "Shop",
    "shop",
    0,
    f"""
  <section class="hero-dark">
    <div>
      <p class="eyebrow" style="color:var(--gold-light)">✦ Handcrafted with intention ✦</p>
      <h1>Welcome to the <span class="script" style="font-size:1.15em">Shop</span></h1>
      <p>Handmade resin art for a more balanced, beautiful life. Each piece is crafted with creativity, intention, and a little bit of magic.</p>
      <a class="btn btn-gold" href="#grid">Shop Now →</a>
      <div class="values-bar">
        <div class="value-item">🌿 Unique Pieces</div>
        <div class="value-item">☽ Positive Intentions</div>
        <div class="value-item">✦ Handcrafted with Care</div>
      </div>
    </div>
  </section>

  <section class="section" id="grid">
    <div class="container">
      <div class="breadcrumbs"><a href="index.html">Home</a> › Shop</div>
      <div class="shop-layout">
        <aside class="filters">
          <h4>Categories</h4>
          <ul>
            <li><a class="is-active" href="shop.html">All Products <span>8</span></a></li>
            <li><a href="categories/home-decor.html">Home Decor <span>3</span></a></li>
            <li><a href="categories/keepsakes.html">Keepsakes <span>3</span></a></li>
            <li><a href="categories/jewelry.html">Jewelry <span>2</span></a></li>
            <li><a href="categories/tabletop-games.html">Tabletop Games <span>—</span></a></li>
          </ul>
          <h4>Price</h4>
          <ul>
            <li><label><span>Under $25</span><input type="checkbox" /></label></li>
            <li><label><span>$25–$50</span><input type="checkbox" checked /></label></li>
            <li><label><span>$50–$100</span><input type="checkbox" /></label></li>
            <li><label><span>Over $100</span><input type="checkbox" /></label></li>
          </ul>
          <h4>Availability</h4>
          <ul>
            <li><label><span>In Stock</span><input type="checkbox" checked /></label></li>
            <li><label><span>Made to Order</span><input type="checkbox" /></label></li>
          </ul>
          <div class="filter-promo">
            <strong>More Than Decor</strong>
            <span class="script">A little more light for your journey ♡</span>
          </div>
        </aside>
        <div>
          <div class="shop-toolbar">
            <span>Showing 1–8 of 8 products</span>
            <label>Sort by
              <select>
                <option>Featured</option>
                <option>Price: Low to High</option>
                <option>Newest</option>
              </select>
            </label>
          </div>
          <div class="product-grid">{product_cards()}</div>
          <div class="pagination">
            <span class="current">1</span>
            <a href="shop.html">2</a>
            <a href="shop.html">→</a>
          </div>
        </div>
      </div>
    </div>
  </section>
""",
)
write("shop.html", shop)

studio = shell(
    "The Studio",
    "studio",
    0,
    f"""
  <section class="hero-dark">
    <div>
      <h1>The Studio</h1>
      <p>A closer look at the maker, the process, and the little moments behind each creation.</p>
      <p class="eyebrow" style="color:var(--gold-light)">Resin + Nature + Intention + A Brighter You</p>
    </div>
  </section>

  <section class="section section-cream">
    <div class="container portrait-row">
      <div class="portrait" aria-hidden="true">E</div>
      <div>
        <p class="eyebrow">About Eyvette</p>
        <h2>Artist + Dreamer + Nature Lover</h2>
        <p class="muted">I'm the hands and heart behind {BRAND}. My resin pieces are inspired by nature, the moon, and the feeling of finding calm in small beautiful things.</p>
      </div>
      <div class="center">
        <p class="eyebrow">Beauty can be a form of healing</p>
        <p class="script" style="font-size:1.8rem;color:var(--plum)">Eyvette ♡</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2>From the Workbench</h2>
        <span class="eyebrow">Real creations. Brighter days.</span>
      </div>
      <div class="workbench">
        <article class="wb-card"><div class="media"><div class="ph ph-1"></div><span class="status">In the Works</span></div><div class="body"><h3>Moon Phase Coasters</h3></div></article>
        <article class="wb-card"><div class="media"><div class="ph ph-2"></div><span class="status">Curing</span></div><div class="body"><h3>Celestial Moon Tray</h3></div></article>
        <article class="wb-card"><div class="media"><div class="ph ph-3"></div><span class="status">Experiment</span></div><div class="body"><h3>Galaxy Color Tests</h3></div></article>
        <article class="wb-card"><div class="media"><div class="ph ph-4"></div><span class="status">Coming Soon</span></div><div class="body"><h3>Botanical Pendants</h3></div></article>
        <article class="wb-card"><div class="media"><div class="ph ph-5"></div><span class="status">One of a Kind</span></div><div class="body"><h3>Flower Catchall</h3></div></article>
      </div>
    </div>
  </section>

  <section class="section section-cream">
    <div class="container">
      <div class="section-head">
        <h2>Studio Journal</h2>
        <a href="journal/index.html">View All →</a>
      </div>
      <div class="card-row">
        <article class="journal-card">
          <a class="media" href="journal/testing-new-mold.html"><div class="ph ph-2"></div></a>
          <div class="body">
            <p class="eyebrow">Apr 18, 2025</p>
            <h3><a href="journal/testing-new-mold.html">Testing a New Mold</a></h3>
            <p class="muted">First pour notes and edge cleanup tips.</p>
            <a href="journal/testing-new-mold.html">Read More →</a>
          </div>
        </article>
        <article class="journal-card">
          <a class="media" href="journal/new-color-story.html"><div class="ph ph-4"></div></a>
          <div class="body">
            <p class="eyebrow">Apr 12, 2025</p>
            <h3><a href="journal/new-color-story.html">A New Color Story</a></h3>
            <p class="muted">Indigo, plum, and gold leaf experiments.</p>
            <a href="journal/new-color-story.html">Read More →</a>
          </div>
        </article>
        <article class="journal-card">
          <a class="media" href="journal/nothing-goes-to-waste.html"><div class="ph ph-6"></div></a>
          <div class="body">
            <p class="eyebrow">Apr 5, 2025</p>
            <h3><a href="journal/nothing-goes-to-waste.html">Nothing Goes to Waste</a></h3>
            <p class="muted">Scrap pours become moon charms.</p>
            <a href="journal/nothing-goes-to-waste.html">Read More →</a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head">
        <h2>Behind the Pour</h2>
        <a href="studio.html">Watch All →</a>
      </div>
      <div class="video-row">
        <a class="video-thumb" href="studio.html"><span class="play">▶</span><span class="time">0:42</span><span style="position:absolute;bottom:2.2rem;left:0.6rem;font-size:0.75rem">Mixing Pigment</span></a>
        <a class="video-thumb" href="studio.html"><span class="play">▶</span><span class="time">0:58</span><span style="position:absolute;bottom:2.2rem;left:0.6rem;font-size:0.75rem">Pouring the Resin</span></a>
        <a class="video-thumb" href="studio.html"><span class="play">▶</span><span class="time">0:47</span><span style="position:absolute;bottom:2.2rem;left:0.6rem;font-size:0.75rem">Placing the Florals</span></a>
        <a class="video-thumb" href="studio.html"><span class="play">▶</span><span class="time">0:36</span><span style="position:absolute;bottom:2.2rem;left:0.6rem;font-size:0.75rem">Finishing Touches</span></a>
        <a class="video-thumb" href="studio.html"><span class="play">▶</span><span class="time">0:51</span><span style="position:absolute;bottom:2.2rem;left:0.6rem;font-size:0.75rem">Demolding</span></a>
      </div>
    </div>
  </section>
""",
)
write("studio.html", studio)

CAT_PRODUCTS = {
    "home-decor": ["celestial-moon-coaster-set", "galaxy-vanity-tray", "blooming-heart-paperweight"],
    "keepsakes": ["amethyst-realm-pyramid", "moonlit-trinket-dish", "lunar-keepsake-jar"],
    "jewelry": ["pressed-flower-moon-necklace", "celestial-keychain"],
}

for slug, name, sub, ph, blurb in CATEGORIES:
    if slug == "tabletop-games":
        grid = """
        <div class="empty-state" style="grid-column:1/-1">
          <h2>Tabletop Games — Coming Soon</h2>
          <p class="muted">Dice, dominoes, and playful sets are on the workbench. Browse other categories meanwhile.</p>
          <a class="btn btn-gold" href="../shop.html">Back to Shop</a>
        </div>"""
    else:
        grid = product_cards(CAT_PRODUCTS[slug], prefix="../")
    body = f"""
  <div class="page-title-bar">
    <div class="container">
      <p class="eyebrow">Shop by Category</p>
      <h1>{name}</h1>
      <p class="muted" style="color:rgba(249,245,240,0.75)">{blurb}</p>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="breadcrumbs"><a href="../index.html">Home</a> › <a href="../shop.html">Shop</a> › {name}</div>
      <div class="product-grid">
        {grid}
      </div>
    </div>
  </section>
"""
    write(f"categories/{slug}.html", shell(name, "shop", 1, body))

for slug, name, price, cat, tag, ph, desc in PRODUCTS:
    cat_slug = {
        "Home Decor": "home-decor",
        "Keepsakes": "keepsakes",
        "Jewelry": "jewelry",
    }[cat]
    tag_html = f'<p class="eyebrow">{tag}</p>' if tag else ""
    body = f"""
  <section class="section">
    <div class="container">
      <div class="breadcrumbs"><a href="../index.html">Home</a> › <a href="../shop.html">Shop</a> › <a href="../categories/{cat_slug}.html">{cat}</a> › {name}</div>
      <div class="pdp">
        <div class="pdp-gallery"><div class="ph {ph}"></div></div>
        <div class="pdp-info">
          {tag_html}
          <h1>{name}</h1>
          <div class="price">{price}</div>
          <div class="stars">★★★★★ <span class="muted">12 reviews</span></div>
          <p class="muted">{desc}</p>
          <p class="muted">Each piece is handmade in small batches. Colors and gold flecks may vary — that's part of the magic.</p>
          <div class="pdp-actions">
            <button class="btn btn-gold" type="button" data-mock-purchase>Add to Cart</button>
            <button class="btn btn-outline" type="button" data-mock-wish>♡ Wishlist</button>
          </div>
          <p class="script" style="color:var(--plum);font-size:1.4rem">Small creations, bigger light.</p>
          <a href="../shipping.html">Shipping & returns →</a>
        </div>
      </div>
    </div>
  </section>
"""
    write(f"products/{slug}.html", shell(name, "shop", 1, body))

faq = shell(
    "FAQ",
    "faq",
    0,
    """
  <div class="page-title-bar"><div class="container"><h1>FAQ</h1><p>Answers for collectors, gifters, and the curious.</p></div></div>
  <section class="section"><div class="container faq" style="max-width:760px">
    <details open><summary>Is this a real checkout?</summary><p class="muted">No — this is a mock storefront for layout and brand exploration. Purchase buttons do not process payments.</p></details>
    <details><summary>Are the pieces handmade?</summary><p class="muted">Yes. Eyvette pours each resin piece in small batches with botanicals, pigments, and gold leaf.</p></details>
    <details><summary>Do colors match photos exactly?</summary><p class="muted">Natural variation is expected. No two pours are identical.</p></details>
    <details><summary>Can I request a custom piece?</summary><p class="muted">Use the Contact page — custom requests are welcome for future live commerce.</p></details>
    <details><summary>What about shipping?</summary><p class="muted">See the Shipping page for the planned policy outline.</p></details>
  </div></section>
""",
)
write("faq.html", faq)

contact = shell(
    "Contact",
    "contact",
    0,
    """
  <div class="page-title-bar"><div class="container"><h1>Contact</h1><p>Say hello — studio notes, custom ideas, and collaborations.</p></div></div>
  <section class="section"><div class="container">
    <form class="form-stack" data-mock-form>
      <input class="input" name="name" placeholder="Your name" required />
      <input class="input" type="email" name="email" placeholder="Email" required />
      <input class="input" name="subject" placeholder="Subject" />
      <textarea class="input" name="message" placeholder="Your message" required></textarea>
      <button class="btn btn-gold" type="submit">Send Message →</button>
    </form>
  </div></section>
""",
)
write("contact.html", contact)

cart = shell(
    "Cart",
    "cart",
    0,
    """
  <div class="page-title-bar"><div class="container"><h1>Your Cart</h1></div></div>
  <section class="section"><div class="container">
    <div class="empty-state">
      <h2>Cart is empty (mock)</h2>
      <p class="muted">Add to Cart buttons are disabled on this preview. Explore products freely — checkout is not wired.</p>
      <a class="btn btn-gold" href="shop.html">Continue Shopping</a>
      <p style="margin-top:1rem"><button class="btn btn-outline is-disabled" type="button" data-mock-purchase>Checkout →</button></p>
    </div>
  </div></section>
""",
)
write("cart.html", cart)

wishlist = shell(
    "Wishlist",
    "wishlist",
    0,
    """
  <div class="page-title-bar"><div class="container"><h1>Wishlist</h1></div></div>
  <section class="section"><div class="container">
    <div class="empty-state">
      <h2>Saved pieces live here later</h2>
      <p class="muted">Wishlist hearts are mock actions for this layout pass.</p>
      <a class="btn btn-gold" href="shop.html">Browse the Shop</a>
    </div>
  </div></section>
""",
)
write("wishlist.html", wishlist)

search = shell(
    "Search",
    "search",
    0,
    """
  <div class="page-title-bar"><div class="container"><h1>Search</h1><p>Find a little magic.</p></div></div>
  <section class="section"><div class="container" style="max-width:640px">
    <form class="form-row" data-mock-search>
      <input class="input" name="q" placeholder="Search magical creations..." />
      <button class="btn btn-gold" type="submit">Search</button>
    </form>
    <p class="muted" style="margin-top:1.25rem">Try categories:
      <a href="categories/home-decor.html">Home Decor</a> ·
      <a href="categories/keepsakes.html">Keepsakes</a> ·
      <a href="categories/jewelry.html">Jewelry</a>
    </p>
  </div></section>
""",
)
write("search.html", search)

shipping = shell(
    "Shipping",
    "shipping",
    0,
    """
  <div class="page-title-bar"><div class="container"><h1>Shipping</h1></div></div>
  <section class="section"><div class="container" style="max-width:720px">
    <h2>Planned policy (mock)</h2>
    <p class="muted">Orders ship in protective packaging suited to resin art. Processing times and rates will be confirmed when commerce goes live.</p>
    <ul class="muted">
      <li>Careful packing for trays, jars, and jewelry</li>
      <li>Tracking provided on live orders</li>
      <li>Returns window outlined at launch</li>
    </ul>
    <a class="btn btn-outline" href="faq.html">Back to FAQ</a>
  </div></section>
""",
)
write("shipping.html", shipping)

privacy = shell(
    "Privacy",
    "privacy",
    0,
    """
  <div class="page-title-bar"><div class="container"><h1>Privacy</h1></div></div>
  <section class="section"><div class="container" style="max-width:720px">
    <p class="muted">This mock site does not collect personal data. Forms and newsletter fields are local-only demos and do not submit to a server.</p>
    <a class="btn btn-outline" href="index.html">Return Home</a>
  </div></section>
""",
)
write("privacy.html", privacy)

journal_index = shell(
    "Studio Journal",
    "studio",
    1,
    """
  <div class="page-title-bar"><div class="container"><h1>Studio Journal</h1><p>Notes from the pour table.</p></div></div>
  <section class="section"><div class="container card-row">
    <article class="journal-card"><a class="media" href="testing-new-mold.html"><div class="ph ph-2"></div></a><div class="body"><p class="eyebrow">Apr 18, 2025</p><h3><a href="testing-new-mold.html">Testing a New Mold</a></h3><a href="testing-new-mold.html">Read More →</a></div></article>
    <article class="journal-card"><a class="media" href="new-color-story.html"><div class="ph ph-4"></div></a><div class="body"><p class="eyebrow">Apr 12, 2025</p><h3><a href="new-color-story.html">A New Color Story</a></h3><a href="new-color-story.html">Read More →</a></div></article>
    <article class="journal-card"><a class="media" href="nothing-goes-to-waste.html"><div class="ph ph-6"></div></a><div class="body"><p class="eyebrow">Apr 5, 2025</p><h3><a href="nothing-goes-to-waste.html">Nothing Goes to Waste</a></h3><a href="nothing-goes-to-waste.html">Read More →</a></div></article>
  </div></section>
""",
)
write("journal/index.html", journal_index)

for slug, title, date, blurb in JOURNAL:
    body = f"""
  <div class="page-title-bar"><div class="container"><p class="eyebrow">{date}</p><h1>{title}</h1></div></div>
  <section class="section"><div class="container" style="max-width:720px">
    <div class="about-photo" style="min-height:280px;margin-bottom:1.5rem;background:linear-gradient(180deg,transparent,rgba(26,15,31,.25)), radial-gradient(circle at 40% 30%, rgba(197,160,89,.35), transparent 40%), linear-gradient(145deg,#4a2f55,#1a0f1f);"></div>
    <p class="muted">{blurb}</p>
    <p class="muted">This journal entry is placeholder copy for the mock layout — ready to swap with Eyvette's real studio notes later.</p>
    <p class="script" style="font-size:1.6rem;color:var(--plum)">More art, a kinder world ♡</p>
    <a class="btn btn-outline" href="index.html">All Journal Posts</a>
  </div></section>
"""
    write(f"journal/{slug}.html", shell(title, "studio", 1, body))

# sitemap helper page
sitemap_links = [
    "index.html", "shop.html", "studio.html", "faq.html", "contact.html",
    "cart.html", "wishlist.html", "search.html", "shipping.html", "privacy.html",
    "journal/index.html",
] + [f"journal/{s}.html" for s, *_ in JOURNAL] + [f"categories/{s}.html" for s, *_ in CATEGORIES] + [
    f"products/{s}.html" for s, *_ in PRODUCTS
]
sitemap_body = """
  <div class="page-title-bar"><div class="container"><h1>Site Map</h1><p>All mock pages for click-through review.</p></div></div>
  <section class="section"><div class="container"><ul>""" + "".join(
    f'<li><a href="{href}">{href}</a></li>' for href in sitemap_links
) + "</ul></div></section>"
write("sitemap.html", shell("Sitemap", "home", 0, sitemap_body))

readme = f"""# {BRAND} (Mock Site)

Public **proof of concept** storefront for **{BRAND} by Eyvette** — handmade resin art layout preview.

> Work in progress. Navigation and pages are clickable. **Purchases are disabled** (mock only).

## Live preview

**https://inner-balance-emporium.pages.dev**

Forward that link for client mock viewing (purchases disabled).

## Local preview

```bash
cd inner-balance-emporium
python -m http.server 5173
```

Open http://127.0.0.1:5173/

## Deploy (Cloudflare Pages)

```bash
npx wrangler pages deploy . --project-name=inner-balance-emporium --branch=main
```

## Notes

- Full navigation and product links work.
- **Add to Cart / Checkout / Subscribe / Contact** are mocked (toast only).
- Product imagery uses CSS placeholders until real photos are added.
- Regenerate pages: `python generate_pages.py`
- See `sitemap.html` for the full clickable page list.
"""
write("README.md", readme)
print("done", len(sitemap_links), "linked pages + sitemap")
