---
mode: 'edit'
description: 'Create an implementation plan for a specification document'
---

Your goal is to generate an implementation plan for a specification document provided to you.

RULES:
- Keep implementations simple, do not over architect
- Do not generate real code for your plan, pseudocode is OK
- The `featurePlan.md` should only contain the high-level phases of the implementation, with a brief objective for each phase.
- All detailed steps, tasks, and AI prompts for each phase must be placed in the corresponding `phaseN_tasks.md` subfiles.
- For each phase, include only a summary/objective in the plan; do not include detailed steps or pseudocode in `featurePlan.md`.
- Call out any necessary user intervention required for each phase in the plan.
- Consider accessibility part of each phase and not a separate phase

FIRST:
- Review the #file `.github/memory-bank/projectBrief.md` file to understand the project scope and requirements.
- Review all other memory bank top-level files to gather context on the project and its current state.
- Review the attached `featureBrief` document to understand the requirements and objectives.
- If no specification document is provided, ask the user to provide one.

THEN:
- Create a high-level implementation plan that outlines the phases needed to achieve the objectives of the specification document.
- For each phase, provide a clear objective and summary (no detailed steps).
- Structure your plan as follows, and output as Markdown code block

NEXT:
- Iterate with me until I am satisifed with the plan

FINALLY:
- Output your plan in #folder:.`.github/memory-bank/features/{featureID}/featurePlan.md`
- For each phase in the development approach, create a detailed `phaseN_tasks.md` file. These must contain all the tasks to be completed for each phase, and include an AI Prompt so AI can work on the project.
- DO NOT start implementation without my permission.

