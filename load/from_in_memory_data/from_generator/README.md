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

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 3: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 6: `def build_examples():`
  Defines the function `build_examples` so the example logic is grouped into a named step.
- Line 7: `    for i in range(5):`
  Starts a loop that repeats the same operation for each item in a collection.
- Line 8: `        yield {`
  Yields one generated example row at a time from the generator.
- Line 9: `            "id": i,`
  Provides one literal sample value used by the example data or configuration.
- Line 10: `            "text": f"example-{i}",`
  Provides one literal sample value used by the example data or configuration.
- Line 11: `            "length": len(f"example-{i}"),`
  Provides one literal sample value used by the example data or configuration.
- Line 12: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 15: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 16: `    cache_dir = Path(__file__).resolve().parent / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 18: `    dataset = Dataset.from_generator(build_examples, cache_dir=str(cache_dir))`
  Builds a dataset lazily from a Python generator function.
- Line 20: `    print("Dataset created with Dataset.from_generator")`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 23: `    print("Last row:", dataset[len(dataset) - 1])`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 27: `    main()`
  Calls `main()` to start the example.

## Notes

- The generator-based API is often a clean bridge between custom Python data pipelines and the `datasets` library.
- Keep generated examples small and consistent in shape.
