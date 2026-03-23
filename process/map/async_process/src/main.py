import asyncio

from datasets import Dataset


async def normalize_batch(batch: dict[str, list]) -> dict[str, list]:
    await asyncio.sleep(0)
    return {
        "normalized": [text.lower().replace(" ", "_") for text in batch["text"]]
    }


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "text": [
                "Async Map Example",
                "Normalize Retrieved Text",
                "Keep The Example Small",
            ],
        }
    )

    mapped_dataset = dataset.map(normalize_batch, batched=True)

    print("Dataset after async batched map")
    print(mapped_dataset)
    print()
    print("Rows:", mapped_dataset[:])


if __name__ == "__main__":
    main()
