from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

local_result = {
    "rank": rank,
    "start": rank * 10,
    "end": rank * 10 + 9,
    "local_sum": sum(range(rank * 10, rank * 10 + 10)),
}

results = comm.gather(local_result, root=0)

if rank == 0:
    print("Gathered results:")
    for item in results:
        print(item)
    total = sum(item["local_sum"] for item in results)
    print(f"global_sum={total}, ranks={size}")
