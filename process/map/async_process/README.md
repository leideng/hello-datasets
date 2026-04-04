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

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `import asyncio`
  Imports Python's async support so the example can define asynchronous preprocessing logic.
- Line 3: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 6: `async def normalize_batch(batch: dict[str, list]) -> dict[str, list]:`
  Defines async helper `normalize_batch`, which is later passed into the dataset workflow.
- Line 7: `    await asyncio.sleep(0)`
  Shows where the async function yields control before continuing its work.
- Line 8: `    return {`
  Returns the transformed value that the dataset API will store or use next.
- Line 13: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 14: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 25: `    mapped_dataset = dataset.map(normalize_batch, batched=True)`
  Applies `map(...)` to create transformed columns or rows from the original dataset.
- Line 33: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This example uses `await asyncio.sleep(0)` to keep the async behavior visible without external I/O.
