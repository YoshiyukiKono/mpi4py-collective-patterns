# 08. Distributed Vector Statistics

This chapter computes statistics over a distributed vector.

Rank 0 creates a vector. Scatter splits it across ranks.

Each rank computes local statistics:

- local sum
- local count
- local min
- local max

Then all ranks compute global statistics using allreduce.

Run:

```bash
make vector-stats
```

The important shift is this:

```text
The full vector does not need to be present on every rank.
```

Each rank owns a shard. Global answers are produced by communication.

This pattern appears in:

- large arrays
- distributed simulation
- distributed training
- tensor and matrix operations
- quantum state vector simulation
