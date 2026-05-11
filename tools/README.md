# tools/

Python helpers for generating site assets (interactive figures, processed data).

## Environment

No local venv. Reuses the sibling project's environment:

```
source /Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/.venv/bin/activate
```

## Conventions

- Scripts here read source data from `AI_in_finance/data/` and write site-ready output into `../assets/figures/` or `../assets/data/`.
- Each script is self-contained and idempotent.
