# Project Brief: Awesome Data Engineering Awesomelist Agent

## Project Overview
A tool-assisted workflow for curating, organizing, and maintaining an awesomelist of data engineering resources. Users manually collect and dump links into a file. An LLM agent, triggered on demand, sorts new links into a structured Markdown awesomelist and maintains a monthly changelog of additions. The agent preserves formatting, avoids duplicates, and suggests categories for ambiguous links. The project and its outputs must follow the official awesomelist style guide for structure, formatting, and best practices.

## Core Objectives and Goals
- Enable users to manually collect and dump resource links for later curation
- Use an LLM agent to sort and categorize new links into the awesomelist (readme.md) on demand
- Maintain a human-readable changelog (CHANGELOG.md) listing links added each month
- Avoid duplicate entries in the awesomelist
- Preserve formatting and order of the awesomelist
- Suggest categories for links that fit multiple sections (with user confirmation in future iterations)
- Ensure the awesomelist and all related files comply with the awesomelist style guide

## Technical Specifications
- All files are Markdown: `linkdump.md` (input), `readme.md` (awesomelist), `CHANGELOG.md` (changelog)
- Manual workflow: user collects links, agent is triggered on demand
- LLM agent prompt file instructs the agent to sort dumped links, avoid duplicates, preserve formatting, suggest categories for ambiguous links, and enforce the awesomelist style guide
- No backend, UI, or automation required
- Platform-agnostic, can be run locally as a script or tool
- Awesomelist output must pass style guide checks (e.g., section order, link formatting, descriptions, badges, etc.)

## Non-Functional Requirements
- Simplicity: No automation or UI, all actions are manual
- Extensibility: Future support for malformed/inactive link detection, automated category suggestions, and user confirmation for ambiguous links
- Reliability: Agent must not corrupt or misformat the awesomelist
- Transparency: Changelog provides a clear record of monthly additions
- Compliance: All outputs must adhere to the awesomelist style guide

## Success Metrics
- All new links from `linkdump.md` are correctly categorized and added to `readme.md` without duplicates
- Changelog is updated monthly with new additions
- Awesomelist formatting and order are preserved and compliant with the style guide
- User feedback on ease of use and accuracy
- Awesomelist passes style guide validation tools (if available)

## Out of Scope
- Automated link collection or submission interfaces
- Automated detection of malformed or inactive links (may be added later)
- Automated category assignment without user confirmation for ambiguous links (may be added later)
- Moderation, approval workflows, or multi-user support

# Awesomelist Structure & Contributor Guidance (Merged from feature memory bank)

## Feature Overview
The awesomelist is structured so that only topics and categories with at least one resource/link are included. Each section uses a clear, relevant emoji for navigation and clarity. Contributor guidance is provided to ensure future additions follow these rules.

## Functional Requirements
- Only create topics/categories if there is at least one resource/link for them.
- Assign each resource to the most fitting topic/category (no duplicates).
- Use an appropriate emoji for each topic/category (see Emoji Legend).
- Update the Table of Contents to reflect only present topics/categories.
- Provide clear contributor guidance for adding new topics/categories: only add if a resource exists, always include an emoji.
- Ensure accessibility and clarity in structure and navigation, including clear section headings and descriptive link text.

## Contributor Guidance
- Only add a new topic/category if you are including at least one resource/link for it. No empty sections.
- Every topic/category must have an appropriate emoji in its heading. Use the emoji legend for reference. If you introduce a new topic/category, select a clear, relevant emoji and update the legend.
- Each resource should appear only once, in the most relevant section. Do not duplicate resources across multiple topics/categories.
- Use clear, descriptive section headings and link text. Ensure the Table of Contents is accurate and all links work. Structure the list for easy navigation and readability.

## Emoji Legend (Example)
- 🛠️ Product Repos
- 🔧 Useful Repos
- 📚 Books
- 📝 Blogs
- 📦 Repos
- 🧱 Databricks

## Implementation Plan (Phased)
1. **Audit and Categorize**: Identify all resources, assign to most relevant category, avoid duplicates.
2. **Define Structure & Emojis**: Design structure, assign/document emojis for each section.
3. **Update Content & ToC**: Refactor readme.md, apply structure/emojis, update ToC, remove empty sections.
4. **Contributor Guidance**: Add clear rules for contributors (see above).
5. **Review & Validation**: Ensure all acceptance criteria are met (no empty sections, no duplicates, accurate ToC, clear navigation, guidance present).

## Acceptance Criteria
- Only topics/categories with at least one resource are present.
- Each resource appears only once, in the most relevant section.
- All topics/categories use appropriate emojis.
- Table of Contents is accurate and links work.
- Contributor guidance is present and clear.
- No empty sections are present.
- Navigation and structure are accessible and easy to follow.

---

## Project Brief

The goal of the awesomelist project is to provide a curated, accessible, and well-organized list of resources for data engineering. The structure of the list (topic-based, generic categories, or other) is user-driven and may change over time. The memory bank must always reflect the current, actual structure of the main documentation (e.g., readme.md), not just the intended or previous structure.