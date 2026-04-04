from pathlib import Path

import pandas as pd
from datasets import load_dataset


def write_parquet_file(parquet_file: Path) -> None:
    parquet_file.parent.mkdir(parents=True, exist_ok=True)

    dataframe = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "task": [
                "write parquet locally",
                "load parquet with datasets",
                "inspect the resulting schema",
            ],
            "done": [True, True, False],
        }
    )
    dataframe.to_parquet(parquet_file, index=False)


def main() -> None:
    example_dir = Path(__file__).resolve().parent
    data_file = example_dir / "data" / "sample.parquet"
    cache_dir = example_dir / ".cache"

    write_parquet_file(data_file)

    dataset_dict = load_dataset(
        "parquet",
        data_files=str(data_file),
        cache_dir=str(cache_dir),
    )
    train_dataset = dataset_dict["train"]

    print("Dataset loaded with load_dataset('parquet', data_files=...)")
    print(dataset_dict)
    print()
    print("Features:", train_dataset.features)
    print("All rows:", train_dataset[:])


if __name__ == "__main__":
    main()
