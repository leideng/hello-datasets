# concatenate

Combine multiple datasets with `concatenate_datasets(...)`.

## What It Teaches

- Datasets with the same schema can be stacked vertically.
- Concatenation is useful when merging shards or appending extra examples.
- All input datasets should have compatible columns and feature types.

## Run

From the repository root:

```bash
uv run python process/concatenate/main.py
```

## Expected Result

The script prints:

- the combined dataset summary
- all rows from both source datasets in order

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset, concatenate_datasets`
  Imports `Dataset, concatenate_datasets` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 5: `    train_like = Dataset.from_dict(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 6: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 7: `            "id": [1, 2],`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "text": ["first dataset row 1", "first dataset row 2"],`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 10: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 11: `    extra_like = Dataset.from_dict(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 12: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 13: `            "id": [3, 4],`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `            "text": ["second dataset row 1", "second dataset row 2"],`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 16: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 18: `    combined_dataset = concatenate_datasets([train_like, extra_like])`
  Saves a value into `combined_dataset` so later lines can reuse it.
- Line 20: `    print("Dataset after concatenate_datasets")`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print(combined_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 23: `    print("Rows:", combined_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 27: `    main()`
  Calls `main()` to start the example.

## Notes

- This operation keeps row order unless you shuffle afterward.
