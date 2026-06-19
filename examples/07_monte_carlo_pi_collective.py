from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    config = {
        "total_samples": 1_000_000,
        "seed": 2026,
    }
else:
    config = None

config = comm.bcast(config, root=0)

samples_per_rank = config["total_samples"] // size
rng = np.random.default_rng(config["seed"] + rank)
points = rng.random((samples_per_rank, 2))
inside = np.sum(points[:, 0] ** 2 + points[:, 1] ** 2 <= 1.0)

total_inside = comm.reduce(int(inside), op=MPI.SUM, root=0)
total_samples_used = samples_per_rank * size

if rank == 0:
    pi_estimate = 4.0 * total_inside / total_samples_used
    print(f"ranks={size}")
    print(f"samples={total_samples_used}")
    print(f"inside={total_inside}")
    print(f"pi≈{pi_estimate}")
