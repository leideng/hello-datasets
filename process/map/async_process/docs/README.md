# async_process

Use an async mapping function with `Dataset.map(...)`.

## What It Teaches

- `map` can work with an async function in modern `datasets`.
- Async functions are useful when each batch needs cooperative I/O or async preprocessing.
- The function still returns normal dataset columns.

## Run

From the repository root:

```bash
uv run python process/map/async_process/src/main.py
```

## Expected Result

The script prints:

- the transformed dataset summary
- rows with a derived `normalized` column

## Notes

- This example uses `await asyncio.sleep(0)` to keep the async behavior visible without external I/O.
