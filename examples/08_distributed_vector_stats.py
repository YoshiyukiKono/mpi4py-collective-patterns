from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    vector = np.arange(1, size * 8 + 1, dtype=np.float64)
    chunks = np.array_split(vector, size)
else:
    chunks = None

local_vector = comm.scatter(chunks, root=0)
local_sum = float(np.sum(local_vector))
local_count = len(local_vector)
local_min = float(np.min(local_vector))
local_max = float(np.max(local_vector))

global_sum = comm.allreduce(local_sum, op=MPI.SUM)
global_count = comm.allreduce(local_count, op=MPI.SUM)
global_min = comm.allreduce(local_min, op=MPI.MIN)
global_max = comm.allreduce(local_max, op=MPI.MAX)

global_mean = global_sum / global_count

print(
    f"rank={rank}: local_vector={local_vector.tolist()}, "
    f"local_sum={local_sum}"
)

if rank == 0:
    print("Global statistics:")
    print(f"count={global_count}")
    print(f"sum={global_sum}")
    print(f"mean={global_mean}")
    print(f"min={global_min}")
    print(f"max={global_max}")
