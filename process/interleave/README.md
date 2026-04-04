# interleave

Mix rows from multiple datasets with `interleave_datasets(...)`.

## What It Teaches

- Interleaving alternates examples from multiple datasets.
- This is useful when mixing sources or balancing data streams.
- `stopping_strategy` controls how the function behaves when datasets have different lengths.

## Run

From the repository root:

```bash
uv run python process/interleave/main.py
```

## Expected Result

The script prints:

- the interleaved dataset summary
- rows alternating between the two sources

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset, interleave_datasets`
  Imports `Dataset, interleave_datasets` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 5: `    first_dataset = Dataset.from_dict(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 6: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 7: `            "source": ["tips", "tips", "tips"],`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "text": ["tip-1", "tip-2", "tip-3"],`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 10: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 11: `    second_dataset = Dataset.from_dict(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 12: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 13: `            "source": ["examples", "examples"],`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `            "text": ["example-1", "example-2"],`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 16: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 18: `    interleaved_dataset = interleave_datasets([first_dataset, second_dataset], stopping_strategy="all_exhausted")`
  Saves a value into `interleaved_dataset` so later lines can reuse it.
- Line 20: `    print("Dataset after interleave_datasets")`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print(interleaved_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 23: `    print("Rows:", interleaved_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 27: `    main()`
  Calls `main()` to start the example.

## Notes

- `all_exhausted` continues until every input dataset is exhausted.
