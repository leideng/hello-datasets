# batch

Iterate over a dataset in batches with `Dataset.iter(...)`.

## What It Teaches

- You do not need to materialize every row one by one.
- `iter(batch_size=...)` yields dictionaries of column lists.
- Batch iteration is useful for inspection, export loops, and lightweight processing outside `map`.

## Run

From the repository root:

```bash
uv run python process/batch/main.py
```

## Expected Result

The script prints:

- the dataset summary
- each batch as a dictionary of column lists

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 6: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 7: `            "id": [1, 2, 3, 4, 5],`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "text": [f"example-{i}" for i in range(1, 6)],`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 10: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 12: `    print("Iterating over dataset batches")`
  Prints information so you can observe what the dataset operation produced.
- Line 13: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 14: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 16: `    for batch_index, batch in enumerate(dataset.iter(batch_size=2), start=1):`
  Starts a loop that repeats the same operation for each item in a collection.
- Line 17: `        print(f"Batch {batch_index}: {batch}")`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 21: `    main()`
  Calls `main()` to start the example.

## Notes

- This is an iteration pattern, not a permanent dataset transformation.
