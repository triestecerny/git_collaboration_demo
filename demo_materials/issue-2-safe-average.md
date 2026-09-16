# Add a safe average helper

## Outcome

Add `average_or_none(values)` to `stats_helpers.py`.

## Why it matters

A caller should receive a useful result for a nonempty collection without receiving a division-by-zero error for an empty collection.

## Acceptance criteria

- [ ] Return the arithmetic mean for a nonempty collection.
- [ ] Return `None` when the collection is empty.
- [ ] Keep the function independent of external packages.

