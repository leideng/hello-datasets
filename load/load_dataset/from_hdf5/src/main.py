from pathlib import Path

import h5py
from datasets import load_dataset


def write_hdf5_file(hdf5_file: Path) -> None:
    hdf5_file.parent.mkdir(parents=True, exist_ok=True)

    with h5py.File(hdf5_file, "w") as handle:
        handle.create_dataset("id", data=[1, 2, 3])
        handle.create_dataset(
            "title",
            data=[
                b"store columns in one hdf5 file",
                b"load them with datasets",
                b"inspect the inferred schema",
            ],
        )
        handle.create_dataset("score", data=[0.9, 0.8, 0.95])


def main() -> None:
    example_dir = Path(__file__).resolve().parent.parent
    data_file = example_dir / "data" / "sample.h5"
    cache_dir = example_dir / ".cache"

    write_hdf5_file(data_file)

    dataset = load_dataset(
        "hdf5",
        data_files=str(data_file),
        cache_dir=str(cache_dir),
    )["train"]

    print("Dataset loaded with load_dataset('hdf5', data_files=...)")
    print(dataset)
    print()
    print("Features:", dataset.features)
    print("Rows:", dataset[:])


if __name__ == "__main__":
    main()
