# distributed_usage

Use sharding plus `map(...)` as a simple distributed preprocessing pattern.

## What It Teaches

- A common distributed pattern is to shard a dataset by worker or rank.
- Each worker can map over its own shard independently.
- This keeps preprocessing logic deterministic and easy to reason about.

## Run

From the repository root:

```bash
uv run python process/map/distributed_usage/main.py
```

## Expected Result

The script prints:

- the rows handled by simulated rank `0`
- the rows handled by simulated rank `1`

## Notes

- This example simulates distributed preprocessing locally without needing a real multi-node setup.
