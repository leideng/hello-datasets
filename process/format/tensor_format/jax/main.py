from datasets import Dataset


def main() -> None:
    try:
        import jax  # noqa: F401
    except ImportError:
        print("This example requires JAX.")
        print("Install it in the root environment before running this script.")
        return

    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "values": [[1.0, 1.5], [2.0, 2.5], [3.0, 3.5]],
        }
    )

    jax_dataset = dataset.with_format("jax")
    first_item = jax_dataset[0]
    first_batch = jax_dataset[:2]

    print("Dataset with JAX output format")
    print(jax_dataset)
    print()
    print("Item 0 types:", {key: type(value) for key, value in first_item.items()})
    print("Item 0:", first_item)
    print("Batch types:", {key: type(value) for key, value in first_batch.items()})
    print("Batch values:", first_batch)


if __name__ == "__main__":
    main()
