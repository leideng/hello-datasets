# load_dataset from_hdf5

Load a local HDF5 file with `load_dataset("hdf5", ...)`.

## What It Teaches

- `datasets` includes a packaged HDF5 loader.
- Top-level HDF5 datasets can map naturally to dataset columns.
- HDF5 is useful when data is already stored in scientific or array-oriented pipelines.

## Run

From the repository root:

```bash
uv run python topics/01-load/load_dataset/from_hdf5/main.py
```

## Expected Result

The script:

- creates a small local `.h5` file in `data/`
- loads it with `load_dataset`
- prints the inferred features and rows

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 3: `import h5py`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 4: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 7: `def write_hdf5_file(hdf5_file: Path) -> None:`
  Defines `write_hdf5_file`, the function that groups one logical step of the example.
- Line 8: `    hdf5_file.parent.mkdir(parents=True, exist_ok=True)`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 10: `    with h5py.File(hdf5_file, "w") as handle:`
  Starts a context manager so temporary resources are created and cleaned up safely.
- Line 23: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 24: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so local `data/` and `.cache/` paths stay relative to this example.
- Line 25: `    data_file = example_dir / "data" / "sample.h5"`
  Builds the path to the local sample data used by the example.
- Line 26: `    cache_dir = example_dir / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 30: `    dataset = load_dataset(`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 43: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- All top-level datasets used as columns should have the same length.
- This example writes its own sample file to stay self-contained.
