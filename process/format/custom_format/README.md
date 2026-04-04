# custom_format

Apply a custom retrieval-time transform with `with_transform(...)`.

## What It Teaches

- A dataset can transform rows when you read them, without rewriting the stored data.
- `with_transform(...)` is useful for presentation logic or lightweight preprocessing.
- The transform runs on retrieved batches rather than permanently changing the dataset.

## Run

From the repository root:

```bash
uv run python process/format/custom_format/main.py
```

## Expected Result

The script prints:

- the transformed dataset summary
- one transformed item
- a transformed slice

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def build_preview(batch: dict[str, list]) -> dict[str, list]:`
  Defines the function `build_preview` so the example logic is grouped into a named step.
- Line 5: `    return {`
  Returns the computed value back to the caller.
- Line 6: `        "preview": [`
  Provides one literal sample value used by the example data or configuration.
- Line 7: `            f"[{identifier}] {text.upper()}"`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 8: `            for identifier, text in zip(batch["id"], batch["text"])`
  Starts a loop that repeats the same operation for each item in a collection.
- Line 9: `        ]`
  Continues the multi-line Python structure opened by the previous line.
- Line 10: `    }`
  Continues the multi-line Python structure opened by the previous line.
- Line 13: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 14: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 15: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 16: `            "id": [1, 2, 3],`
  Provides one literal sample value used by the example data or configuration.
- Line 17: `            "text": ["custom formatter", "returns derived values", "works on retrieval"],`
  Provides one literal sample value used by the example data or configuration.
- Line 18: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 19: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 21: `    formatted_dataset = dataset.with_transform(build_preview)`
  Saves a value into `formatted_dataset` so later lines can reuse it.
- Line 23: `    print("Dataset with a custom retrieval transform")`
  Prints information so you can observe what the dataset operation produced.
- Line 24: `    print(formatted_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 25: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `    print("Item 0:", formatted_dataset[0])`
  Prints information so you can observe what the dataset operation produced.
- Line 27: `    print("Items 0:2:", formatted_dataset[:2])`
  Prints information so you can observe what the dataset operation produced.
- Line 30: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 31: `    main()`
  Calls `main()` to start the example.

## Notes

- This is different from `map`, which creates a new dataset with stored transformed columns.
