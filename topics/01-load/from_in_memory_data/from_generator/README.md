# from_generator

Create a Hugging Face `Dataset` from a Python generator function.

## What It Teaches

- `Dataset.from_generator(...)` is useful when examples are produced incrementally.
- The generator should yield one Python dictionary per example.
- This pattern is handy when you want to convert existing Python iteration logic into a dataset.

## Run

From the repository root:

```bash
uv run python topics/01-load/from_in_memory_data/from_generator/main.py
```

## Expected Result

The script prints:

- a short dataset summary
- the final generated row

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 3: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 6: `def build_examples():`
  Defines `build_examples`, the function that groups one logical step of the example.
- Line 7: `    for i in range(5):`
  Loops over example items to build or transform the dataset input.
- Line 8: `        yield {`
  Yields one example row from the generator-based dataset source.
- Line 15: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 16: `    cache_dir = Path(__file__).resolve().parent / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 18: `    dataset = Dataset.from_generator(build_examples, cache_dir=str(cache_dir))`
  Builds a dataset from a generator so rows are produced by Python code instead of a file.
- Line 26: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- The generator-based API is often a clean bridge between custom Python data pipelines and the `datasets` library.
- Keep generated examples small and consistent in shape.
