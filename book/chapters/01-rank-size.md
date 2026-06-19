# 01. Rank and Size

MPI programs usually start with the same two questions.

```python
rank = comm.Get_rank()
size = comm.Get_size()
```

`size` is the number of processes participating in the communicator.

`rank` is the identifier of the current process.

Run:

```bash
make hello
```

You should see output like:

```text
Hello from rank 0 of 4
Hello from rank 1 of 4
Hello from rank 2 of 4
Hello from rank 3 of 4
```

The order may differ. That is normal. Parallel programs do not promise that output will arrive in rank order.

The rest of the book is about how these ranks exchange data.
