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

## Notes

- Always set a seed in learning examples so output is stable.
