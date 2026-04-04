# select

Pick specific row indices with `Dataset.select(...)`.

## What It Teaches

- `select` keeps rows by position.
- It is useful for slicing examples, debugging, or building small subsets.
- The selected indices are zero-based positions in the dataset.

## Run

From the repository root:

```bash
uv run python process/select/main.py
```

## Expected Result

The script prints:

- the selected dataset summary
- only rows `0`, `2`, and `4`

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
- Line 7: `            "id": [10, 11, 12, 13, 14],`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "text": [`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `                "zero-based row selection",`
  Provides one literal sample value used by the example data or configuration.
- Line 10: `                "select keeps explicit indices",`
  Provides one literal sample value used by the example data or configuration.
- Line 11: `                "this is the third row",`
  Provides one literal sample value used by the example data or configuration.
- Line 12: `                "this is the fourth row",`
  Provides one literal sample value used by the example data or configuration.
- Line 13: `                "this is the fifth row",`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `            ],`
  Closes part of the sample data structure being built.
- Line 15: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 16: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 18: `    selected_dataset = dataset.select([0, 2, 4])`
  Selects only specific row positions from the dataset.
- Line 20: `    print("Dataset after select")`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print(selected_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 23: `    print("Rows:", selected_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 27: `    main()`
  Calls `main()` to start the example.

## Notes

- `select` is different from `filter`: it uses explicit row indices instead of a predicate function.
