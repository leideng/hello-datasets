# shard

Take one shard of a dataset with `Dataset.shard(...)`.

## What It Teaches

- Sharding splits a dataset into deterministic pieces by row position.
- It is useful for distributed work, chunked processing, or manual partitioning.
- `index` selects which shard to keep.

## Run

From the repository root:

```bash
uv run python process/shard/main.py
```

## Expected Result

The script prints:

- the selected shard summary
- only the rows that belong to shard `1` out of `3`

## Notes

- This is a structural partition, not a random split.
