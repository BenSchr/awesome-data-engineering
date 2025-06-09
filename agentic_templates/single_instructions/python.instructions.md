---
applyTo: '**'
---
This file contains Python programming rules for clean coding and project maintenance.

## Important Rules
- uv will be the package manager of choice.
- NEVER add packages on your behalf
- run the project using `uv run python <main-file.py>`
- use the `src/<project_name>` layout for the python project
- we will use `ruff` for linting and code formatting
- We will use `pytest` for testing framework.
- We MUST always think about the tests we need before writing code.
- All tests must be written first and then the code.
- When tests fail - its because the code is invalid and the code must be fixed.
- We MUST Strictly follow a TEST first approach to coding otherwise we will get in a mess.
- Use absolute imports, never relative imports

## Project structure
/root/<project-name>/src/<project-name>/

## Type Hints
- Use type hints for all function parameters and returns
- Import types from `typing` module
- Use `Optional[Type]` instead of `Type | None`
- Use `TypeVar` for generic types
- Define custom types in `types.py`

## Testing
- Use pytest for testing
- Use pytest-cov for coverage
- Implement proper fixtures

## Documentation
- Use Google-style docstrings
- Keep README.md updated
- Use proper inline comments
- Document environment setup

## Dependencies
- Separate dev dependencies
- Check for security vulnerabilities

## Security
- Implement proper logging
- Follow OWASP guidelines

## Error Handling
- Create custom exception classes
- Use proper try-except blocks
- Implement proper logging
- Return proper error responses
- Handle edge cases properly
- Use proper error messages

## Definition of Done
- Integration tests are passing
- The code must be formatted using `ruff`
- The code must have no linting errors or warnings
- ALL our tests MUST pass with no errors or warnings

