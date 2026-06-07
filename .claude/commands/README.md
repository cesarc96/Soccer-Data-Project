# Commands

Project-scoped slash commands. Each command is a single markdown file:

```
.claude/commands/<command-name>.md
```

The file body is the prompt Claude runs when the user types `/<command-name>`.
Optional YAML frontmatter (`description`, `argument-hint`, `allowed-tools`)
controls how the command shows up in the picker and what it can do.

Use these for repeatable workflows — e.g. `/refresh-fixtures`, `/check-data-quality`,
`/new-dbt-model`.
