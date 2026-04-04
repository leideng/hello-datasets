# load_dataset from_url

Load data from a URL with `load_dataset(...)`.

## What It Teaches

- `data_files` can point to a URL instead of a plain local path.
- The same pattern works for remote HTTP URLs and local `file://` URLs.
- Using `file://` keeps this example runnable without external network access.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_url/main.py
```

## Expected Result

The script:

- builds an absolute `file://` URL for the local sample CSV
- loads it through `load_dataset("csv", ...)`
- prints the resolved URL, schema, and loaded rows

## Notes

- This example is intentionally offline-friendly.
- If you replace the `file://` URL with an HTTP URL, the loading pattern is largely the same.
