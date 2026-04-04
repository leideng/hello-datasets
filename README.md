# hello-datasets

Learning repository for efficient, example-driven use of Hugging Face `datasets`.

This repo uses a single root `pyproject.toml` managed by `uv`. The curriculum now follows the official Hugging Face `datasets` General usage guides, and each first-level curriculum section lives under `topics/` with a slugged name such as `topics/01-load/` or `topics/11-cli/`. Concrete runnable examples stay minimal and self-contained, with code and learning-oriented `README.md` files placed directly in each example root. Local sample data stays in `data/` when needed.

## Table of Contents

- [Curriculum Manifest](#curriculum-manifest)
- [Topic Tree](#topic-tree)
- [Topic Notes](#topic-notes)
- [Repository Conventions](#repository-conventions)
- [Run](#run)

## Curriculum Manifest

The repository root contains [topics.yaml](/home/leo/code/hello-datasets/topics.yaml), which is the machine-readable curriculum guide for later agent automation.

- It is aligned to the official Hugging Face `datasets` General usage docs structure.
- It currently tracks 11 top-level curriculum sections and 50 project entries.
- The current top-level sections are: Load, Process, Stream, Use With PyTorch, Use With NumPy, Use With Pandas, Use With PyArrow, Cache Management, Cloud Storage, Search Index, CLI.
- Existing examples are marked `ready`; planned curriculum placeholders are marked `planned`.

## Topic Tree

The current repository structure below is generated from the filesystem in tree-style format.

```text
.
├── config/
│   ├── get_dataset_config_names/
│   └── troubleshooting/
│       └── .gitkeep
├── create/
├── export/
│   ├── to_csv/
│   ├── to_json/
│   ├── to_parquet/
│   └── to_sql/
├── preprocess/
├── read/
├── tokenize/
├── topics/
│   ├── 01-load/
│   │   ├── from_in_memory_data/
│   │   │   ├── from_dict/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── from_generator/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── from_list/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   └── from_pandas/
│   │   │       ├── README.md
│   │   │       └── main.py
│   │   ├── from_sql/
│   │   │   ├── data/
│   │   │   │   └── sample.sqlite
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── load_dataset/
│   │   │   ├── from_arrow/
│   │   │   │   ├── data/
│   │   │   │   │   └── sample.arrow
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── from_csv/
│   │   │   │   ├── data/
│   │   │   │   │   └── sample.csv
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── from_hdf5/
│   │   │   │   ├── data/
│   │   │   │   │   └── sample.h5
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── from_hfhub/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── from_json/
│   │   │   │   ├── data/
│   │   │   │   │   └── sample.jsonl
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── from_lance/
│   │   │   ├── from_parquet/
│   │   │   │   ├── data/
│   │   │   │   │   └── sample.parquet
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── from_url/
│   │   │   │   ├── data/
│   │   │   │   │   └── sample.csv
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   └── from_webdataset/
│   │   │       ├── data/
│   │   │       │   └── sample.tar
│   │   │       ├── README.md
│   │   │       └── main.py
│   │   ├── multi_process/
│   │   │   ├── data/
│   │   │   │   ├── part-1.jsonl
│   │   │   │   └── part-2.jsonl
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   └── overview/
│   │       ├── data/
│   │       │   └── sample.jsonl
│   │       ├── README.md
│   │       └── main.py
│   ├── 02-process/
│   │   ├── batch/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── cast/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── concatenate/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── filter/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── flatten/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── format/
│   │   │   ├── custom_format/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── tabular_format/
│   │   │   │   ├── polars/
│   │   │   │   │   ├── README.md
│   │   │   │   │   └── main.py
│   │   │   │   └── spark/
│   │   │   │       └── .gitkeep
│   │   │   └── tensor_format/
│   │   │       ├── jax/
│   │   │       │   ├── README.md
│   │   │       │   └── main.py
│   │   │       └── tensorflow/
│   │   │           ├── README.md
│   │   │           └── main.py
│   │   ├── interleave/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── map/
│   │   │   ├── async_process/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── batch_process/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── data_augmentation/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── distributed_usage/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── multi_process/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   └── multi_split_process/
│   │   │       ├── README.md
│   │   │       └── main.py
│   │   ├── overview/
│   │   │   └── .gitkeep
│   │   ├── remove/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── rename/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── select/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── shard/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── shuffle/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── sort/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   └── split/
│   │       ├── README.md
│   │       └── main.py
│   ├── 03-stream/
│   │   └── overview/
│   │       └── .gitkeep
│   ├── 04-use-with-pytorch/
│   │   └── torch/
│   │       ├── README.md
│   │       └── main.py
│   ├── 05-use-with-numpy/
│   │   └── numpy/
│   │       ├── README.md
│   │       └── main.py
│   ├── 06-use-with-pandas/
│   │   └── pandas/
│   │       ├── README.md
│   │       └── main.py
│   ├── 07-use-with-pyarrow/
│   │   └── arrow/
│   │       ├── README.md
│   │       └── main.py
│   ├── 08-cache-management/
│   │   └── cache_management/
│   │       └── .gitkeep
│   ├── 09-cloud-storage/
│   │   └── cloud_storage/
│   │       └── .gitkeep
│   ├── 10-search-index/
│   │   └── search_index/
│   │       └── .gitkeep
│   └── 11-cli/
│       └── cli/
│           └── .gitkeep
├── .gitattributes
├── .gitignore
├── .python-version
├── AGENTS.md
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
├── topics.yaml
└── uv.lock
```

## Topic Notes

- `topics.yaml` is the canonical curriculum manifest for future agent automation and long-term coverage planning.
- `topics/01-load/` follows the official [Load](https://huggingface.co/docs/datasets/en/loading) guide and holds loading workflows such as `Dataset.from_*`, local file formats, Hub loading, and multi-file loading.
- `topics/02-process/` follows the official [Process](https://huggingface.co/docs/datasets/en/process) guide and holds transformation workflows such as `map`, `filter`, `select`, formatting, splitting, concatenation, and schema changes.
- `topics/03-stream/` through `topics/11-cli/` follow the remaining official General usage guides for streaming, framework/dataframe integration, cache management, cloud storage, search indexes, and the CLI.
- `config/` currently keeps ancillary placeholders such as `get_dataset_config_names/` and `troubleshooting/` that are not part of the current 11-topic General usage curriculum.
- Some folders currently contain only `.gitkeep` placeholders because they are planned curriculum entries, not implemented examples yet.

## Repository Conventions

- Dependencies are managed globally from the root with `uv`.
- New work should follow `topics.yaml` and the `topics/` tree first.
- Each first-level curriculum section under `topics/` should correspond to one official Hugging Face `datasets` General usage page.
- Each concrete example should live in the relevant topic folder and should eventually include:
  - `main.py` or another small root-level Python file
  - a root-level `README.md` for how to run it and what it teaches
  - optional `data/` for local sample inputs or test data
- Planned curriculum folders may exist with only a `.gitkeep` until the actual example is implemented.

## Run

Prefer `uv run` from the repository root with explicit script paths documented in each example `README.md`, for example `uv run python topics/01-load/from_sql/main.py`.
