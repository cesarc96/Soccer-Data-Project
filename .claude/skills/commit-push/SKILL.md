---
name: commit-push
description: Check branch state, write a best-practice commit message, show a review summary, and push only after explicit user approval.
---

Follow these steps exactly and do not skip any.

## Step 1 — check branch state

Run the following in parallel:
- `git status` — list staged, unstaged, and untracked files
- `git log --oneline origin/main..HEAD` — commits ahead of origin/main
- `git fetch origin` then `git log --oneline HEAD..origin/main` — commits on origin/main not yet local

If origin/main has commits the local branch is missing, stop and tell the user:
> "Your branch is behind origin/main. Pull and resolve any conflicts before committing."
Do not proceed until the user confirms the branch is up to date.

## Step 2 — review changes

Run `git diff HEAD` to understand what changed. Read modified source files if the diff alone is not enough to understand the intent.

## Step 3 — write the commit message

- **Subject line:** 50 characters or fewer, imperative mood ("Add", "Fix", "Update"), no trailing period
- **Blank line** between subject and body
- **Body:** explain *what* and *why*, not how. Wrap at 72 characters. Omit if the subject is self-explanatory.
- Use a conventional prefix where it fits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`

## Step 4 — show review summary and ask for approval

Present this to the user before doing anything else:

---
**Branch:** <current branch>
**Ahead of origin/main by:** <n> commit(s)

**Files to be committed:**
<list every file with its status: modified / new / deleted>

**Proposed commit message:**
```
<full commit message>
```

Do you approve this commit and push? (yes / edit message / cancel)

---

## Step 5 — commit and push

Only proceed on explicit user approval.

- **Approved:** `git add` the relevant files, commit with the approved message, then `git push`
- **Edit message:** show the revised message and ask for approval again
- **Cancelled:** stop, do not commit or push anything

After a successful push, confirm with the commit hash and remote branch name.
