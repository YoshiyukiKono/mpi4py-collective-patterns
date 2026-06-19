from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    config = {
        "experiment": "bcast-demo",
        "samples_per_rank": 5,
        "seed": 2026,
    }
else:
    config = None

config = comm.bcast(config, root=0)

print(f"rank={rank}: received config={config}")
