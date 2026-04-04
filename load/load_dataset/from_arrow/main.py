from pathlib import Path

import pyarrow as pa
from datasets import load_dataset


def write_arrow_file(arrow_file: Path) -> None:
    arrow_file.parent.mkdir(parents=True, exist_ok=True)

    table = pa.table(
        {
            "id": [1, 2, 3],
            "topic": ["arrow", "ipc", "datasets"],
            "difficulty": ["medium", "medium", "easy"],
        }
    )

    with pa.OSFile(str(arrow_file), "wb") as sink:
        with pa.ipc.new_file(sink, table.schema) as writer:
            writer.write_table(table)


def main() -> None:
    example_dir = Path(__file__).resolve().parent
    data_file = example_dir / "data" / "sample.arrow"
    cache_dir = example_dir / ".cache"

    write_arrow_file(data_file)

    dataset_dict = load_dataset(
        "arrow",
        data_files=str(data_file),
        cache_dir=str(cache_dir),
    )
    train_dataset = dataset_dict["train"]

    print("Dataset loaded with load_dataset('arrow', data_files=...)")
    print(dataset_dict)
    print()
    print("Features:", train_dataset.features)
    print("Row 0:", train_dataset[0])


if __name__ == "__main__":
    main()
