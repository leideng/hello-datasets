from pathlib import Path

from datasets import Dataset


def build_examples():
    for i in range(5):
        yield {
            "id": i,
            "text": f"example-{i}",
            "length": len(f"example-{i}"),
        }


def main() -> None:
    cache_dir = Path(__file__).resolve().parent / ".cache"

    dataset = Dataset.from_generator(build_examples, cache_dir=str(cache_dir))

    print("Dataset created with Dataset.from_generator")
    print(dataset)
    print()
    print("Last row:", dataset[len(dataset) - 1])


if __name__ == "__main__":
    main()
