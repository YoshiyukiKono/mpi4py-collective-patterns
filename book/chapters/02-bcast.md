# 02. Broadcast

Broadcast sends one value from one rank to every other rank.

In many programs, rank 0 decides the configuration and all ranks run the same computation using that shared configuration.

Run:

```bash
make bcast
```

The example uses:

```python
config = comm.bcast(config, root=0)
```

Before `bcast`, only rank 0 has the dictionary.

After `bcast`, every rank has the same dictionary.

Broadcast is useful for:

- experiment settings
- random seeds
- model parameters
- paths and filenames

The mental model is simple:

```text
rank 0 owns data
rank 0 sends data to all ranks
all ranks continue with the same data
```
