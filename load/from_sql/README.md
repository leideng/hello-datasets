# from_sql

Load dataset rows from a SQL query with `Dataset.from_sql(...)`.

## What It Teaches

- `Dataset.from_sql(...)` can read query results into a Hugging Face dataset.
- SQL is useful when filtering or reshaping data before loading it.
- SQLite is enough for a minimal local example.

## Run

From the repository root:

```bash
uv run python load/from_sql/main.py
```

## Expected Result

The script:

- creates a local SQLite database in `data/`
- runs a SQL query that selects only training rows
- loads the query result into a dataset
- prints the schema and loaded rows

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `import sqlite3`
  Imports SQLite support so the example can create and query a local database file.
- Line 2: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 4: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 7: `def write_sqlite_database(database_file: Path) -> None:`
  Defines the function `write_sqlite_database` so the example logic is grouped into a named step.
- Line 8: `    database_file.parent.mkdir(parents=True, exist_ok=True)`
  Creates the parent directory if it does not exist yet.
- Line 10: `    connection = sqlite3.connect(database_file)`
  Opens a SQLite connection so SQL commands can be executed.
- Line 11: `    try:`
  Starts a `try` block so the example can handle errors or guarantee cleanup.
- Line 12: `        connection.execute("DROP TABLE IF EXISTS examples")`
  Executes a SQL statement against the SQLite database.
- Line 13: `        connection.execute(`
  Executes a SQL statement against the SQLite database.
- Line 14: `            """`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `            CREATE TABLE examples (`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 16: `                id INTEGER,`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 17: `                title TEXT,`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 18: `                split TEXT`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 19: `            )`
  Continues the multi-line Python structure opened by the previous line.
- Line 20: `            """`
  Provides one literal sample value used by the example data or configuration.
- Line 21: `        )`
  Continues the multi-line Python structure opened by the previous line.
- Line 22: `        connection.executemany(`
  Inserts several example rows into the database in one step.
- Line 23: `            "INSERT INTO examples (id, title, split) VALUES (?, ?, ?)",`
  Provides one literal sample value used by the example data or configuration.
- Line 24: `            [`
  Continues the multi-line Python structure opened by the previous line.
- Line 25: `                (1, "load from sqlite", "train"),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 26: `                (2, "query only the rows you need", "train"),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 27: `                (3, "sql can prepare data before loading", "eval"),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 28: `            ],`
  Closes part of the sample data structure being built.
- Line 29: `        )`
  Continues the multi-line Python structure opened by the previous line.
- Line 30: `        connection.commit()`
  Commits the SQL changes so the inserted rows are saved.
- Line 31: `    finally:`
  Starts a `finally` block so cleanup still runs even if an earlier step fails.
- Line 32: `        connection.close()`
  Closes the database connection and releases the file handle.
- Line 35: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 36: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so nearby `data/` and `.cache/` paths can be built relative to this file.
- Line 37: `    database_file = example_dir / "data" / "sample.sqlite"`
  Builds the path to a local input file used by the example.
- Line 38: `    cache_dir = example_dir / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 40: `    write_sqlite_database(database_file)`
  Calls the helper that prepares a small SQLite database for the loading example.
- Line 42: `    connection = sqlite3.connect(database_file)`
  Opens a SQLite connection so SQL commands can be executed.
- Line 43: `    try:`
  Starts a `try` block so the example can handle errors or guarantee cleanup.
- Line 44: `        dataset = Dataset.from_sql(`
  Loads query results from SQL directly into a Hugging Face dataset.
- Line 45: `            "SELECT id, title, split FROM examples WHERE split = 'train'",`
  Provides one literal sample value used by the example data or configuration.
- Line 46: `            connection,`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 47: `            cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 48: `        )`
  Continues the multi-line Python structure opened by the previous line.
- Line 49: `    finally:`
  Starts a `finally` block so cleanup still runs even if an earlier step fails.
- Line 50: `        connection.close()`
  Closes the database connection and releases the file handle.
- Line 52: `    print("Dataset loaded with Dataset.from_sql(...)")`
  Prints information so you can observe what the dataset operation produced.
- Line 53: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 54: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 55: `    print("Features:", dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 56: `    print("Rows:", dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 59: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 60: `    main()`
  Calls `main()` to start the example.

## Notes

- This example uses a local SQLite file, so it has no external database dependency.
- The SQL query is part of the example's teaching goal, not just setup.
- This folder stays under `load/from_sql/` because the topic is still SQL-based dataset loading.
