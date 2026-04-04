from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": list(range(8)),
            "text": [f"example-{i}" for i in range(8)],
        }
    )

    split_dataset = dataset.train_test_split(test_size=0.25, seed=13)

    print("Dataset after train_test_split")
    print(split_dataset)
    print()
    print("Train rows:", split_dataset["train"][:])
    print("Test rows:", split_dataset["test"][:])


if __name__ == "__main__":
    main()
