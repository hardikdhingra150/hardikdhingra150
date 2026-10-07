# Redesigned F1 profile + GitHub-only race

Upload the CONTENTS of this package to the root of `hardikdhingra150/hardikdhingra150` on its default branch. Keep a copy of existing files before replacing them. The folder layout must stay intact:

```
README.md
assets/                 (10 SVG files)
game/state.json
scripts/race.py
.github/workflows/grid-run.yml
INSTALL.md
```

No GitHub Pages, external game website, or portfolio link is used. The old docs/ game and pages.yml workflow are not part of this package. If you no longer want the earlier Pages deployment, remove its old pages.yml workflow separately.

## Enable the game

1. Ensure Issues is enabled under repository Settings → General → Features.
2. Ensure Actions is enabled. The race workflow requests contents: write and issues: write so the bot can update the three race files and comment on/close move issues. Repository or organization restrictions may prevent those requested permissions; if so, review the Actions policy for this workflow.
3. Put `.github/workflows/grid-run.yml` on the default branch. Hidden folders may be missed during drag-and-drop uploads. If needed, use Add file → Create new file and enter that exact path, then paste the included workflow.
4. The package assumes the default branch is main. If yours differs, change ref: main in the workflow to its actual name.
5. Branch rules must permit the workflow bot's direct updates to README.md, assets/race-board.svg, and game/state.json. If your rules require pull requests, this workflow cannot update the board automatically under those rules; do not claim it is active until that is resolved.
6. On the profile, choose CENTRE for the initial board and submit the prefilled issue. Check Actions → GitHub Grid Run. When complete, refresh the README to see score 1 and the next board. GitHub's image cache may add a delay.

The move links will open GitHub issues after the files are committed. They are not intended to submit silently. Players sign in and submit a public issue, which the bot comments on and closes.

## Game behavior

This is a shared, turn-based race. One lane is clear and two are blocked. A clear move increases the shared score; a blocked move ends the run. Restart is available after a collision. Best score persists in game/state.json.

Every move carries a turn number. Stale links are rejected, so two players cannot both act on an outdated board. The workflow processes open valid move issues in order and ignores unrelated issues. Visitors cannot execute issue titles as code: the script accepts only an exact title pattern and uses argument arrays for GitHub CLI calls.

It is not a draggable game. GitHub's README renderer cannot run JavaScript or canvas input. Real-time dragging remains technically impossible inside the README. This version keeps all game activity within GitHub using issue submissions and Actions.

The bot needs no personal access token; it uses the repository workflow token. Successful runs make bot commits. These are game-state updates, not personal contribution claims.

## Design and checks

The plain bio, project table, and stack list are replaced by custom driver-dossier, project-card, and engineering-specification SVG panels. Alt text supplies text descriptions. All profile information is visible immediately.

Local checks passed for all referenced graphics, SVG XML, valid moves, collisions, restarts, best score, stale moves, title filtering, and control regeneration. A GitHub deployment has not been performed, and the issue workflow has not been tested live in your repository. The streak remains an external image service with a direct GitHub calendar fallback.

GitHub documentation:
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#issues
- https://docs.github.com/en/actions/tutorials/authenticate-with-github_token
