# AIO3 Documentation

Documentation frontend for AIO3, powered by [Mintlify](https://mintlify.com) and maintained separately from [AIO3-Core](https://github.com/shivanshos/AIO3-Core).

## Scope

This public documentation covers the AIO3 mission and principles, learner onboarding, draft learning paths, curriculum framework, technical lab safety, mentorship approach, and research methodology. AIO3 is in discovery and validation; published pages are not course enrollment promises.

## Preview locally

Prerequisites: Node.js and npm.

```bash
npm install -g mint
mint dev
```

Run the commands from the repository root containing `docs.json`. Open the address printed by the CLI (commonly `http://localhost:3000`).

## Publish via Mintlify

1. Create or open a project in [Mintlify](https://dashboard.mintlify.com).
2. Connect GitHub and authorize access to the `shivanshos/AIO3-DOCS` repository.
3. Select the `main` branch and repository root as documentation source.
4. Preview the generated site, validate links and styling, then enable production publishing.
5. Optionally configure a custom domain, such as `docs.aio3.in`, after confirming ownership and DNS settings.

Mintlify hosting and DNS cannot be completed solely through repository commits.

## Contribution workflow

Propose changes through branches and pull requests. Update `docs.json` when adding pages. Do not publish student data, secrets, or unverified marketing claims. See [Contributing](contributing.mdx).
