---
name: csghub
description: Interact with CSGHub platform - manage models, datasets, codes, spaces, MCPs, agents, and more. Use when: (1) working with CSGHub API operations, (2) managing AI resources on CSGHub, (3) deploying models or spaces, (4) querying user resources, (5) any CSGHub platform interaction.
---

# CSGHub Skill

CSGHub is an open-source large model assets platform for managing, sharing, and deploying AI resources including models, datasets, code repositories, and AI applications.

## Authentication

CSGHub API uses Bearer Token authentication via the `Authorization` header.

```bash
export CSGHUB_TOKEN="your-api-token"
export CSGHUB_URL="https://hub.opencsg-stg.com/api/v1"
```

## Quick Start

```bash
# Set environment variables
export CSGHUB_TOKEN="your-token"
export CSGHUB_URL="https://hub.opencsg-stg.com/api/v1"

# List models
curl -H "Authorization: ${CSGHUB_TOKEN}" \
  "${CSGHUB_URL}/models"

# Get model details
curl -H "Authorization: ${CSGHUB_TOKEN}" \
  "${CSGHUB_URL}/models/namespace/model-name"
```

## Resource Types

| Resource | Description | Key Endpoints |
|----------|-------------|---------------|
| **models** | ML models, checkpoints, weights | `/models`, `/models/{namespace}/{name}` |
| **datasets** | Training datasets, evaluation data | `/datasets`, `/datasets/{namespace}/{name}` |
| **codes** | Code repositories, projects | `/codes`, `/codes/{namespace}/{name}` |
| **spaces** | AI applications, demos | `/spaces`, `/spaces/{namespace}/{name}` |
| **mcps** | Model Context Protocol servers | `/mcps`, `/mcps/{namespace}/{name}` |
| **agent** | AI agents and templates | `/agent/*` |
| **collections** | Curated resource collections | `/collections`, `/collections/{id}` |

## Common Operations

### List Resources

```bash
# List all models (paginated)
GET /models?page=1&per=20

# List user's models
GET /user/{username}/models

# List organization's models
GET /organization/{namespace}/models
```

### Get Resource Details

```bash
GET /{repo_type}/{namespace}/{name}
# repo_type: models | datasets | codes | spaces | mcps
```

### Repository Operations

```bash
# Get file tree
GET /{repo_type}/{namespace}/{name}/tree

# Get file content (blob)
GET /{repo_type}/{namespace}/{name}/blob/{file_path}

# Download file
GET /{repo_type}/{namespace}/{name}/download/{file_path}

# Get commits
GET /{repo_type}/{namespace}/{name}/commits

# Get branches
GET /{repo_type}/{namespace}/{name}/branches

# Get last commit
GET /{repo_type}/{namespace}/{name}/last_commit
```

### Model Operations

```bash
# Create model inference endpoint (serverless)
POST /models/{namespace}/{name}/serverless

# Get inference logs
GET /models/{namespace}/{name}/serverless/{id}/logs/{instance}

# Start/stop inference
PUT /models/{namespace}/{name}/serverless/{id}/start
PUT /models/{namespace}/{name}/serverless/{id}/stop

# List model relations (datasets used, etc.)
GET /models/{namespace}/{name}/relations
```

### Space Operations

```bash
# Deploy space
POST /spaces/{namespace}/{name}/run

# Get space status
GET /spaces/{namespace}/{name}/status

# Get space logs
GET /spaces/{namespace}/{name}/logs

# Stop/wake up space
PUT /spaces/{namespace}/{name}/stop
PUT /spaces/{namespace}/{name}/wakeup
```

### Dataset Operations

```bash
# Get data viewer catalog
GET /datasets/{namespace}/{name}/dataviewer/catalog

# Get dataset rows
GET /datasets/{namespace}/{name}/dataviewer/rows

# Preview file
GET /datasets/{namespace}/{name}/viewer/{file_path}
```

### User Operations

```bash
# Get current user
GET /user/{id}

# Get user by username
GET /user/{username}

# List user tokens
GET /user/{username}/tokens

# Manage SSH keys
GET /user/{username}/ssh_keys
POST /user/{username}/ssh_keys
DELETE /user/{username}/ssh_key/{name}
```

### Finetune Operations

```bash
# Create finetune job
POST /models/{namespace}/{name}/finetune

# Get finetune job
GET /models/{namespace}/{name}/finetune/{id}

# Get finetune logs
GET /models/{namespace}/{name}/finetune/{id}/logs/{instance}

# Start/stop finetune
PUT /models/{namespace}/{name}/finetune/{id}/start
PUT /models/{namespace}/{name}/finetune/{id}/stop
```

### Accounting Operations

```bash
# Get balance
GET /accounting/credit/{id}/balance

# List bills
GET /accounting/credit/{id}/bills?start_date=2024-01-01&end_date=2024-12-31

# List statements
GET /accounting/credit/{id}/statements
```

## CLI Tool

Use the included Python CLI for convenient operations:

```bash
# Set credentials
export CSGHUB_TOKEN="your-token"
export CSGHUB_URL="https://hub.opencsg-stg.com/api/v1"

# List models
python scripts/csghub-cli.py list models

# Get model details
python scripts/csghub-cli.py get model namespace/name

# List datasets
python scripts/csghub-cli.py list datasets

# List spaces
python scripts/csghub-cli.py list spaces

# List current user's resources
python scripts/csghub-cli.py list my-models
```

## API Specification

For complete API details including all endpoints, parameters, and response schemas, see [references/api-spec.md](references/api-spec.md).

## Error Handling

Common error codes:

| Code | Meaning |
|------|---------|
| 400 | Bad request - invalid parameters |
| 401 | Unauthorized - invalid or missing token |
| 403 | Forbidden - insufficient permissions |
| 404 | Not found - resource doesn't exist |
| 500 | Internal server error |

Error response format:
```json
{
  "code": 400,
  "msg": "error message",
  "data": null
}
```

## Rate Limiting

Some endpoints may have rate limits. Check response headers:
- `X-RateLimit-Limit`
- `X-RateLimit-Remaining`
- `X-RateLimit-Reset`

## References

- [API Specification](references/api-spec.md) - Complete endpoint documentation
- [CSGHub CLI](scripts/csghub-cli.py) - Python CLI tool for common operations
