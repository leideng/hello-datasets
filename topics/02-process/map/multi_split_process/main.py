from datasets import Dataset, DatasetDict


def add_length(batch: dict[str, list]) -> dict[str, list]:
    return {"length": [len(text) for text in batch["text"]]}


def main() -> None:
    dataset_dict = DatasetDict(
        {
            "train": Dataset.from_dict({"text": ["train-a", "train-b"]}),
            "test": Dataset.from_dict({"text": ["test-a"]}),
        }
    )

    mapped_dataset_dict = dataset_dict.map(add_length, batched=True)

    print("DatasetDict after map across multiple splits")
    print(mapped_dataset_dict)
    print()
    print("Train rows:", mapped_dataset_dict["train"][:])
    print("Test rows:", mapped_dataset_dict["test"][:])


if __name__ == "__main__":
    main()
