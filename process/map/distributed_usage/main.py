from datasets import Dataset


def annotate_rank(rank: int):
    def add_rank(batch: dict[str, list]) -> dict[str, list]:
        return {"worker_rank": [rank] * len(batch["text"])}

    return add_rank


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "text": [
                "row-0",
                "row-1",
                "row-2",
                "row-3",
                "row-4",
                "row-5",
            ]
        }
    )

    rank0_dataset = dataset.shard(num_shards=2, index=0).map(annotate_rank(0), batched=True)
    rank1_dataset = dataset.shard(num_shards=2, index=1).map(annotate_rank(1), batched=True)

    print("Distributed-style preprocessing by shard")
    print()
    print("Rank 0 rows:", rank0_dataset[:])
    print("Rank 1 rows:", rank1_dataset[:])


if __name__ == "__main__":
    main()
