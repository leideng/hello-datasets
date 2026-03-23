from datasets import load_dataset


def main() -> None:
    repo_id = "cornell-movie-review-data/rotten_tomatoes"

    print(f"Trying to load a small sample from Hugging Face Hub: {repo_id}")
    print()

    try:
        dataset = load_dataset(repo_id, split="train[:3]")
    except Exception as exc:
        print("This example requires network access to Hugging Face Hub.")
        print(f"Loading failed in the current environment: {type(exc).__name__}: {exc}")
        return

    print("Dataset loaded from Hugging Face Hub")
    print(dataset)
    print()
    print("Features:", dataset.features)
    print("Rows:", dataset[:])


if __name__ == "__main__":
    main()
