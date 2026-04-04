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

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 3: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 6: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 7: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so nearby `data/` and `.cache/` paths can be built relative to this file.
- Line 8: `    data_file = example_dir / "data" / "sample.csv"`
  Builds the path to a local input file used by the example.
- Line 9: `    cache_dir = example_dir / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 10: `    file_url = data_file.resolve().as_uri()`
  Saves a value into `file_url` so later lines can reuse it.
- Line 12: `    dataset = load_dataset(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 13: `        "csv",`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `        data_files=file_url,`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 15: `        cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 16: `    )["train"]`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 18: `    print("Dataset loaded from a file:// URL")`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print("URL:", file_url)`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print("Features:", dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 23: `    print("Rows:", dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 27: `    main()`
  Calls `main()` to start the example.

## Notes

- This example is intentionally offline-friendly.
- If you replace the `file://` URL with an HTTP URL, the loading pattern is largely the same.
