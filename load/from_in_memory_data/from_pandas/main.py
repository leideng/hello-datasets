import pandas as pd
from datasets import Dataset


def main() -> None:
    dataframe = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "name": ["Ada", "Grace", "Linus"],
            "score": [98.5, 97.0, 95.5],
        }
    )

    dataset = Dataset.from_pandas(dataframe, preserve_index=False)

    print("Dataset created with Dataset.from_pandas")
    print(dataset)
    print()
    print("Features:", dataset.features)
    print("Second row:", dataset[1])


if __name__ == "__main__":
    main()
