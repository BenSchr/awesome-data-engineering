---
mode: 'edit'
description: 'Create an implementation plan for a specification document'
---

Your goal is to generate a functional spec for implementing a feature based on a provided file or user input. If no input is provided, ask the user for details about the feature.

RULES:
- Clearly state the feature's goal.
- List what the feature must do.
- Include acceptance criteria.
- Mention any important dependencies or constraints.
- Be clear and easy to understand.

FIRST:
- Review the #file `.github/memory-bank/projectBrief.md` file to understand the project scope and requirements.
- Review all other memory bank top-level files (files directly under `.github/memory-bank/`) to gather context on the project and its current state.
- Review the attached file document to understand the requirements and objectives.
- If requirements are unclear or missing, ask the user clarifying questions.
- If no file is provided, ask the user about the topics of the feature specification.

NEXT:
- Ask the user for specific feedback to ensure satisfaction.
- Suggest additional considerations or edge cases the user may not have thought about.

FINALLY:
- Output your specification in #folder: `.github/memory-bank/features/{featureId}/featureBrief.md`
- Use the following template for the spec:
  - Feature Goal
  - Functional Requirements
  - Acceptance Criteria
  - Dependencies & Constraints
- DO NOT start implementation without my permission.

