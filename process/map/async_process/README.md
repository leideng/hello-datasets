# async_process

Use an async mapping function with `Dataset.map(...)`.

## What It Teaches

- `map` can work with an async function in modern `datasets`.
- Async functions are useful when each batch needs cooperative I/O or async preprocessing.
- The function still returns normal dataset columns.

## Run

From the repository root:

```bash
uv run python process/map/async_process/main.py
```

## Expected Result

The script prints:

- the transformed dataset summary
- rows with a derived `normalized` column

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `import asyncio`
  Imports Python's async support so the example can define and run asynchronous code.
- Line 3: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 6: `async def normalize_batch(batch: dict[str, list]) -> dict[str, list]:`
  Defines the async helper function `normalize_batch` used later in the example.
- Line 7: `    await asyncio.sleep(0)`
  Waits for an async operation to finish before continuing.
- Line 8: `    return {`
  Returns the computed value back to the caller.
- Line 9: `        "normalized": [text.lower().replace(" ", "_") for text in batch["text"]]`
  Provides one literal sample value used by the example data or configuration.
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
- Line 17: `            "text": [`
  Provides one literal sample value used by the example data or configuration.
- Line 18: `                "Async Map Example",`
  Provides one literal sample value used by the example data or configuration.
- Line 19: `                "Normalize Retrieved Text",`
  Provides one literal sample value used by the example data or configuration.
- Line 20: `                "Keep The Example Small",`
  Provides one literal sample value used by the example data or configuration.
- Line 21: `            ],`
  Closes part of the sample data structure being built.
- Line 22: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 23: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 25: `    mapped_dataset = dataset.map(normalize_batch, batched=True)`
  Applies `map(...)` to create a transformed version of the dataset.
- Line 27: `    print("Dataset after async batched map")`
  Prints information so you can observe what the dataset operation produced.
- Line 28: `    print(mapped_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 29: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 30: `    print("Rows:", mapped_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 33: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 34: `    main()`
  Calls `main()` to start the example.

## Notes

- This example uses `await asyncio.sleep(0)` to keep the async behavior visible without external I/O.
