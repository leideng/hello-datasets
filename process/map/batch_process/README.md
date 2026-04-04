# batch_process

Apply a batched transformation with `Dataset.map(..., batched=True)`.

## What It Teaches

- `map` can process examples one by one or in batches.
- Batched processing is often simpler and faster for vectorized transformations.
- A batched function receives lists for each input column and should return lists of equal length.

## Run

From the repository root:

```bash
uv run python process/map/batch_process/main.py
```

## Expected Result

The script prints:

- the transformed dataset summary
- the new column names
- the resulting rows with a derived `summary` column

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def add_summary(batch: dict[str, list]) -> dict[str, list]:`
  Defines the function `add_summary` so the example logic is grouped into a named step.
- Line 5: `    return {`
  Returns the computed value back to the caller.
- Line 6: `        "summary": [`
  Provides one literal sample value used by the example data or configuration.
- Line 7: `            f"{title} ({priority})"`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 8: `            for title, priority in zip(batch["title"], batch["priority"])`
  Starts a loop that repeats the same operation for each item in a collection.
- Line 9: `        ]`
  Continues the multi-line Python structure opened by the previous line.
- Line 10: `    }`
  Continues the multi-line Python structure opened by the previous line.
- Line 13: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 14: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 15: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 16: `            "id": [1, 2, 3],`
  Provides one literal sample value used by the example data or configuration.
- Line 17: `            "title": [`
  Provides one literal sample value used by the example data or configuration.
- Line 18: `                "read the dataset docs",`
  Provides one literal sample value used by the example data or configuration.
- Line 19: `                "write a map example",`
  Provides one literal sample value used by the example data or configuration.
- Line 20: `                "verify the output",`
  Provides one literal sample value used by the example data or configuration.
- Line 21: `            ],`
  Closes part of the sample data structure being built.
- Line 22: `            "priority": ["high", "medium", "high"],`
  Provides one literal sample value used by the example data or configuration.
- Line 23: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 24: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 26: `    mapped_dataset = dataset.map(add_summary, batched=True, batch_size=2)`
  Applies `map(...)` to create a transformed version of the dataset.
- Line 28: `    print("Dataset after batched map")`
  Prints information so you can observe what the dataset operation produced.
- Line 29: `    print(mapped_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 30: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 31: `    print("Column names:", mapped_dataset.column_names)`
  Prints information so you can observe what the dataset operation produced.
- Line 32: `    print("Rows:", mapped_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 35: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 36: `    main()`
  Calls `main()` to start the example.

## Notes

- Batched `map` is a common default when a transformation can be expressed over lists.
- The output batch length must match the input batch length unless you are intentionally changing row counts.
