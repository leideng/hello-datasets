# from_dict

Create a Hugging Face `Dataset` directly from a Python dictionary of columns.

## What It Teaches

- `Dataset.from_dict(...)` expects a column-oriented input shape.
- Each dictionary key becomes a dataset column.
- Every column must have the same number of rows.

## Run

From the repository root:

```bash
uv run python load/from_in_memory_data/from_dict/main.py
```

## Expected Result

The script prints:

- a short dataset summary
- the inferred feature schema
- the first row

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
- Line 7: `            "id": [1, 2, 3],`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "text": [`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `                "datasets can be built from plain Python dicts",`
  Provides one literal sample value used by the example data or configuration.
- Line 10: `                "each key becomes a column",`
  Provides one literal sample value used by the example data or configuration.
- Line 11: `                "all columns must have the same length",`
  Provides one literal sample value used by the example data or configuration.
- Line 12: `            ],`
  Closes part of the sample data structure being built.
- Line 13: `            "label": ["tip", "concept", "warning"],`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 15: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 17: `    print("Dataset created with Dataset.from_dict")`
  Prints information so you can observe what the dataset operation produced.
- Line 18: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print("Column names:", dataset.column_names)`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print("Features:", dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 23: `    print("First row:", dataset[0])`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 27: `    main()`
  Calls `main()` to start the example.

## Notes

- This is one of the simplest ways to create a small in-memory dataset.
- Use it when your data is already organized as lists by column.
