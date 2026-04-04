# data_augmentation

Use `map` to expand a dataset with augmented examples.

## What It Teaches

- Batched `map` can change the number of rows when used for augmentation.
- One input example can produce multiple output examples.
- This pattern is common for text normalization, paraphrasing, or synthetic variants.

## Run

From the repository root:

```bash
uv run python process/map/data_augmentation/main.py
```

## Expected Result

The script prints:

- a larger dataset than the input
- both original and augmented rows

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def augment_batch(batch: dict[str, list]) -> dict[str, list]:`
  Defines the function `augment_batch` so the example logic is grouped into a named step.
- Line 5: `    augmented_text = []`
  Saves a value into `augmented_text` so later lines can reuse it.
- Line 6: `    augmented_variant = []`
  Saves a value into `augmented_variant` so later lines can reuse it.
- Line 8: `    for text in batch["text"]:`
  Starts a loop that repeats the same operation for each item in a collection.
- Line 9: `        augmented_text.extend([text, text.upper()])`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 10: `        augmented_variant.extend(["original", "uppercase"])`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 12: `    return {`
  Returns the computed value back to the caller.
- Line 13: `        "text": augmented_text,`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `        "variant": augmented_variant,`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `    }`
  Continues the multi-line Python structure opened by the previous line.
- Line 18: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 19: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 20: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 21: `            "text": [`
  Provides one literal sample value used by the example data or configuration.
- Line 22: `                "small examples are easier to inspect",`
  Provides one literal sample value used by the example data or configuration.
- Line 23: `                "augmentation can increase row count",`
  Provides one literal sample value used by the example data or configuration.
- Line 24: `            ]`
  Continues the multi-line Python structure opened by the previous line.
- Line 25: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 26: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 28: `    augmented_dataset = dataset.map(augment_batch, batched=True, remove_columns=["text"])`
  Stores the result of a dataset operation so the next lines can inspect it.
- Line 30: `    print("Dataset after augmentation-style map")`
  Prints information so you can observe what the dataset operation produced.
- Line 31: `    print(augmented_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 32: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 33: `    print("Rows:", augmented_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 36: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 37: `    main()`
  Calls `main()` to start the example.

## Notes

- When output row counts change, return lists whose lengths match the new number of rows.
