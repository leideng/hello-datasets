from pathlib import Path
import socket

from datasets import load_dataset


def try_parallel_load(data_files: list[str], cache_dir: Path):
    return load_dataset(
        "json",
        data_files=data_files,
        num_proc=2,
        cache_dir=str(cache_dir),
    )["train"]


def supports_local_process_manager() -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(("127.0.0.1", 0))
        return True
    except OSError:
        return False


def main() -> None:
    example_dir = Path(__file__).resolve().parent.parent
    data_files = sorted(str(path) for path in (example_dir / "data").glob("*.jsonl"))
    cache_dir = example_dir / ".cache"

    if supports_local_process_manager():
        dataset = try_parallel_load(data_files, cache_dir)
        execution_mode = "parallel"
    else:
        print("Parallel loading was blocked in this environment.")
        print("Falling back to num_proc=1 because local process sockets are unavailable.")
        print()
        dataset = load_dataset(
            "json",
            data_files=data_files,
            num_proc=1,
            cache_dir=str(cache_dir),
        )["train"]
        execution_mode = "fallback-single-process"

    print("Dataset loaded with multiple worker processes")
    print("Execution mode:", execution_mode)
    print(dataset)
    print()
    print("Number of rows:", len(dataset))
    print("Rows:", dataset[:])


if __name__ == "__main__":
    main()
