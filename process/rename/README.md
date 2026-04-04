# rename

Rename a column with `rename_column(...)`.

## What It Teaches

- Renaming columns is often useful when standardizing schema across datasets.
- The row values stay the same; only the column name changes.
- Clear names help later transformation code stay readable.

## Run

From the repository root:

```bash
uv run python process/rename/main.py
```

## Expected Result

The script prints:

- the renamed dataset summary
- the updated column names
- the rows using the new `text` column

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
- Line 7: `            "sentence": [`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `                "rename columns to match your downstream code",`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `                "clear column names reduce confusion",`
  Provides one literal sample value used by the example data or configuration.
- Line 10: `            ],`
  Closes part of the sample data structure being built.
- Line 11: `            "label": [1, 0],`
  Provides one literal sample value used by the example data or configuration.
- Line 12: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 13: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 15: `    renamed_dataset = dataset.rename_column("sentence", "text")`
  Renames one column so later code can use the new field name.
- Line 17: `    print("Dataset after rename_column")`
  Prints information so you can observe what the dataset operation produced.
- Line 18: `    print(renamed_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print("Column names:", renamed_dataset.column_names)`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print("Rows:", renamed_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 24: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 25: `    main()`
  Calls `main()` to start the example.

## Notes

- Use this when two datasets express the same concept with different field names.
