import pyarrow as pa
from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "title": ["arrow view", "columnar table", "zero-copy friendly"],
            "score": [0.8, 0.95, 0.88],
        }
    )

    arrow_table = dataset.data.table

    print("Dataset as an Arrow table")
    print(dataset)
    print()
    print("Type:", type(arrow_table))
    print("Schema:", arrow_table.schema)
    print("Pylist:", arrow_table.to_pylist())


if __name__ == "__main__":
    main()
