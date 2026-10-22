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
