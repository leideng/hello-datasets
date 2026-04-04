from datasets import Dataset


def add_summary(batch: dict[str, list]) -> dict[str, list]:
    return {
        "summary": [
            f"{title} ({priority})"
            for title, priority in zip(batch["title"], batch["priority"])
        ]
    }


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "title": [
                "read the dataset docs",
                "write a map example",
                "verify the output",
            ],
            "priority": ["high", "medium", "high"],
        }
    )

    mapped_dataset = dataset.map(add_summary, batched=True, batch_size=2)

    print("Dataset after batched map")
    print(mapped_dataset)
    print()
    print("Column names:", mapped_dataset.column_names)
    print("Rows:", mapped_dataset[:])


if __name__ == "__main__":
    main()
