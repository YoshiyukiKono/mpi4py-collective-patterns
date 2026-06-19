# 05. Reduce

Reduce combines values from all ranks into one result on the root rank.

Run:

```bash
make reduce
```

The example uses:

```python
global_sum = comm.reduce(local_value, op=MPI.SUM, root=0)
global_max = comm.reduce(local_value, op=MPI.MAX, root=0)
```

Each rank has a local value.

MPI combines those values using an operation such as:

- `MPI.SUM`
- `MPI.MAX`
- `MPI.MIN`
- `MPI.PROD`

Only the root rank receives the final result.

This is the core pattern behind many parallel computations:

```text
compute locally
combine globally
report from root
```
