# InnerBalancEmporium (Mock Site)

Public **proof of concept** storefront for **InnerBalancEmporium by Eyvette** — handmade resin art layout preview.

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
- Product imagery from `assets/images/` (mock crops + optional Google Flow).
- Regenerate pages: `python generate_pages.py`
- See `sitemap.html` for the full clickable page list.

## Custom images

```powershell
python scripts/prepare_mock_crops.py   # from Eyvette mock PNGs
python generate_pages.py
.\scripts\run-ibe-flow.ps1 -LiveFlow -Max 3 -Priority banner  # Google Flow stills
```

Queue: `flow/image-queue.json` (19 slots).
