# Podcast episode library

This directory contains the full 200-episode research library behind the [AI-Native Company and Podcast Research](../README.md).

## Files

- `episode-library.csv.gz.part-01`
- `episode-library.csv.gz.part-02`
- `episode-library.csv.gz.part-03`
- `episode-library.csv.gz.part-04`
- `episode-library.csv.gz.part-05`

The files are sequential binary chunks of one gzip archive.

## Reassemble and extract

```bash
cat episode-library.csv.gz.part-* > episode-library.csv.gz
sha256sum episode-library.csv.gz
# expected: 4540ef5a1003181905e4a842dbc24fb0f4871b2a25b1a76401d593d78d99aa52
gzip -dk episode-library.csv.gz
```

The extracted file is `episode-library.csv`.

## Fields

`Rank`, `Priority`, `Primary Topic`, `Tags`, `Podcast`, `Episode`, `Guest(s)`, `Published`, `Why relevant to Alexey`, `Apply / experiment`, `Source type`, `Status`, `Rating (1–5)`, `Notes`, and `Official episode/source URL`.

Research date: 2026-09-05. Episode availability and titles may change.
