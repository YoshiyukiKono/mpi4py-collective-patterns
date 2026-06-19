from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

local_value = rank + 1

global_sum = comm.reduce(local_value, op=MPI.SUM, root=0)
global_max = comm.reduce(local_value, op=MPI.MAX, root=0)

print(f"rank={rank}: local_value={local_value}")

if rank == 0:
    print(f"SUM={global_sum}")
    print(f"MAX={global_max}")
