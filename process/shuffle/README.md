# shuffle

Randomize row order with `Dataset.shuffle(...)`.

## What It Teaches

- `shuffle` changes row order without changing row contents.
- Providing a fixed `seed` makes the result reproducible.
- Reproducibility matters for debugging and experiments.

## Run

From the repository root:

```bash
uv run python process/shuffle/main.py
```

## Expected Result

The script prints:

- the shuffled dataset summary
- the rows in deterministic shuffled order

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
- Line 7: `            "id": [1, 2, 3, 4, 5],`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "text": [`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `                "first",`
  Provides one literal sample value used by the example data or configuration.
- Line 10: `                "second",`
  Provides one literal sample value used by the example data or configuration.
- Line 11: `                "third",`
  Provides one literal sample value used by the example data or configuration.
- Line 12: `                "fourth",`
  Provides one literal sample value used by the example data or configuration.
- Line 13: `                "fifth",`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `            ],`
  Closes part of the sample data structure being built.
- Line 15: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 16: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 18: `    shuffled_dataset = dataset.shuffle(seed=7)`
  Randomly reorders the rows to demonstrate dataset shuffling.
- Line 20: `    print("Dataset after shuffle")`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print(shuffled_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 23: `    print("Rows:", shuffled_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 27: `    main()`
  Calls `main()` to start the example.

## Notes

- Always set a seed in learning examples so output is stable.
