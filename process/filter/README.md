# filter

Keep only rows that match a condition with `Dataset.filter(...)`.

## What It Teaches

- `filter` removes rows that do not satisfy a predicate.
- The filter function returns `True` to keep a row and `False` to drop it.
- Filtering is one of the most common cleanup steps before training or evaluation.

## Run

From the repository root:

```bash
uv run python process/filter/main.py
```

## Expected Result

The script prints:

- the filtered dataset summary
- only the rows whose `priority` is `high`

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def keep_high_priority(example: dict[str, str]) -> bool:`
  Defines the function `keep_high_priority` so the example logic is grouped into a named step.
- Line 5: `    return example["priority"] == "high"`
  Returns the computed value back to the caller.
- Line 8: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 9: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 10: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 11: `            "id": [1, 2, 3, 4],`
  Provides one literal sample value used by the example data or configuration.
- Line 12: `            "task": [`
  Provides one literal sample value used by the example data or configuration.
- Line 13: `                "load local data",`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `                "read the docs",`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `                "profile a transformation",`
  Provides one literal sample value used by the example data or configuration.
- Line 16: `                "write notes",`
  Provides one literal sample value used by the example data or configuration.
- Line 17: `            ],`
  Closes part of the sample data structure being built.
- Line 18: `            "priority": ["high", "low", "high", "medium"],`
  Provides one literal sample value used by the example data or configuration.
- Line 19: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 20: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 22: `    filtered_dataset = dataset.filter(keep_high_priority)`
  Applies `filter(...)` to keep only rows that match the condition.
- Line 24: `    print("Dataset after filter")`
  Prints information so you can observe what the dataset operation produced.
- Line 25: `    print(filtered_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 27: `    print("Rows:", filtered_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 30: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 31: `    main()`
  Calls `main()` to start the example.

## Notes

- `filter` changes the number of rows.
- Prefer simple predicates first, then add more complex logic only when needed.
