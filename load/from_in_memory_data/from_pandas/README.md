# from_pandas

Create a Hugging Face `Dataset` from a Pandas DataFrame.

## What It Teaches

- `Dataset.from_pandas(...)` converts tabular in-memory data into a dataset.
- Pandas is convenient when data cleaning already happened in a DataFrame workflow.
- `preserve_index=False` avoids turning the DataFrame index into an extra dataset column.

## Run

From the repository root:

```bash
uv run python load/from_in_memory_data/from_pandas/main.py
```

## Expected Result

The script prints:

- a dataset summary
- the inferred feature schema
- one example row

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `import pandas as pd`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 2: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 5: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 6: `    dataframe = pd.DataFrame(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 7: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 8: `            "id": [1, 2, 3],`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `            "name": ["Ada", "Grace", "Linus"],`
  Provides one literal sample value used by the example data or configuration.
- Line 10: `            "score": [98.5, 97.0, 95.5],`
  Provides one literal sample value used by the example data or configuration.
- Line 11: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 12: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 14: `    dataset = Dataset.from_pandas(dataframe, preserve_index=False)`
  Converts a pandas DataFrame into a Hugging Face dataset.
- Line 16: `    print("Dataset created with Dataset.from_pandas")`
  Prints information so you can observe what the dataset operation produced.
- Line 17: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 18: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print("Features:", dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print("Second row:", dataset[1])`
  Prints information so you can observe what the dataset operation produced.
- Line 23: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 24: `    main()`
  Calls `main()` to start the example.

## Notes

- If you keep the index, it may appear as an extra column.
- This is a useful bridge when moving from Pandas-based exploration into `datasets`.
