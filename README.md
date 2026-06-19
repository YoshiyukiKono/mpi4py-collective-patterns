# mpi4py Collective Patterns

A compact Book-as-Code introduction to MPI collective communication with `mpi4py`.

This book focuses on the operations that make MPI feel like a real parallel programming model:

- `bcast`
- `scatter`
- `gather`
- `reduce`
- `allreduce`
- practical rewrites of Monte Carlo π and distributed vector statistics

The goal is not to cover all of MPI. The goal is to build a clear mental model of how data moves among ranks.

## Requirements

Recommended path: Docker Desktop.

Optional local path on macOS:

```bash
brew install open-mpi
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Quick start with Docker

```bash
make build
make hello
make bcast
make scatter
make gather
make reduce
make allreduce
make pi
make vector-stats
```

Run everything:

```bash
make run-all
```

## Local execution

After installing Open MPI and Python dependencies:

```bash
make local-hello
make local-bcast
make local-scatter
make local-gather
make local-reduce
make local-allreduce
make local-pi
make local-vector-stats
```

## Repository structure

```text
mpi4py-collective-patterns/
  README.md
  Makefile
  Dockerfile
  requirements.txt
  book/
    chapters/
  examples/
  notes/
```

## Reading order

1. [Chapter 00: Environment](book/chapters/00-environment.md)
2. [Chapter 01: Rank and Size](book/chapters/01-rank-size.md)
3. [Chapter 02: Broadcast](book/chapters/02-bcast.md)
4. [Chapter 03: Scatter](book/chapters/03-scatter.md)
5. [Chapter 04: Gather](book/chapters/04-gather.md)
6. [Chapter 05: Reduce](book/chapters/05-reduce.md)
7. [Chapter 06: Allreduce](book/chapters/06-allreduce.md)
8. [Chapter 07: Monte Carlo Pi](book/chapters/07-monte-carlo-pi.md)
9. [Chapter 08: Distributed Vector Statistics](book/chapters/08-vector-stats.md)
10. [Chapter 09: What Comes Next](book/chapters/09-next.md)

## License

MIT License for code examples. Text can be adapted under CC BY 4.0 unless you choose another policy.
