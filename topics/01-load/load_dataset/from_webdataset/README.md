# load_dataset from_webdataset

Load a local tar shard in WebDataset format with `load_dataset("webdataset", ...)`.

## What It Teaches

- WebDataset stores one example across multiple files that share the same prefix.
- File extensions become dataset fields such as `txt` or `json`.
- A tar archive is enough for a minimal local example.

## Run

From the repository root:

```bash
uv run python topics/01-load/load_dataset/from_webdataset/main.py
```

## Expected Result

The script:

- creates a local tar shard in WebDataset format
- loads it with the packaged `webdataset` loader
- prints the inferred features and first example

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `import io`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 2: `import json`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 3: `import tarfile`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 4: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 6: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 9: `def write_webdataset_tar(tar_file: Path) -> None:`
  Defines `write_webdataset_tar`, the function that groups one logical step of the example.
- Line 10: `    tar_file.parent.mkdir(parents=True, exist_ok=True)`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 25: `    with tarfile.open(tar_file, "w") as archive:`
  Starts a context manager so temporary resources are created and cleaned up safely.
- Line 26: `        for key, text, metadata in examples:`
  Loops over example items to build or transform the dataset input.
- Line 38: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 39: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so local `data/` and `.cache/` paths stay relative to this example.
- Line 40: `    data_file = example_dir / "data" / "sample.tar"`
  Builds the path to the local sample data used by the example.
- Line 41: `    cache_dir = example_dir / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 45: `    dataset = load_dataset(`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 58: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- Files such as `sample-0001.txt` and `sample-0001.json` are grouped into one example.
- This example uses text and JSON fields because they decode cleanly without optional media dependencies.
