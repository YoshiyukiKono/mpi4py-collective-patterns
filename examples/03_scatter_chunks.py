from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    numbers = list(range(1, size * 4 + 1))
    chunks = [numbers[i * 4:(i + 1) * 4] for i in range(size)]
else:
    chunks = None

my_chunk = comm.scatter(chunks, root=0)
local_sum = sum(my_chunk)

print(f"rank={rank}: chunk={my_chunk}, local_sum={local_sum}")
