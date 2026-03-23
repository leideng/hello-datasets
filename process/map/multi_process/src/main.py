import socket

from datasets import Dataset


def supports_local_process_manager() -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(("127.0.0.1", 0))
        return True
    except OSError:
        return False


def add_length(batch: dict[str, list]) -> dict[str, list]:
    return {"length": [len(text) for text in batch["text"]]}


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "text": [
                "parallel map can speed up heavier transforms",
                "but tiny examples often do not benefit",
                "the api still matters for learning",
                "sandbox restrictions may block worker management",
            ]
        }
    )

    if supports_local_process_manager():
        mapped_dataset = dataset.map(add_length, batched=True, num_proc=2)
        execution_mode = "parallel"
    else:
        print("Multiprocessing is blocked in this environment.")
        print("Falling back to plain map(...) for a runnable example.")
        print()
        mapped_dataset = dataset.map(add_length, batched=True)
        execution_mode = "fallback-plain-map"

    print("Dataset after multi-process style map")
    print("Execution mode:", execution_mode)
    print(mapped_dataset)
    print()
    print("Rows:", mapped_dataset[:])


if __name__ == "__main__":
    main()
