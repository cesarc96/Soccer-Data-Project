---
description: Orient Claude at the start of a session — read project context, review recent work, and confirm how to collaborate.
---

You are starting a new working session on the Soccer Data Project. Do the following in order:

1. Read `CLAUDE.md` to load project conventions, the current phase, implemented endpoints, and working rules.

2. Read memory files at `/Users/cc309378/.claude/projects/-Users-cc309378-Documents-Personal-Soccer-Data-Project/memory/` to load persistent context about user preferences, feedback, and project decisions from prior sessions.

3. Run `git log --oneline -10` to see what was done recently.

4. Run `git status` to check for any uncommitted changes or in-progress work left over from the last session.

5. Read `src/soccer_data/client.py` to see which endpoints are currently implemented.

6. Read `src/soccer_data/models.py` to see the current data models.

7. Read `tests/test_client.py` to see what is tested vs. what is still a stub.

8. List files in `.claude/commands/` to know what slash commands are available this session.

9. Check (do not read) that a `.env` file exists. If it does not, flag it — any work that calls the live API will fail without it.

After reading, summarize in plain language:

**Project state**
- What the project is and what phase it is in

**Recent work**
- What was done in the last few commits
- Any uncommitted changes to be aware of

**Current code**
- Endpoints implemented in `client.py`
- Models defined in `models.py`
- What is tested vs. stubbed in the test file

**Housekeeping**
- Available slash commands
- Whether `.env` is present

Then ask the user what they want to work on today.

Keep each section to two to four bullet points. Do not start writing code until the user says what to work on.

## Committing and pushing

Whenever the user says they want to commit, push, or ship changes during this session, apply the skill defined in `.claude/skills/commit-push/SKILL.md`. Do not run any git commit or push commands outside of that workflow.
