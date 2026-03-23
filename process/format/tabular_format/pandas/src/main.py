import pandas as pd
from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "topic": ["pandas output", "tabular analysis", "dataframe workflow"],
            "done": [True, False, True],
        }
    )

    dataframe = dataset.to_pandas()

    print("Dataset converted to a Pandas DataFrame")
    print(dataset)
    print()
    print("Type:", type(dataframe))
    print(dataframe)


if __name__ == "__main__":
    main()
