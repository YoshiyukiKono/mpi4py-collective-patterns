IMAGE := mpi4py-collective-patterns
NP ?= 4
PY ?= python
MPIRUN_LOCAL ?= mpirun
MPIRUN_DOCKER := docker run --rm $(IMAGE) mpirun --allow-run-as-root -np $(NP)

.PHONY: build shell run-all \
 hello bcast scatter gather reduce allreduce pi vector-stats \
 local-hello local-bcast local-scatter local-gather local-reduce local-allreduce local-pi local-vector-stats

build:
	docker build -t $(IMAGE) .

shell:
	docker run --rm -it $(IMAGE) bash

hello:
	$(MPIRUN_DOCKER) python examples/01_hello.py

bcast:
	$(MPIRUN_DOCKER) python examples/02_bcast_config.py

scatter:
	$(MPIRUN_DOCKER) python examples/03_scatter_chunks.py

gather:
	$(MPIRUN_DOCKER) python examples/04_gather_results.py

reduce:
	$(MPIRUN_DOCKER) python examples/05_reduce_sum.py

allreduce:
	$(MPIRUN_DOCKER) python examples/06_allreduce_mean.py

pi:
	$(MPIRUN_DOCKER) python examples/07_monte_carlo_pi_collective.py

vector-stats:
	$(MPIRUN_DOCKER) python examples/08_distributed_vector_stats.py

run-all: hello bcast scatter gather reduce allreduce pi vector-stats

local-hello:
	$(MPIRUN_LOCAL) -np $(NP) $(PY) examples/01_hello.py

local-bcast:
	$(MPIRUN_LOCAL) -np $(NP) $(PY) examples/02_bcast_config.py

local-scatter:
	$(MPIRUN_LOCAL) -np $(NP) $(PY) examples/03_scatter_chunks.py

local-gather:
	$(MPIRUN_LOCAL) -np $(NP) $(PY) examples/04_gather_results.py

local-reduce:
	$(MPIRUN_LOCAL) -np $(NP) $(PY) examples/05_reduce_sum.py

local-allreduce:
	$(MPIRUN_LOCAL) -np $(NP) $(PY) examples/06_allreduce_mean.py

local-pi:
	$(MPIRUN_LOCAL) -np $(NP) $(PY) examples/07_monte_carlo_pi_collective.py

local-vector-stats:
	$(MPIRUN_LOCAL) -np $(NP) $(PY) examples/08_distributed_vector_stats.py
