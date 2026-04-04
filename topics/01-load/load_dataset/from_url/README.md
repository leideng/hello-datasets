# load_dataset from_url

Load data from a URL with `load_dataset(...)`.

## What It Teaches

- `data_files` can point to a URL instead of a plain local path.
- The same pattern works for remote HTTP URLs and local `file://` URLs.
- Using `file://` keeps this example runnable without external network access.

## Run

From the repository root:

```bash
uv run python topics/01-load/load_dataset/from_url/main.py
```

## Expected Result

The script:

- builds an absolute `file://` URL for the local sample CSV
- loads it through `load_dataset("csv", ...)`
- prints the resolved URL, schema, and loaded rows

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 3: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 6: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 7: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so local `data/` and `.cache/` paths stay relative to this example.
- Line 8: `    data_file = example_dir / "data" / "sample.csv"`
  Builds the path to the local sample data used by the example.
- Line 9: `    cache_dir = example_dir / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 12: `    dataset = load_dataset(`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 26: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This example is intentionally offline-friendly.
- If you replace the `file://` URL with an HTTP URL, the loading pattern is largely the same.
