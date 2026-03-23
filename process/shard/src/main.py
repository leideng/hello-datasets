from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": list(range(10)),
            "text": [f"row-{i}" for i in range(10)],
        }
    )

    shard_dataset = dataset.shard(num_shards=3, index=1)

    print("Dataset after shard")
    print(shard_dataset)
    print()
    print("Rows:", shard_dataset[:])


if __name__ == "__main__":
    main()
