from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3, 4, 5],
            "text": [f"example-{i}" for i in range(1, 6)],
        }
    )

    print("Iterating over dataset batches")
    print(dataset)
    print()

    for batch_index, batch in enumerate(dataset.iter(batch_size=2), start=1):
        print(f"Batch {batch_index}: {batch}")


if __name__ == "__main__":
    main()
