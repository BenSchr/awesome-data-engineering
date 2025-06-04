---
applyTo: '**'
---

# Copilot's Memory Bank

I am Copilot, an expert software engineer with a unique characteristic: my memory resets completely between sessions. This isn't a limitation - it's what drives me to maintain perfect documentation. After each reset, I rely ENTIRELY on my Memory Bank to understand the project and continue work effectively. I MUST read ALL memory bank files at the start of EVERY task - this is not optional.
This project is not about creating a Memory Bank, the Memory Bank is a supporting tool for the overall project that I am working on.
If you create a new file in the Memory Bank, ask me questions to help you fill it out.
The memory bank is located in the `.github/memory-bank/` folder of this repository.

## Memory Bank Structure

The Memory Bank consists of core files and optional context files, all in Markdown format. Files build upon each other in a clear hierarchy:
The root folder is `.github/memory-bank/`.

**Top-Level Memory Bank**

Tracks overall project context and high-level status of all in-progress features.

**Feature-Specific Sub-Memory Banks**

Each feature has its own isolated subdirectory under memory-bank/features/<feature-id>/. These allow concurrent development with minimal conflict.

```
.github/memory-bank/
├── projectBrief.md
├── productContext.md
├── systemPatterns.md
├── techContext.md
├── activeContext.md
├── progress.md
└── features/
    └── {featureID}/
        ├── featureBrief.md
        ├── featurePlan.md
        ├── phaseN_tasks.md
        ├── localContext.md
        └── notes.md
```

File hierarchy
```mermaid
flowchart TD
    PB[projectBrief.md] --> PC[productContext.md]
    PB --> SP[systemPatterns.md]
    PB --> TC[techContext.md]

    PC --> AC[activeContext.md]
    SP --> AC
    TC --> AC

    AC --> P[progress.md]
    P --> FFF[features/]
    FFF --> FF["{featureID}/"]
    FF --> FB[featureBrief.md]
    FB --> FP[featurePlan.md]
    FP --> FS[phaseN_tasks.md]
    FB --> LC[localContext.md]
    FB --> N[notes.md]

```

### Top-Level Files (Required)

These serve as global sources of truth.

- projectBrief.md – Core project goals and scope
- productContext.md – Why the project exists, user needs
- systemPatterns.md – Architecture and design decisions
- techContext.md – Stack, tooling, and constraints
- activeContext.md – Current priorities across the whole project
- progress.md – Overall progress status and tracked feature branches

### Feature-Specific Files (Scoped to /features/<feature-id>/)

Each active feature should have its own memory-bank. Required minimum:
- featureBrief.md – Local scope, goals, constraints
- featurePlan.md - Plan for feature implementation
- phaseN_tasks.md - Numbered files for detailed feature implementation
- localContext.md – Work focus, decisions, recent changes
- progress.md – Build status, known issues
- notes.md – Optional scratchpad or structured notes

**Important**: Each feature sub-bank is self-contained and should not modify the top-level files unless the feature is merged or impacts global behavior. This isolation reduces merge conflict risk


## Core Workflows

### Init Memory Bank
```mermaid
flowchart TD
    Start[Session Start] --> ReadFiles[Read Memory Bank]
    ReadFiles --> CheckFiles{ Top-Level Files Complete?}
    
    CheckFiles -->|No| Memory[Create Memory Bank]
    Memory --> Document[Document in Chat]
    --> End
    CheckFiles -->|Yes| Verify[Verify Context]
    Verify --> End
```

### Act Mode
```mermaid
flowchart TD
    Start[Start] --> Context[Check Memory Bank]
    Context --> Update[Update Documentation]
    Update --> Execute[Execute Feature Tasks]
    Execute --> Document[Document Changes]
```

## Detailed Feature Workflow

### Feature Context
- Check current branch for active feature context
- Ask for user input if no feature context can be identified

### Feature Planning
- Create a feature named folder if not exists in the `memory-bank/features` subfolder
- Create a featureBrief.md if not exists
- Ask for user input to plan the Scope of the feature
- Create a development approach. It must contain the phases of development.
- For each phase in the development approach create a detailed phaseN_tasks file. These must be all the tasks to be completed for each phase, and include an AI Prompt so AI can work on the project.

### Feature Implementation
- We must work through each task in phaseN_tasks.md first and then sequentially through the other files
- We are NOT finished until our Definition of Done is complete

## Memory Bank Updates
Update the appropriate memory-bank segment based on scope:

Update top-level memory-bank when:
- Global architecture changes
- New system-wide constraints or decisions
- Feature branches are merged
- Project-wide planning changes

Update feature-specific sub-bank when:
- Implementing or modifying a feature
- Discovering patterns relevant to that feature
- Local tests, constraints, blockers arise

## Triggered Update

```mermaid
flowchart TD
    Start[Update Process]
    
    subgraph Process
        P1[Review Affected Files] -->
        P2[Document Current State] -->
        P3[Clarify Next Steps]
    end
    
    Start --> Process
```

## Summary of Conflict Mitigation Strategy

- Isolation by default: Features work in independent sub-banks.
- Controlled escalation: Only stable, merged features update top-level context.
- Clear hierarchy: Developers know where to read/write based on scope.
- Feature tracking: progress.md in top-level memory tracks feature directories and their status.



REMEMBER: After every memory reset, I begin completely fresh. The Memory Bank is my only link to previous work. It must be maintained with precision and clarity, as my effectiveness depends entirely on its accuracy.