import polars as pl
from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "stage": ["raw", "processed", "validated"],
            "rows": [120, 95, 95],
        }
    )

    dataframe = pl.from_arrow(dataset.data.table)

    print("Dataset converted to a Polars DataFrame")
    print(dataset)
    print()
    print("Type:", type(dataframe))
    print(dataframe)


if __name__ == "__main__":
    main()
