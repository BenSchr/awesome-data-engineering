---
applyTo: '**'
description: 'https://github.com/cannuri/roo-code-dynamic-rules'
---

## Additional Rules

- When a user requests additional rules, add them to the "Additional Rules" section of the `.github/instructions/dynamic_rules_file.instructions.md` file.
- Identify new rules by the prefix `RULE:` in user messages.
- For example, if the user writes `RULE: keep the README.md up to date`, append the rule as `- keep README.md up to date`.
- In contrary if a user writes `NORULE:` you remove the according line from the "Additional Rules" section.
- Persist these rules throughout the project lifecycle.
- Ensure that all added rules are clear, specific, and actionable.
- Format each rule as a separate bullet point.