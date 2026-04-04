# multi_process

Use `num_proc` with `map(...)` for process-based parallel preprocessing.

## What It Teaches

- `num_proc` can distribute a mapping workload across multiple worker processes.
- This is useful for heavier CPU-bound transforms on larger datasets.
- Some restricted environments block local multiprocessing primitives.

## Run

From the repository root:

```bash
uv run python process/map/multi_process/main.py
```

## Expected Result

The script prints:

- whether it ran in parallel or used a fallback
- the transformed dataset
- rows with a derived `length` column

## Notes

- In sandboxes that block process management, the example falls back to plain `map(...)` without `num_proc`.
