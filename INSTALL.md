# Add this package to your GitHub profile

Repository: `hardikdhingra150/hardikdhingra150`.

## 1. Upload the README and graphics

Extract the ZIP. Upload the CONTENTS of github-profile-ready to your repository root. Do not upload the ZIP itself or nest the whole folder inside your repository.

Replace the existing README.md and the supplied assets as needed, after keeping a copy of your previous version. These three exact image files must be committed with the README:

```
README.md
assets/
  grid-header.svg
  race-strategy.svg
  footer.svg
docs/
  index.html
  .nojekyll
.github/
  workflows/
    pages.yml
INSTALL.md
```

The README now uses bundled artwork and does not load the previous banner or your portfolio's racing image. No portfolio links are included. Profile information is immediately visible.

## 2. Enable the playable game

The game runs separately on GitHub Pages. The README can link to it; GitHub cannot execute a game inside README Markdown.

1. Open your repository's Settings → Pages.
2. Under Build and deployment, set Source to GitHub Actions.
3. Commit the package to main. If your default branch is different, replace main in pages.yml with that branch name.
4. Check that `.github/workflows/pages.yml` exists. Hidden folders may be skipped by a browser file picker. If it is absent, use Add file → Create new file, enter `.github/workflows/pages.yml`, and paste the provided pages.yml content.
5. Open Actions → Publish REDLINE racing game → Run workflow. Wait for a successful deployment.
6. Open the URL shown by the deployment. With this repository and no custom domain, it should be:
   https://hardikdhingra150.github.io/hardikdhingra150/

The README's Play link becomes live after this deployment. The package is prepared for upload; it has not been deployed by this chat. If this repository already uses Pages, this workflow will replace the content served by that repository's Pages site. Review that setting before deploying. It does not configure a custom domain.

If the deployment reports a different URL because the repository already has a custom domain, replace BOTH game links in README.md with the actual deployment URL.

## 3. What is included

- Original red-and-charcoal motorsport cover, development circuit, and checkered footer.
- Featured project links, engineering stack, and live contribution streak.
- Separate self-contained racing game with mouse/touch drag, arrow controls, pause, increasing pace, and a local personal best.
- GitHub Pages workflow that publishes only docs/, keeping the game separate from the profile README.

The game requires no install, API keys, libraries, or external resources. Best scores stay in each browser. All profile text is visible without expanding panels.

## Validation and limits

All README image paths and SVG XML were checked against this package. The game passed JavaScript syntax and mocked runtime checks for start, scoring, input, pause, resume, and automatic pause. Its real browser rendering remains unverified because the in-app browser blocked local-file previews.

Existing public project links and the live streak service returned HTTP 200 during the October 6 checks. The streak is an external service and may occasionally be unavailable; the contribution-calendar link is the fallback. The NEW game URL has not been deployed or verified live.

This workflow follows GitHub's current Pages documentation:
https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
