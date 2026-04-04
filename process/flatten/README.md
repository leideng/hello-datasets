# flatten

Expand nested struct columns with `Dataset.flatten(...)`.

## What It Teaches

- Nested dictionary-like columns can be expanded into top-level columns.
- Flattening is useful before export or when downstream code expects simple schemas.
- Nested fields become dotted column names such as `meta.title`.

## Run

From the repository root:

```bash
uv run python process/flatten/main.py
```

## Expected Result

The script prints:

- the flattened dataset summary
- top-level columns such as `meta.title` and `meta.difficulty`

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
- Line 7: `            "id": [1, 2],`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "meta": [`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `                {"title": "first example", "difficulty": "easy"},`
  Closes part of the sample data structure being built.
- Line 10: `                {"title": "second example", "difficulty": "medium"},`
  Closes part of the sample data structure being built.
- Line 11: `            ],`
  Closes part of the sample data structure being built.
- Line 12: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 13: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 15: `    flattened_dataset = dataset.flatten()`
  Flattens nested fields into top-level columns.
- Line 17: `    print("Dataset after flatten")`
  Prints information so you can observe what the dataset operation produced.
- Line 18: `    print(flattened_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print("Column names:", flattened_dataset.column_names)`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print("Rows:", flattened_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 24: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 25: `    main()`
  Calls `main()` to start the example.

## Notes

- Flattening is especially useful after loading nested JSON-like records.
