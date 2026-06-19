# 04. Gather

Gather is the reverse of scatter.

Each rank computes a local result. Rank 0 collects all local results.

Run:

```bash
make gather
```

The example produces dictionaries like:

```python
{
    "rank": 2,
    "start": 20,
    "end": 29,
    "local_sum": 245,
}
```

Then rank 0 receives a list of such dictionaries.

Gather is useful when results are small and you want one process to format, write, or summarize them.

However, gather can become a bottleneck. If every rank sends a large object to rank 0, rank 0 becomes a traffic jam.

For numeric aggregation, `reduce` or `allreduce` is often better.
