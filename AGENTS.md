# AGENTS.md

This repository is a learning workspace for `huggingface/datasets`.

The goal is not to build one large package. The goal is to collect small, focused, self-contained examples that each teach one feature or workflow of the `datasets` library.

## Repository intent

- Use this repo to learn `huggingface datasets` efficiently through minimal runnable examples.
- Each top-level feature directory should demonstrate exactly one main idea.
- Keep examples easy to read, easy to run, and easy to delete or replace.
- Prefer practical examples over abstract helper layers.

## Required structure

Each feature lives in its own top-level subfolder.

Example:

```text
hello-datasets/
  AGENTS.md
  README.md
  pyproject.toml
  load-local-json/
    src/
      main.py
    docs/
      README.md
```

For every feature subfolder:

- `src/` contains the Python source code.
- `docs/` contains:
  - how to run the code
  - what the example demonstrates
  - short learning notes about the relevant `datasets` feature
- The subfolder should be minimal and self-contained.

## Dependency management

- Use `uv` to manage Python dependencies.
- Manage dependencies globally from the repository root.
- Keep a single `pyproject.toml` in the root directory.
- Do not create `pyproject.toml` files inside feature subfolders.
- Keep dependencies minimal. Only add packages required for that specific example.
- Prefer `uv run` for execution in docs and examples.

## What belongs in a feature folder

A good feature folder usually includes:

- `src/`
- `docs/`
- optional small local data files only if they are necessary for the example

A feature folder should not depend on hidden setup in another example folder.

## Coding rules

- Keep code short and direct.
- Prefer a single entry script such as `src/main.py` unless the example genuinely needs more files.
- Avoid premature abstractions, framework code, and utility modules shared across unrelated examples.
- Use clear variable names and straightforward control flow.
- Add comments only when they explain a non-obvious `datasets` behavior.
- Default to ASCII unless the file already uses non-ASCII content.

## Documentation rules

Each feature's `docs/README.md` should usually contain:

- a one-sentence summary of the feature
- prerequisites
- exact `uv` commands to run
- expected output or observable behavior
- key learning points
- links or references to the relevant Hugging Face datasets concepts when useful

Documentation should teach, not just list commands.

## Scope rules

- One folder, one main lesson.
- If a new example teaches a different concept, create a new top-level folder instead of extending an existing one.
- Keep examples independent even if that causes a small amount of duplication.
- Do not turn this repo into a monolithic application or shared library.

## Naming guidance

- Use short, descriptive kebab-case names for feature folders.
- Name folders by the learning topic or workflow, such as:
  - `load-csv`
  - `map-and-filter`
  - `train-test-split`
  - `streaming-dataset`
  - `save-to-disk`

## Preferred workflow for future changes

When adding a new example:

1. Create a new top-level feature folder.
2. Use the root `pyproject.toml` managed with `uv` for dependencies.
3. Put runnable Python code in `src/`.
4. Write learning-oriented documentation in `docs/`.
5. Keep the example independent from other folders.
6. Verify the documented commands are correct.

When modifying an existing example:

- Preserve the folder's single teaching goal.
- Do not add unrelated capabilities.
- Update docs together with code changes.

## Non-goals

- No complex shared infrastructure unless explicitly requested.
- No unnecessary packaging boilerplate.
- No large internal helper framework across examples.
- No hidden assumptions that require reading another folder first.

## Agent instructions

If you are an automated coding agent working in this repo:

- Follow the structure and scope rules in this file.
- Default to creating small, focused, standalone examples.
- Use `uv` for dependency and run instructions.
- If adding a new example, include both `src/` and `docs/`.
- If adding code, also add or update the corresponding documentation.
- Prefer the simplest implementation that accurately demonstrates the `datasets` feature.
