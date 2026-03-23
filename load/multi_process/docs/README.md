# multi_process

Load local files with multiple worker processes using `num_proc`.

## What It Teaches

- Some dataset loading workflows can use multiple processes.
- `num_proc` is useful when many local files need to be parsed.
- A multi-file input pattern is common for sharded datasets.

## Run

From the repository root:

```bash
uv run python load/multi_process/src/main.py
```

## Expected Result

The script:

- loads two local JSON Lines shards
- requests `num_proc=2`
- prints the combined dataset rows

## Notes

- This example keeps the data tiny so the multiprocessing behavior is easy to understand.
- On very small inputs, multiprocessing may add overhead instead of improving total runtime.
- In restricted sandboxes, multiprocessing may be blocked. This example falls back to `num_proc=1` and prints that it did so.
