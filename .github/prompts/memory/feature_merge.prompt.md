# Feature Cleanup and Memory Bank Merge Prompt

You are about to finalize a feature branch. Follow these steps to ensure all relevant knowledge is preserved and the Memory Bank remains accurate:

1. **Review Feature Sub-Bank**
   - Examine all files in `.github/memory-bank/features/{featureID}/`.
   - Identify decisions, patterns, constraints, or knowledge that should be elevated to the top-level Memory Bank.

2. **Cleanup Feature Files**
   - Remove obsolete, redundant, or temporary notes from the feature sub-bank.
   - Ensure all tasks in `phaseN_tasks.md` are marked as complete or moved to the appropriate backlog if unfinished.

3. **Merge Context Upwards**
   - For each relevant insight, update the corresponding top-level file:
     - `systemPatterns.md` for reusable patterns or architecture changes.
     - `techContext.md` for stack/tooling updates.
     - `productContext.md` for user needs or product scope changes.
     - `activeContext.md` for current priorities.
     - `progress.md` to reflect feature completion and status.

4. **Archive or Remove Feature Sub-Bank**
   - If the feature is fully merged and no longer needed, archive or delete the feature's subdirectory under `features/`.

**Prompt for AI:**
- "Review the feature sub-bank for {featureID}. Clean up obsolete content, and merge all relevant context into the top-level Memory Bank files. Summarize what was merged and why. Archive or remove the feature sub-bank if appropriate."
