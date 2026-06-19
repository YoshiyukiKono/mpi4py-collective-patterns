# 06. Allreduce

Allreduce is like reduce, but every rank receives the final result.

Run:

```bash
make allreduce
```

The example computes a global mean.

```python
global_sum = comm.allreduce(local_value, op=MPI.SUM)
global_mean = global_sum / size
```

After `allreduce`, all ranks know `global_sum` and `global_mean`.

This is extremely important in distributed machine learning. Each worker computes local gradients. The workers then use an allreduce-like operation to compute a shared global gradient.

Mental model:

```text
all ranks contribute
MPI combines values
all ranks receive the combined value
```
