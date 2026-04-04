# hello-datasets

Learning repository for efficient, example-driven use of Hugging Face `datasets`.

This repo uses a single root `pyproject.toml` managed by `uv`. Each topic folder is intended to stay minimal and self-contained, with runnable code and its learning-oriented `README.md` placed directly in the example root. Local sample data stays in `data/` when needed.

## Table of Contents

- [Curriculum Manifest](#curriculum-manifest)
- [Topic Tree](#topic-tree)
- [Topic Notes](#topic-notes)
- [Repository Conventions](#repository-conventions)
- [Run](#run)

## Curriculum Manifest

The repository root contains [topics.yaml](/home/leo/code/hello-datasets/topics.yaml), which is the machine-readable curriculum guide for later agent automation.

- It is aligned to the official Hugging Face `datasets` docs index.
- It currently tracks 10 top-level curriculum sections and 88 project entries.
- The current top-level sections are: Get Started, Tutorials, General Usage, Audio, Vision, Text, Tabular, Dataset Repository, Conceptual Guides, Reference.
- Existing examples are marked `ready`; planned curriculum placeholders are marked `planned`.

## Topic Tree

The current repository structure below is generated from the filesystem in tree-style format.

```text
.
├── audio/
│   ├── create_audio_dataset/
│   │   └── .gitkeep
│   ├── load_audio_data/
│   │   └── .gitkeep
│   └── process_audio_data/
│       └── .gitkeep
├── concepts/
│   ├── batch_mapping/
│   │   └── .gitkeep
│   ├── build_and_load/
│   │   └── .gitkeep
│   ├── dataset_features/
│   │   └── .gitkeep
│   ├── dataset_or_iterable_dataset/
│   │   └── .gitkeep
│   ├── datasets_and_arrow/
│   │   └── .gitkeep
│   └── the_cache/
│       └── .gitkeep
├── config/
│   ├── cache_management/
│   │   └── .gitkeep
│   ├── cli/
│   │   └── .gitkeep
│   ├── get_dataset_config_names/
│   └── troubleshooting/
│       └── .gitkeep
├── create/
├── export/
│   ├── to_csv/
│   ├── to_json/
│   ├── to_parquet/
│   └── to_sql/
├── getting_started/
│   ├── installation/
│   │   └── .gitkeep
│   └── quickstart/
│       └── .gitkeep
├── load/
│   ├── cloud_storage/
│   │   └── .gitkeep
│   ├── from_in_memory_data/
│   │   ├── from_dict/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── from_generator/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── from_list/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   └── from_pandas/
│   │       ├── README.md
│   │       └── main.py
│   ├── from_sql/
│   │   ├── data/
│   │   │   └── sample.sqlite
│   │   ├── README.md
│   │   └── main.py
│   ├── load_dataset/
│   │   ├── from_arrow/
│   │   │   ├── data/
│   │   │   │   └── sample.arrow
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── from_csv/
│   │   │   ├── data/
│   │   │   │   └── sample.csv
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── from_hdf5/
│   │   │   ├── data/
│   │   │   │   └── sample.h5
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── from_hfhub/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── from_json/
│   │   │   ├── data/
│   │   │   │   └── sample.jsonl
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── from_lance/
│   │   ├── from_parquet/
│   │   │   ├── data/
│   │   │   │   └── sample.parquet
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── from_url/
│   │   │   ├── data/
│   │   │   │   └── sample.csv
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   └── from_webdataset/
│   │       ├── data/
│   │       │   └── sample.tar
│   │       ├── README.md
│   │       └── main.py
│   ├── multi_process/
│   │   ├── data/
│   │   │   ├── part-1.jsonl
│   │   │   └── part-2.jsonl
│   │   ├── README.md
│   │   └── main.py
│   └── overview/
│       └── .gitkeep
├── preprocess/
├── process/
│   ├── batch/
│   │   ├── README.md
│   │   └── main.py
│   ├── cast/
│   │   ├── README.md
│   │   └── main.py
│   ├── concatenate/
│   │   ├── README.md
│   │   └── main.py
│   ├── filter/
│   │   ├── README.md
│   │   └── main.py
│   ├── flatten/
│   │   ├── README.md
│   │   └── main.py
│   ├── format/
│   │   ├── custom_format/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── tabular_format/
│   │   │   ├── arrow/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── pandas/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   ├── polars/
│   │   │   │   ├── README.md
│   │   │   │   └── main.py
│   │   │   └── spark/
│   │   │       └── .gitkeep
│   │   └── tensor_format/
│   │       ├── jax/
│   │       │   ├── README.md
│   │       │   └── main.py
│   │       ├── numpy/
│   │       │   ├── README.md
│   │       │   └── main.py
│   │       ├── tensorflow/
│   │       │   ├── README.md
│   │       │   └── main.py
│   │       └── torch/
│   │           ├── README.md
│   │           └── main.py
│   ├── interleave/
│   │   ├── README.md
│   │   └── main.py
│   ├── map/
│   │   ├── async_process/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── batch_process/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── data_augmentation/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── distributed_usage/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   ├── multi_process/
│   │   │   ├── README.md
│   │   │   └── main.py
│   │   └── multi_split_process/
│   │       ├── README.md
│   │       └── main.py
│   ├── overview/
│   │   └── .gitkeep
│   ├── remove/
│   │   ├── README.md
│   │   └── main.py
│   ├── rename/
│   │   ├── README.md
│   │   └── main.py
│   ├── select/
│   │   ├── README.md
│   │   └── main.py
│   ├── shard/
│   │   ├── README.md
│   │   └── main.py
│   ├── shuffle/
│   │   ├── README.md
│   │   └── main.py
│   ├── sort/
│   │   ├── README.md
│   │   └── main.py
│   └── split/
│       ├── README.md
│       └── main.py
├── read/
├── reference/
│   ├── builder_classes/
│   │   └── .gitkeep
│   ├── loading_methods/
│   │   └── .gitkeep
│   ├── main_classes/
│   │   └── .gitkeep
│   ├── table_classes/
│   │   └── .gitkeep
│   └── utilities/
│       └── .gitkeep
├── share/
│   ├── create_dataset_card/
│   │   └── .gitkeep
│   ├── share_dataset_repository/
│   │   └── .gitkeep
│   ├── share_dataset_to_hub/
│   │   └── .gitkeep
│   └── structure_repository/
│       └── .gitkeep
├── stream/
│   └── overview/
│       └── .gitkeep
├── table/
│   └── search_index/
│       └── .gitkeep
├── tabular/
│   └── load_tabular_data/
│       └── .gitkeep
├── text/
│   ├── load_text_data/
│   │   └── .gitkeep
│   └── process_text_data/
│       └── .gitkeep
├── tokenize/
├── tutorials/
│   ├── know_your_dataset/
│   │   └── .gitkeep
│   ├── overview/
│   │   └── .gitkeep
│   └── preprocess/
│       └── .gitkeep
├── vision/
│   ├── create_document_dataset/
│   │   └── .gitkeep
│   ├── create_image_dataset/
│   │   └── .gitkeep
│   ├── create_medical_imaging_dataset/
│   │   └── .gitkeep
│   ├── create_video_dataset/
│   │   └── .gitkeep
│   ├── depth_estimation/
│   │   └── .gitkeep
│   ├── image_classification/
│   │   └── .gitkeep
│   ├── load_document_data/
│   │   └── .gitkeep
│   ├── load_image_data/
│   │   └── .gitkeep
│   ├── load_video_data/
│   │   └── .gitkeep
│   ├── object_detection/
│   │   └── .gitkeep
│   ├── process_image_data/
│   │   └── .gitkeep
│   └── semantic_segmentation/
│       └── .gitkeep
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
- `getting_started/` and `tutorials/` track beginner onboarding flows derived from the official docs structure.
- `load/` focuses on dataset ingestion from local files, in-memory objects, URLs, Hugging Face Hub, SQL, and multiprocessing-related loading workflows.
- `process/` focuses on transformations such as `map`, `filter`, formatting, splitting, concatenation, sharding, batching, and feature casting.
- `audio/`, `vision/`, `text/`, and `tabular/` reserve modality-specific examples that align with the official how-to guides.
- `share/`, `stream/`, `table/`, `concepts/`, and `reference/` reserve curriculum areas for publishing, streaming, indexing, conceptual explanations, and API-oriented reference examples.
- Some folders currently contain only `.gitkeep` placeholders because they are planned curriculum entries, not implemented examples yet.

## Repository Conventions

- Dependencies are managed globally from the root with `uv`.
- New work should follow both the current filesystem tree and `topics.yaml`.
- It is acceptable to refine or extend the tree when a topic boundary is unclear, but `topics.yaml`, `README.md`, and the folder structure should stay consistent with each other.
- Each concrete example should live in the relevant topic folder and should eventually include:
  - `main.py` or another small root-level Python file
  - a root-level `README.md` for how to run it and what it teaches
  - optional `data/` for local sample inputs or test data
- Planned curriculum folders may exist with only a `.gitkeep` until the actual example is implemented.

## Run

Once examples are added, prefer `uv run` from the repository root with explicit module or script paths documented in each example's `README.md`.
