# hello-datasets

Learning repository for efficient, example-driven use of Hugging Face `datasets`.

This repo uses a single root `pyproject.toml` managed by `uv`. Each topic folder is intended to stay minimal and self-contained, with runnable code and its learning-oriented `README.md` placed directly in the example root. Local sample data stays in `data/` when needed.

## Topic Tree

The current repository topic structure is:

```text
hello-datasets/
  config/
    get_dataset_config_names/
  create/
  export/
    to_csv/
    to_json/
    to_parquet/
    to_sql/
  load/
    from_in_memory_data/
      from_dict/
      from_generator/
      from_list/
      from_pandas/
    from_sql/
    load_dataset/
      from_arrow/
      from_csv/
      from_hdf5/
      from_hfhub/
      from_json/
      from_lance/
      from_parquet/
      from_url/
      from_webdataset/
    multi_process/
  preprocess/
  process/
    batch/
    cast/
    concatenate/
    filter/
    flatten/
    format/
      custom_format/
      tabular_format/
        arrow/
        pandas/
        polars/
      tensor_format/
        jax/
        numpy/
        tensorflow/
        torch/
    interleave/
    map/
      async_process/
      batch_process/
      data_augmentation/
      distributed_usage/
      multi_process/
      multi_split_process/
    remove/
    rename/
    select/
    shard/
    shuffle/
    sort/
    split/
  read/
  share/
  stream/
  table/
  tokenize/
```

## Topic Notes

- `load/` focuses on dataset ingestion from local files, in-memory objects, URLs, Hugging Face Hub, SQL, and multiprocessing-related loading workflows.
- `process/` focuses on transformations such as `map`, `filter`, formatting, splitting, concatenation, sharding, batching, and feature casting.
- `export/` focuses on persisting datasets to common file and storage formats.
- `config/` covers configuration discovery helpers.
- `create/`, `preprocess/`, `read/`, `share/`, `stream/`, `table/`, and `tokenize/` are reserved for focused examples in those areas.

## Repository Conventions

- Dependencies are managed globally from the root with `uv`.
- New work should largely follow the existing topic tree above.
- It is acceptable to refine or extend the tree when a topic boundary is unclear.
- Each concrete example should live in the relevant topic folder and should eventually include:
  - `main.py` or another small root-level Python file
  - a root-level `README.md` for how to run it and what it teaches
  - optional `data/` for local sample inputs or test data

## Run

Once examples are added, prefer `uv run` from the repository root with explicit module or script paths documented in each example's `README.md`.
