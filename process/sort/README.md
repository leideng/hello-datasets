# sort

Order rows by a column with `Dataset.sort(...)`.

## What It Teaches

- Sorting reorders the dataset by one or more columns.
- `reverse=True` gives descending order.
- This is useful for ranking, inspection, or deterministic report generation.

## Run

From the repository root:

```bash
uv run python process/sort/main.py
```

## Expected Result

The script prints:

- the sorted dataset summary
- rows ordered by highest score first

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
- Line 7: `            "id": [1, 2, 3, 4],`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "score": [0.82, 0.95, 0.74, 0.91],`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 10: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 12: `    sorted_dataset = dataset.sort("score", reverse=True)`
  Sorts the dataset by the chosen column.
- Line 14: `    print("Dataset after sort")`
  Prints information so you can observe what the dataset operation produced.
- Line 15: `    print(sorted_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 16: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 17: `    print("Rows:", sorted_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 21: `    main()`
  Calls `main()` to start the example.

## Notes

- Sorting changes row order but not row values.
