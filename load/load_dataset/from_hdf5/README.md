# load_dataset from_hdf5

Load a local HDF5 file with `load_dataset("hdf5", ...)`.

## What It Teaches

- `datasets` includes a packaged HDF5 loader.
- Top-level HDF5 datasets can map naturally to dataset columns.
- HDF5 is useful when data is already stored in scientific or array-oriented pipelines.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_hdf5/main.py
```

## Expected Result

The script:

- creates a small local `.h5` file in `data/`
- loads it with `load_dataset`
- prints the inferred features and rows

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 3: `import h5py`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 4: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 7: `def write_hdf5_file(hdf5_file: Path) -> None:`
  Defines the function `write_hdf5_file` so the example logic is grouped into a named step.
- Line 8: `    hdf5_file.parent.mkdir(parents=True, exist_ok=True)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 10: `    with h5py.File(hdf5_file, "w") as handle:`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 11: `        handle.create_dataset("id", data=[1, 2, 3])`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 12: `        handle.create_dataset(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 13: `            "title",`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `            data=[`
  Starts a multi-line collection literal used by this example.
- Line 15: `                b"store columns in one hdf5 file",`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 16: `                b"load them with datasets",`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 17: `                b"inspect the inferred schema",`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 18: `            ],`
  Closes part of the sample data structure being built.
- Line 19: `        )`
  Continues the multi-line Python structure opened by the previous line.
- Line 20: `        handle.create_dataset("score", data=[0.9, 0.8, 0.95])`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 23: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 24: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so nearby `data/` and `.cache/` paths can be built relative to this file.
- Line 25: `    data_file = example_dir / "data" / "sample.h5"`
  Builds the path to a local input file used by the example.
- Line 26: `    cache_dir = example_dir / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 28: `    write_hdf5_file(data_file)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 30: `    dataset = load_dataset(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 31: `        "hdf5",`
  Provides one literal sample value used by the example data or configuration.
- Line 32: `        data_files=str(data_file),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 33: `        cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 34: `    )["train"]`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 36: `    print("Dataset loaded with load_dataset('hdf5', data_files=...)")`
  Prints information so you can observe what the dataset operation produced.
- Line 37: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 38: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 39: `    print("Features:", dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 40: `    print("Rows:", dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 43: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 44: `    main()`
  Calls `main()` to start the example.

## Notes

- All top-level datasets used as columns should have the same length.
- This example writes its own sample file to stay self-contained.
