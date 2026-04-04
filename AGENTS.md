# AGENTS.md

This repository is a learning workspace for `huggingface/datasets`.

The goal is not to build one large package. The goal is to collect small, focused, self-contained examples that each teach one feature or workflow of the `datasets` library.

## Repository intent

- Use this repo to learn `huggingface datasets` efficiently through minimal runnable examples.
- Each top-level feature directory should demonstrate exactly one main idea.
- Keep examples easy to read, easy to run, and easy to delete or replace.
- Prefer practical examples over abstract helper layers.
- Largely follow the existing topic tree already present in the repository.

## Required structure

The repository already contains a topic taxonomy such as `load/`, `process/`, `export/`, `config/`, `stream/`, and related nested subfolders.

Prefer placing new work into the existing topic tree instead of inventing a parallel structure. You may refine or extend the structure when necessary, but do so deliberately and keep names consistent with the current layout.

Each concrete example should live in the most relevant existing topic subfolder.

Example:

```text
hello-datasets/
  AGENTS.md
  README.md
  pyproject.toml
  load/
    load_dataset/
      from_json/
        main.py
        README.md
        data/
          sample.json
```

For every concrete example folder:

- put runnable Python source code directly in the example root
- put the example documentation in a root-level `README.md`
- keep local test data or sample input files in `data/` when needed
- `README.md` contains:
  - how to run the code
  - what the example demonstrates
  - short learning notes about the relevant `datasets` feature
  - a line-by-line code explanation section for beginners
- The subfolder should be minimal and self-contained.

## Dependency management

- Use `uv` to manage Python dependencies.
- Manage dependencies globally from the repository root.
- Keep a single `pyproject.toml` in the root directory.
- Do not create `pyproject.toml` files inside feature subfolders.
- Keep dependencies minimal. Only add packages required for that specific example.
- Prefer `uv run` for execution in docs and examples.

## What belongs in a feature folder

A good concrete example folder usually includes:

- `main.py` or another small root-level Python file
- `README.md`
- optional `data/`
- optional small local data files only if they are necessary for the example

A concrete example folder should not depend on hidden setup in another example folder.

## Coding rules

- Keep code short and direct.
- Prefer a single entry script such as `main.py` in the example root unless the example genuinely needs more files.
- Avoid premature abstractions, framework code, and utility modules shared across unrelated examples.
- Use clear variable names and straightforward control flow.
- Add comments only when they explain a non-obvious `datasets` behavior.
- Default to ASCII unless the file already uses non-ASCII content.

## Documentation rules

Each feature's root-level `README.md` should usually contain:

- a one-sentence summary of the feature
- prerequisites
- exact `uv` commands to run
- expected output or observable behavior
- key learning points
- a line-by-line explanation of the code so a beginner can follow what each part does
- links or references to the relevant Hugging Face datasets concepts when useful

Documentation should teach, not just list commands. This repository is for beginners, so prefer explicit, patient explanations over terse summaries.

## Scope rules

- One concrete example folder, one main lesson.
- If a new example teaches a different concept, first check whether it fits naturally into the existing topic tree.
- Only create a new top-level topic when the current tree does not provide a clean home for the concept.
- Keep examples independent even if that causes a small amount of duplication.
- Do not turn this repo into a monolithic application or shared library.

## Naming guidance

- Preserve the current semantic grouping used by directories such as `load/load_dataset/from_json` or `process/format/tensor_format/torch`.
- Use short, descriptive snake_case or existing-style names that match nearby folders.
- Prefer consistency with sibling directories over introducing a new naming style.

## Preferred workflow for future changes

When adding a new example:

1. Read the current topic tree in `README.md` first.
2. Choose the most relevant existing topic path.
3. Use the root `pyproject.toml` managed with `uv` for dependencies.
4. Put runnable Python code directly in the example root.
5. Write learning-oriented documentation in the example's root-level `README.md`, including a line-by-line code explanation section.
6. Use `data/` for local test data or sample files when needed.
7. Keep the example independent from other folders.
8. Verify the documented commands are correct.

When modifying an existing example:

- Preserve the folder's single teaching goal.
- Do not add unrelated capabilities.
- Update docs together with code changes.

Before writing new code:

- Update `README.md` if the topic tree changes.
- Keep the recursive topic list in `README.md` complete and current.

## Non-goals

- No complex shared infrastructure unless explicitly requested.
- No unnecessary packaging boilerplate.
- No large internal helper framework across examples.
- No hidden assumptions that require reading another folder first.

## Agent instructions

If you are an automated coding agent working in this repo:

- Follow the structure and scope rules in this file.
- Read the existing directory tree before proposing a new location.
- Default to creating small, focused, standalone examples.
- Use `uv` for dependency and run instructions.
- If adding a new example, put code files and `README.md` in the example root, and use `data/` only for local data files.
- Update `README.md` first when introducing or changing topic paths.
- If adding code, also add or update the corresponding documentation, including a line-by-line code explanation section in the example `README.md`.
- Prefer the simplest implementation that accurately demonstrates the `datasets` feature.
