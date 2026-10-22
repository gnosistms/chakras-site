# Chakra Roots and Flowers

Static hosting for https://chakras.gnosis-tms.com. The root index serves the same 3D page as `/3d`, preserving language query
parameters and fragment identifiers without a redirect.

The original Spaces CDN serves objects but cannot serve a default index at `/`.
DigitalOcean App Platform serves this snapshot with a normal default document.
Existing model, report, and asset paths are preserved, including `/3d`, `/where`,
`/donde`, `/dau`, and everything under `/chakras/`.

`python3 scripts/sync-public.py` refreshes the snapshot from the existing public
Spaces files. No credentials are used or stored in this repository. `snapshot.json`
records the downloaded file hashes. Original attribution and licenses remain in
the pages. All storage objects remain unchanged.

Deploy the repository's `public/` directory as a DigitalOcean static site.
