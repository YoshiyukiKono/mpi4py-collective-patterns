# 00. Environment

This book is designed to be runnable in two ways.

The recommended path is Docker. It avoids most MPI installation problems and makes the examples reproducible.

```bash
make build
make run-all
```

The local macOS path is useful when you want to understand how MPI is installed on your own machine.

```bash
brew install open-mpi
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then run:

```bash
make local-hello
```

The important point is that `mpi4py` is not MPI itself. It is a Python binding to an MPI implementation. You need both:

- Open MPI or another MPI implementation
- `mpi4py`

Docker hides this distinction at first. Local execution reveals it.
