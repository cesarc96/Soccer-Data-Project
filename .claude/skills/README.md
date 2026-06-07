# Skills

Project-scoped skills for Claude Code. Each skill lives in its own directory:

```
.claude/skills/<skill-name>/
└── SKILL.md
```

`SKILL.md` starts with YAML frontmatter (`name`, `description`, optional `allowed-tools`)
followed by the instructions Claude should follow when the skill is invoked.

Skills are auto-discovered by Claude Code from this directory. Keep each one
focused on a single capability (one verb, one outcome).
