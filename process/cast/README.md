# cast

Change the dataset feature schema with `cast(...)`.

## What It Teaches

- `cast` lets you replace inferred features with an explicit schema.
- `ClassLabel` is useful for categorical targets such as sentiment classes.
- Explicit feature definitions make the dataset easier to interpret downstream.

## Run

From the repository root:

```bash
uv run python process/cast/main.py
```

## Expected Result

The script prints:

- the cast dataset summary
- the updated features
- the decoded human-readable class names

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import ClassLabel, Dataset, Features, Value`
  Imports `ClassLabel, Dataset, Features, Value` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 6: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 7: `            "text": [`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `                "this review is positive",`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `                "this review is negative",`
  Provides one literal sample value used by the example data or configuration.
- Line 10: `                "this review is positive too",`
  Provides one literal sample value used by the example data or configuration.
- Line 11: `            ],`
  Closes part of the sample data structure being built.
- Line 12: `            "label": [1, 0, 1],`
  Provides one literal sample value used by the example data or configuration.
- Line 13: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 14: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 16: `    target_features = Features(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 17: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 18: `            "text": Value("string"),`
  Provides one literal sample value used by the example data or configuration.
- Line 19: `            "label": ClassLabel(names=["negative", "positive"]),`
  Provides one literal sample value used by the example data or configuration.
- Line 20: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 21: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 23: `    cast_dataset = dataset.cast(target_features)`
  Casts the dataset to the declared feature schema.
- Line 25: `    print("Dataset after cast")`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `    print(cast_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 27: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 28: `    print("Features:", cast_dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 29: `    print("Decoded labels:", [cast_dataset.features["label"].int2str(v) for v in cast_dataset["label"]])`
  Prints information so you can observe what the dataset operation produced.
- Line 32: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 33: `    main()`
  Calls `main()` to start the example.

## Notes

- Casting is most useful when inference does not capture the semantics you want.
