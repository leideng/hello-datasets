# from_generator

Create a Hugging Face `Dataset` from a Python generator function.

## What It Teaches

- `Dataset.from_generator(...)` is useful when examples are produced incrementally.
- The generator should yield one Python dictionary per example.
- This pattern is handy when you want to convert existing Python iteration logic into a dataset.

## Run

From the repository root:

```bash
uv run python load/from_in_memory_data/from_generator/main.py
```

## Expected Result

The script prints:

- a short dataset summary
- the final generated row

## Notes

- The generator-based API is often a clean bridge between custom Python data pipelines and the `datasets` library.
- Keep generated examples small and consistent in shape.
