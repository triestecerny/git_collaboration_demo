# Git collaboration demonstration

This small repository supports a live class demonstration of a collaborative Git and GitHub workflow:

1. Define work in an issue.
2. Develop the change on a branch.
3. Commit and push the branch.
4. Open a pull request.
5. Review the proposal.
6. Revise or merge it.

The code is intentionally simple. The focus is the collaboration process and the evidence each step preserves.

## Repository contents

- `stats_helpers.py` is the starting point for two pull request examples.
- `analysis_config.py` is the starting point for the merge conflict demonstration.
- `demo_materials/` contains prepared issue text and copy/paste code.
- `.github/PULL_REQUEST_TEMPLATE.md` gives every pull request the same useful structure.
- `.github/workflows/seed-demo-issue.yml` creates the first demonstration issue in a fresh fork.

## Instructor setup

See [`INSTRUCTOR_GUIDE.md`](INSTRUCTOR_GUIDE.md) for the one-time publishing steps, the pre-class checklist, and the exact demonstration sequence.

## Why Issue #1 is seeded after forking

A fork is a separate repository with its own issues and settings. After forking this repository, run the **Seed demo issue** workflow once. It creates the first work item inside the fork so that `Fixes #1` can link the first pull request to the correct issue.

