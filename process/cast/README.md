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

## Notes

- Casting is most useful when inference does not capture the semantics you want.
