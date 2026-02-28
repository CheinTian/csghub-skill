# Space

## Operations

| Method | Path | Summary | Details |
|--------|------|---------|----------|
| GET | `/spaces` | Get spaces visible to current user | [View](../operations/get-spaces.md) |
| POST | `/spaces` | Create a new space | [View](../operations/post-spaces.md) |
| GET | `/spaces/cuda-versions` | Get supported CUDA versions | [View](../operations/get-spaces-cuda-versions.md) |
| GET | `/spaces/{namespace}/{name}` | show space detail | [View](../operations/get-spaces-namespace-name.md) |
| PUT | `/spaces/{namespace}/{name}` | Update a exists space | [View](../operations/put-spaces-namespace-name.md) |
| DELETE | `/spaces/{namespace}/{name}` | Delete a exists space | [View](../operations/delete-spaces-namespace-name.md) |
| GET | `/spaces/{namespace}/{name}/logs` | get space logs | [View](../operations/get-spaces-namespace-name-logs.md) |
| POST | `/spaces/{namespace}/{name}/run` | run space app | [View](../operations/post-spaces-namespace-name-run.md) |
| GET | `/spaces/{namespace}/{name}/status` | get space status | [View](../operations/get-spaces-namespace-name-status.md) |
| POST | `/spaces/{namespace}/{name}/stop` | stop space app | [View](../operations/post-spaces-namespace-name-stop.md) |
| POST | `/spaces/{namespace}/{name}/wakeup` | wake up space app | [View](../operations/post-spaces-namespace-name-wakeup.md) |
