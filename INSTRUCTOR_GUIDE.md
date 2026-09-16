# Instructor guide

This repository is designed so the live demonstration is mostly navigation, copy/paste, and discussion. The code changes are intentionally small.

## One-time publishing setup

Create an empty GitHub repository, then publish this local repository:

```bash
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

Keep Issues and Actions enabled in the GitHub repository settings.

## Pre-class checklist

1. Fork the published repository into the account or organization you will use for the demonstration.
2. Clone that fork and open it in Positron.
3. If GitHub prompts you, enable Actions in the fork.
4. On GitHub, open **Actions**, select **Seed demo issue**, choose **Run workflow**, and run it on `main`.
5. Confirm that **Issue #1: Add a data range helper** now exists.
6. Create or open the GitHub Project you will show in class. Add Issue #1 and place it in the appropriate starting status.
7. Open `demo_materials/` in a nearby window so each code example is ready to copy.

The seeding workflow skips creation when an issue with the same title already exists, so rerunning it will not create duplicates.

## Example 1: a complete proposal

Start by opening Issue #1 and reading its acceptance criteria.

Create the branch:

```bash
git switch main
git pull
git switch -c issue-1-data-range
git status
```

Copy the function from `demo_materials/example-1-data-range.py` into `stats_helpers.py`, then commit and push:

```bash
git add stats_helpers.py
git commit -m "Add data range helper"
git push -u origin issue-1-data-range
```

Open a pull request with this description:

```markdown
Fixes #1

Adds `data_range(values)` to calculate the difference between the maximum and minimum.
```

Review the files changed, merge the pull request into `main`, and confirm that Issue #1 closes automatically. Then synchronize the local copy:

```bash
git switch main
git pull
git log --oneline -3
```

## Example 2: a proposal that needs revision

Create Issue #2 live. Copy the title and body from `demo_materials/issue-2-safe-average.md`, then add the issue to the Project.

Create the branch:

```bash
git switch main
git pull
git switch -c issue-2-safe-average
```

Copy the function from `demo_materials/example-2-first-proposal.py` into `stats_helpers.py`, then commit and push:

```bash
git add stats_helpers.py
git commit -m "Add average helper"
git push -u origin issue-2-safe-average
```

Open a pull request with `Fixes #2` in the description. Review the proposal against the issue and request a change because the empty case is missing.

Replace the first implementation with the function from `demo_materials/example-2-revision.py`, then update the same branch:

```bash
git add stats_helpers.py
git commit -m "Handle empty values in average helper"
git push
```

Show that the existing pull request updates. Review again, approve, merge, and synchronize local `main`.

## Merge conflict demonstration

The two branches must begin from the same version of `main`. Create and push both branches before merging either pull request.

Create Branch A:

```bash
git switch main
git pull
git switch -c conflict-add-median
```

Replace the contents of `analysis_config.py` with `demo_materials/conflict-branch-a.py`, then run:

```bash
git add analysis_config.py
git commit -m "Add median summary metric"
git push -u origin conflict-add-median
```

Create Branch B from the same unchanged `main`:

```bash
git switch main
git switch -c conflict-add-standard-deviation
```

Replace the contents of `analysis_config.py` with `demo_materials/conflict-branch-b.py`, then run:

```bash
git add analysis_config.py
git commit -m "Add standard deviation summary metric"
git push -u origin conflict-add-standard-deviation
```

Open a pull request for each branch. Merge Branch A first. Return to Branch B and incorporate the new `main`:

```bash
git switch conflict-add-standard-deviation
git fetch origin
git merge origin/main
```

Git pauses with a conflict in `analysis_config.py`. Use Positron to inspect both versions. Replace the file with `demo_materials/conflict-resolution.py`, then finish the merge:

```bash
git add analysis_config.py
git commit -m "Resolve summary metrics conflict"
git push
git status
```

Return to the Branch B pull request, show that the conflict is gone, review the combined proposal, and merge it.

## Useful reset point

If you want a clean rehearsal, create a new fork and run the issue-seeding workflow again. Each fork has its own issues, pull requests, Actions, and Projects.

