# from_list

Create a Hugging Face `Dataset` from a row-oriented Python list of dictionaries.

## What It Teaches

- `Dataset.from_list(...)` works well when your data starts as records.
- Each dictionary in the list represents one row.
- Feature types are inferred from the Python values.

## Run

From the repository root:

```bash
uv run python load/from_in_memory_data/from_list/main.py
```

## Expected Result

The script prints:

- a short dataset summary
- the column names
- one sample row

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 5: `    records = [`
  Starts a multi-line collection literal used by this example.
- Line 6: `        {"id": 1, "title": "load from a list", "difficulty": "easy"},`
  Closes part of the sample data structure being built.
- Line 7: `        {"id": 2, "title": "rows are Python dicts", "difficulty": "easy"},`
  Closes part of the sample data structure being built.
- Line 8: `        {"id": 3, "title": "schema is inferred automatically", "difficulty": "medium"},`
  Closes part of the sample data structure being built.
- Line 9: `    ]`
  Continues the multi-line Python structure opened by the previous line.
- Line 11: `    dataset = Dataset.from_list(records)`
  Saves a value into `dataset` so later lines can reuse it.
- Line 13: `    print("Dataset created with Dataset.from_list")`
  Prints information so you can observe what the dataset operation produced.
- Line 14: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 15: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 16: `    print("Column names:", dataset.column_names)`
  Prints information so you can observe what the dataset operation produced.
- Line 17: `    print("Row 1:", dataset[1])`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 21: `    main()`
  Calls `main()` to start the example.

## Notes

- Compared with `from_dict`, this input is row-oriented instead of column-oriented.
- This is usually more convenient when prototyping from JSON-like records.
