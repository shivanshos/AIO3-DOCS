# Documentation source and publication

Verified against the connected Mintlify deployment on 2026-10-18.

- Site: https://docs.aio3.ai; deployment: `aio-3`.
- Git source: `shivanshos/AIO3-DOCS`, branch `main`.
- **Active content directory: `home/shivansh/AIO3/AIO3-DOCS`.** This is a repository-relative path, not a path on the build machine.
- Run preview and validation from that directory. Root `docs.json` is a separate, earlier library configuration and is not the deployed configuration.

```sh
python3 scripts/check-docs.py
cd home/shivansh/AIO3/AIO3-DOCS
mint validate
mint broken-links
mint dev
```

## Ownership and preserved work

Edit published pages in the active directory. The root library remains preserved for comparison and later reviewed migration; do not edit both copies independently. Seven missing routes and the empty homepage were restored from existing root content in the October 18 repair. Broader strategy, operations, curriculum and governance pages at the root remain publication candidates, not automatically published content.

`brand/` is the handbook; `brand-system/` contains overlapping implementation references with distinct text. Keep both URL families until an editorial merge and redirect plan is reviewed. AIO3-BRAND owns approved brand specifications and token values. Its original artwork archive is not present in GitHub. Do not substitute the root Mintlify starter artwork or Core placeholders for approved AIO3 artwork.

AIO3-Core retains its independent `mintlify/` foundation for reference; it is not this site's source. AIO3-APP is a separate application starter. Repository links do not establish data synchronization.

## Release and future consolidation

Review the PR preview before merging. Merging to `main` can deploy automatically. Check navigation, homepage, both themes and mobile layout after publication. Keep dashboard Git settings unchanged for this repair.

To consolidate at the repository root later: reconcile every differing page, bring across all active brand routes, exclude archived/starter pages, validate the complete site, then coordinate the Git-source directory change and deployment. Merely changing the dashboard path would lose the active brand handbook. Do not delete either tree before that migration is verified.

No canonical logo or favicon is configured pending verified originals. The site can use its configured text name in the meantime.
