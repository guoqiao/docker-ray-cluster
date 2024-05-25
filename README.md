# Docker Ray Cluster

Launch a [Ray](https://docs.ray.io/) Cluster with Docker Containers.

## Logical Roles

4 Logical Roles in a Ray Cluster:
- head: only 1, where workloads are scheduled, expose `:6379` and `:8265`
- worker: where workloads are actually done, connects to head with `head-ip:6379` (no http://)
- driver: trigger workloads, any machine connects to head/cluster with `http://head-ip:8265`
- client: a http client to call serve apps in cluster

Note:
- first 3 roles need ray installed, ideally same version.
- head = worker + control processes, so head is also a worker
- driver can be on head or worker, with address `http://localhost:8265`
- you can start a ray cluster with a single node, which acts as all 4 above roles, but that's not helpful for understanding ray.

## Workloads types

Trigger from driver, with `ray job submit --address http://head-ip:8265`:
- task: a function (without state), one-off
- actor: a class (with state), you can interactive with it until it dies

Serve on cluster/head (normally http services):
- app: a class with @ray.deployment, use `serve run xxx:app` to start

## Ray Address

In Ray, you often need to use `--address` cli option or `RAY_ADDRESS` env var to connect to ray cluster.
However, the expected url is actually different, depends on the role:

- when start ray worker: use `ray start --address head-ip:6379` (no http://)
- when submit ray job from driver: `ray job submit --address http://head-ip:8265 ... -- python script.py`
- when serve run: `serve run --address xxx:app`

This is very confusing, and hard to realize!