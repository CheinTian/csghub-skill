# Model

## Operations

| Method | Path | Summary | Details |
|--------|------|---------|----------|
| GET | `/models` | Get Visiable models for current user | [View](../operations/get-models.md) |
| POST | `/models` | Create a new model | [View](../operations/post-models.md) |
| GET | `/models/{namespace}/{name}` | Get model detail | [View](../operations/get-models-namespace-name.md) |
| PUT | `/models/{namespace}/{name}` | Update a exists model | [View](../operations/put-models-namespace-name.md) |
| DELETE | `/models/{namespace}/{name}` | Delete a exists model | [View](../operations/delete-models-namespace-name.md) |
| POST | `/models/{namespace}/{name}/finetune` | create a finetune instance | [View](../operations/post-models-namespace-name-finetune.md) |
| PUT | `/models/{namespace}/{name}/finetune/{id}` | Update a finetune instance | [View](../operations/put-models-namespace-name-finetune-id.md) |
| DELETE | `/models/{namespace}/{name}/finetune/{id}` | Delete a finetune instance | [View](../operations/delete-models-namespace-name-finetune-id.md) |
| PUT | `/models/{namespace}/{name}/finetune/{id}/start` | Start a finetune instance | [View](../operations/put-models-namespace-name-finetune-id-start.md) |
| PUT | `/models/{namespace}/{name}/finetune/{id}/stop` | Stop a finetune instance | [View](../operations/put-models-namespace-name-finetune-id-stop.md) |
| GET | `/models/{namespace}/{name}/quantizations` | list all gguf quantizations | [View](../operations/get-models-namespace-name-quantizations.md) |
| GET | `/models/{namespace}/{name}/relations` | Get model related assets | [View](../operations/get-models-namespace-name-relations.md) |
| PUT | `/models/{namespace}/{name}/relations` | Set dataset relation for model | [View](../operations/put-models-namespace-name-relations.md) |
| POST | `/models/{namespace}/{name}/relations/dataset` | add dataset relation for model | [View](../operations/post-models-namespace-name-relations-dataset.md) |
| DELETE | `/models/{namespace}/{name}/relations/dataset` | delete dataset relation for model | [View](../operations/delete-models-namespace-name-relations-dataset.md) |
| POST | `/models/{namespace}/{name}/run` | run model as inference | [View](../operations/post-models-namespace-name-run.md) |
| GET | `/models/{namespace}/{name}/run/versions/{id}` | list all inference versions | [View](../operations/get-models-namespace-name-run-versions-id.md) |
| POST | `/models/{namespace}/{name}/run/versions/{id}` | create a new inference version | [View](../operations/post-models-namespace-name-run-versions-id.md) |
| PUT | `/models/{namespace}/{name}/run/versions/{id}/traffic` | update inference version traffic percent | [View](../operations/put-models-namespace-name-run-versions-id-traffic.md) |
| DELETE | `/models/{namespace}/{name}/run/versions/{id}/{commit_id}` | delete inference version | [View](../operations/delete-models-namespace-name-run-versions-id-commit-id.md) |
| DELETE | `/models/{namespace}/{name}/run/{id}` | Delete a model inference | [View](../operations/delete-models-namespace-name-run-id.md) |
| PUT | `/models/{namespace}/{name}/run/{id}/start` | Start a model inference | [View](../operations/put-models-namespace-name-run-id-start.md) |
| PUT | `/models/{namespace}/{name}/run/{id}/stop` | Stop a model inference | [View](../operations/put-models-namespace-name-run-id-stop.md) |
| PUT | `/models/{namespace}/{name}/run/{id}/wakeup` | Wake up a model inference | [View](../operations/put-models-namespace-name-run-id-wakeup.md) |
| GET | `/models/{namespace}/{name}/serverless` | get model serverless | [View](../operations/get-models-namespace-name-serverless.md) |
| POST | `/models/{namespace}/{name}/serverless` | run model as serverless service | [View](../operations/post-models-namespace-name-serverless.md) |
| DELETE | `/models/{namespace}/{name}/serverless` | remove a serverless service | [View](../operations/delete-models-namespace-name-serverless.md) |
| GET | `/models/{namespace}/{name}/serverless/{id}` | Get repo serverless detail | [View](../operations/get-models-namespace-name-serverless-id.md) |
| PUT | `/models/{namespace}/{name}/serverless/{id}` | Update serverless parameters | [View](../operations/put-models-namespace-name-serverless-id.md) |
| GET | `/models/{namespace}/{name}/serverless/{id}/logs/{instance}` | get serverless logs | [View](../operations/get-models-namespace-name-serverless-id-logs-instance.md) |
| PUT | `/models/{namespace}/{name}/serverless/{id}/start` | Start a model serverless | [View](../operations/put-models-namespace-name-serverless-id-start.md) |
| GET | `/models/{namespace}/{name}/serverless/{id}/status` | get serverless status | [View](../operations/get-models-namespace-name-serverless-id-status.md) |
| PUT | `/models/{namespace}/{name}/serverless/{id}/stop` | Stop a model serverless | [View](../operations/put-models-namespace-name-serverless-id-stop.md) |
| POST | `/modeltrees/scan` | scan model tree | [View](../operations/post-modeltrees-scan.md) |
| GET | `/modeltrees/{namespace}/{name}/lineage` | Get model tree | [View](../operations/get-modeltrees-namespace-name-lineage.md) |
| POST | `/runtime_framework/scan` | Scan model metadata | [View](../operations/post-runtime-framework-scan.md) |
| POST | `/runtime_framework/{namespace}/{name}/scan` | Scan model metadata | [View](../operations/post-runtime-framework-namespace-name-scan.md) |
