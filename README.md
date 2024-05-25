# Docker Ray Cluster

Launch a Ray Cluster with Docker containers.

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

Workloads type:

Trigger from driver, with `ray job submit --address http://head-ip:8265`:
- task: a function (without state), one-off
- actor: a class (with state), you can interactive with it until it dies

Note: for ray worker, the `--address` option or `RAY_ADDRESS` envvar is `head-ip:6379` (no http://). Do not be confused.

Run from cluster/head:
- app: a class with @ray.deployment, use serve run xxx:app to start