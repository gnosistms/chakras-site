# Chakra root address

The public custom domain points directly to a DigitalOcean Spaces CDN. `/3d`
works, but `/` returns a bucket-level 403 because the CDN has no default index.

1. Preserve the current public Chakra files in a dedicated static-site source.
2. Serve the existing `/3d` document as the root index, preserving query parameters and hash.
3. Deploy on DigitalOcean's free static hosting; verify the default hostname.
4. Move only chakras.gnosis-tms.com to the verified app, preserving existing paths.
5. Verify TLS, root navigation, model assets, and all language article routes.

Rollback: restore the domain's previous CNAME to
`gnosiswebtools.sgp1.cdn.digitaloceanspaces.com.`. Keep all Spaces objects unchanged.

## Completed — 22 October 2026

- Public repository: https://github.com/gnosistms/chakras-site
- DigitalOcean app: dd59b203-dd86-4169-90f3-f33ab3f513c5 (static component only).
- Domain DNS points to gnosis-chakras-cdgqn.ondigitalocean.app.
- Custom domain is ACTIVE with a valid HTTPS certificate.
- Homepage and /3d return exactly the original 3D HTML with its existing base URL.
- Verified all 14 original file hashes on the deployed static site.
- Verified /, /3d, /where, /donde, /dau and both anatomy model/metadata routes
  on the real custom domain. HTTP redirects to HTTPS.
- Browser verified the homepage, male/female model rendering, and language query.
- Original Spaces objects and unrelated services were unchanged.
