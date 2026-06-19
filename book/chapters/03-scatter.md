# 03. Scatter

Scatter distributes one piece of data to each rank.

Rank 0 starts with a list of chunks:

```python
chunks = [chunk0, chunk1, chunk2, chunk3]
```

Then MPI sends:

```text
chunk0 -> rank 0
chunk1 -> rank 1
chunk2 -> rank 2
chunk3 -> rank 3
```

Run:

```bash
make scatter
```

The example computes a local sum for each chunk.

Scatter is the beginning of data parallelism. Instead of all ranks doing the same work on the same data, each rank receives a different part of the data.

Common use cases:

- split a vector
- split a list of files
- split a set of simulation tasks
- split a batch of training examples
