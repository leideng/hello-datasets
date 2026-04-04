from datasets import Dataset


def keep_high_priority(example: dict[str, str]) -> bool:
    return example["priority"] == "high"


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3, 4],
            "task": [
                "load local data",
                "read the docs",
                "profile a transformation",
                "write notes",
            ],
            "priority": ["high", "low", "high", "medium"],
        }
    )

    filtered_dataset = dataset.filter(keep_high_priority)

    print("Dataset after filter")
    print(filtered_dataset)
    print()
    print("Rows:", filtered_dataset[:])


if __name__ == "__main__":
    main()
