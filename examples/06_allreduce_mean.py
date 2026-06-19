from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

local_value = (rank + 1) * 10

global_sum = comm.allreduce(local_value, op=MPI.SUM)
global_mean = global_sum / size

print(
    f"rank={rank}: local_value={local_value}, "
    f"global_sum={global_sum}, global_mean={global_mean}"
)
