# interleave

Mix rows from multiple datasets with `interleave_datasets(...)`.

## What It Teaches

- Interleaving alternates examples from multiple datasets.
- This is useful when mixing sources or balancing data streams.
- `stopping_strategy` controls how the function behaves when datasets have different lengths.

## Run

From the repository root:

```bash
uv run python process/interleave/src/main.py
```

## Expected Result

The script prints:

- the interleaved dataset summary
- rows alternating between the two sources

## Notes

- `all_exhausted` continues until every input dataset is exhausted.
