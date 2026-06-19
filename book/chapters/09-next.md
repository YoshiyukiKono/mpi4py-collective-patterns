# 09. What Comes Next

This book covered the core collective operations:

- broadcast
- scatter
- gather
- reduce
- allreduce

These operations are small, but they scale into major systems.

Possible next books in the same series:

1. OpenMP and Numba for single-node CPU parallelism
2. Slurm mini cluster for HPC job scheduling
3. Kubernetes Jobs and MPI Operator
4. PyTorch DistributedDataParallel
5. CuPy and CUDA first steps
6. NetKet small systems

The most important conceptual bridge is this:

```text
MPI collective communication is not just an HPC detail.
It is a pattern language for distributed computation.
```

Once you understand collective operations, Slurm, Kubernetes-based batch systems, and distributed deep learning become much easier to place on the same map.
