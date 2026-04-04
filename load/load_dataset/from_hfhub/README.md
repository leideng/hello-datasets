# load_dataset from_hfhub

Load a public dataset directly from Hugging Face Hub with `load_dataset(repo_id, ...)`.

## What It Teaches

- `load_dataset(...)` can download a dataset by Hub repository ID.
- You can request only a small slice such as `train[:3]` while learning.
- Hub-hosted datasets are one of the most common entry points for `datasets`.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_hfhub/main.py
```

## Expected Result

In a normal networked environment, the script:

- downloads a small public dataset sample
- prints the dataset summary, features, and rows

In a restricted environment, the script catches the failure and explains that Hub access is required.

## Notes

- This example intentionally uses a public dataset and a small split slice.
- If you work in an offline or sandboxed environment, this example may not be runnable until network access is available.
