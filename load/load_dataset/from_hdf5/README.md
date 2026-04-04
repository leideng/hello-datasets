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

## Notes

- All top-level datasets used as columns should have the same length.
- This example writes its own sample file to stay self-contained.
