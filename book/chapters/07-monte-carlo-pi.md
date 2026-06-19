# 07. Monte Carlo Pi with Collectives

Monte Carlo π estimation is a small but useful example.

Each rank generates random points in a square and counts how many fall inside the unit circle.

The local count is then reduced into a global count.

Run:

```bash
make pi
```

The program uses two collective operations.

First, broadcast configuration:

```python
config = comm.bcast(config, root=0)
```

Second, reduce local counts:

```python
total_inside = comm.reduce(int(inside), op=MPI.SUM, root=0)
```

This chapter combines the earlier patterns into a real parallel computation.

It is not about π itself. It is about a general pattern:

```text
broadcast configuration
compute independent local samples
reduce local results
```
