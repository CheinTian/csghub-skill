# CSGHub API Specification

## Overview

- **Base URL**: `https://hub.opencsg-stg.com/api/v1`
- **Authentication**: Bearer Token via `Authorization` header
- **Format**: JSON

## Authentication

All API requests require authentication using a Bearer token:

```http
Authorization: your-api-token
```

## Resource Types

CSGHub supports these primary resource types:

| Type | Description | Path Prefix |
|------|-------------|-------------|
| `models` | Machine learning models | `/models` |
| `datasets` | Training and evaluation datasets | `/datasets` |
| `codes` | Code repositories | `/codes` |
| `spaces` | AI applications and demos | `/spaces` |
| `mcps` | Model Context Protocol servers | `/mcps` |

## Common Operations

### Repository Operations

All repository types (models, datasets, codes, spaces, mcps) share these common endpoints:

#### List Resources
```
GET /{resource_type}
```

Query Parameters:
- `page` (int): Page number (default: 1)
- `per` (int): Items per page (default: 20)
- `search` (string): Search query

#### Get Resource
```
GET /{resource_type}/{namespace}/{name}
```

#### Create Resource
```
POST /{resource_type}
```

Request Body:
```json
{
  "namespace": "org-name",
  "name": "resource-name",
  "description": "Resource description",
  "private": false
}
```

#### Update Resource
```
PUT /{resource_type}/{namespace}/{name}
```

#### Delete Resource
```
DELETE /{resource_type}/{namespace}/{name}
```

### File Operations

#### List Files
```
GET /{resource_type}/{namespace}/{name}/tree?path={path}
```

#### Get File Content
```
GET /{resource_type}/{namespace}/{name}/blob/{file_path}
```

#### Download File
```
GET /{resource_type}/{namespace}/{name}/download/{file_path}
```

#### Get Last Commit
```
GET /{resource_type}/{namespace}/{name}/last_commit
```

#### List Commits
```
GET /{resource_type}/{namespace}/{name}/commits
```

#### List Branches
```
GET /{resource_type}/{namespace}/{name}/branches
```

## Model Operations

### List Models
```
GET /models
```

### Get Model
```
GET /models/{namespace}/{name}
```

### Model Relations
```
GET /models/{namespace}/{name}/relations
PUT /models/{namespace}/{name}/relations
```

### Model Inference (Serverless)

#### List Inference Endpoints
```
GET /models/{namespace}/{name}/serverless
```

#### Create Inference Endpoint
```
POST /models/{namespace}/{name}/serverless
```

Request Body:
```json
{
  "runtime_framework": "transformers",
  "resource_class": "gpu.nvidia.a10",
  "min_replica": 1,
  "max_replica": 3
}
```

#### Get Inference Endpoint
```
GET /models/{namespace}/{name}/serverless/{id}
```

#### Update Inference Endpoint
```
PUT /models/{namespace}/{name}/serverless/{id}
```

#### Delete Inference Endpoint
```
DELETE /models/{namespace}/{name}/serverless
DELETE /models/{namespace}/{name}/serverless/{id}
```

#### Start/Stop Inference
```
PUT /models/{namespace}/{name}/serverless/{id}/start
PUT /models/{namespace}/{name}/serverless/{id}/stop
```

#### Get Inference Logs
```
GET /models/{namespace}/{name}/serverless/{id}/logs/{instance}
```

#### Get Inference Status
```
GET /models/{namespace}/{name}/serverless/{id}/status
```

### Model Inference (Dedicated)

#### Create Run
```
POST /models/{namespace}/{name}/run
```

#### Get Run
```
GET /models/{namespace}/{name}/run/{id}
```

#### Delete Run
```
DELETE /models/{namespace}/{name}/run/{id}
```

#### Start/Stop/Wake Up Run
```
PUT /models/{namespace}/{name}/run/{id}/start
PUT /models/{namespace}/{name}/run/{id}/stop
PUT /models/{namespace}/{name}/run/{id}/wakeup
```

### Finetune Operations

#### Create Finetune Job
```
POST /models/{namespace}/{name}/finetune
```

Request Body:
```json
{
  "dataset_namespace": "org",
  "dataset_name": "dataset-name",
  "resource_class": "gpu.nvidia.a10",
  "hyperparameters": {
    "learning_rate": 5e-5,
    "batch_size": 8,
    "epochs": 3
  }
}
```

#### Get Finetune Job
```
GET /models/{namespace}/{name}/finetune/{id}
```

#### Update Finetune Job
```
PUT /models/{namespace}/{name}/finetune/{id}
```

#### Delete Finetune Job
```
DELETE /models/{namespace}/{name}/finetune/{id}
```

#### Start/Stop Finetune
```
PUT /models/{namespace}/{name}/finetune/{id}/start
PUT /models/{namespace}/{name}/finetune/{id}/stop
```

#### Get Finetune Logs
```
GET /models/{namespace}/{name}/finetune/{id}/logs/{instance}
```

### Model Quantization
```
GET /models/{namespace}/{name}/quantizations
```

## Dataset Operations

### List Datasets
```
GET /datasets
```

### Get Dataset
```
GET /datasets/{namespace}/{name}
```

### Data Viewer

#### Get Catalog
```
GET /datasets/{namespace}/{name}/dataviewer/catalog
```

#### Get Rows
```
GET /datasets/{namespace}/{name}/dataviewer/rows
```

Query Parameters:
- `page` (int): Page number
- `per` (int): Rows per page
- `search` (string): Search query

#### Preview File
```
GET /datasets/{namespace}/{name}/viewer/{file_path}
```

## Space Operations

### List Spaces
```
GET /spaces
```

### Get Space
```
GET /spaces/{namespace}/{name}
```

### Deploy Space
```
POST /spaces/{namespace}/{name}/run
```

### Get Space Status
```
GET /spaces/{namespace}/{name}/status
```

### Get Space Logs
```
GET /spaces/{namespace}/{name}/logs
```

### Stop/Wake Up Space
```
POST /spaces/{namespace}/{name}/stop
POST /spaces/{namespace}/{name}/wakeup
```

### CUDA Versions
```
GET /spaces/cuda-versions
```

## MCP Operations

### List MCPs
```
GET /mcps
```

### Get MCP
```
GET /mcps/{namespace}/{name}
```

### Deploy MCP
```
POST /mcps/{namespace}/{name}/deploy
```

### List MCP Tools
```
GET /mcps/tools
```

## Code Operations

### List Codes
```
GET /codes
```

### Get Code
```
GET /codes/{namespace}/{name}
```

### Get Relations
```
GET /codes/{namespace}/{name}/relations
```

## User Operations

### Get User
```
GET /user/{username}
GET /user/{id}
```

### Update User
```
PUT /user/{id}
```

### Delete User
```
DELETE /user/{username}
```

### User Resources

#### List User Models
```
GET /user/{username}/models
```

#### List User Datasets
```
GET /user/{username}/datasets
```

#### List User Codes
```
GET /user/{username}/codes
```

#### List User Spaces
```
GET /user/{username}/spaces
```

#### List User MCPs
```
GET /user/{username}/mcps
```

#### List User Collections
```
GET /user/{username}/collections
```

### User Likes

```
GET /user/{username}/likes/models
GET /user/{username}/likes/datasets
GET /user/{username}/likes/codes
GET /user/{username}/likes/spaces
GET /user/{username}/likes/collections
GET /user/{username}/likes/mcps

PUT /user/{username}/likes/{repoid}
DELETE /user/{username}/likes/{repoid}
```

### SSH Keys

```
GET /user/{username}/ssh_keys
POST /user/{username}/ssh_keys
DELETE /user/{username}/ssh_key/{name}
```

### Tokens

```
GET /user/{username}/tokens
GET /user/{username}/tokens/first
DELETE /user/{username}/tokens/{token_name}
```

### User Labels
```
PUT /user/labels
```

## Organization Operations

### List Organizations
```
GET /organization
```

### Get Organization
```
GET /organization/{namespace}
```

### Organization Resources

```
GET /organization/{namespace}/models
GET /organization/{namespace}/datasets
GET /organization/{namespace}/codes
GET /organization/{namespace}/spaces
GET /organization/{namespace}/mcps
```

### Members

```
GET /organization/{namespace}/members
POST /organization/{namespace}/members
PUT /organization/{namespace}/members/{username}
DELETE /organization/{namespace}/members/{username}
```

## Collection Operations

### List Collections
```
GET /collections
```

### Get Collection
```
GET /collections/{id}
```

### Create Collection
```
POST /collections
```

### Update Collection
```
PUT /collections/{id}
```

### Delete Collection
```
DELETE /collections/{id}
```

## Accounting Operations

### Balance

#### Get Current User Balance
```
GET /accounting/credit/balance
```

Query Parameters:
- `current_user` (string, required): Current user ID
- `page` (int): Page number
- `per` (int): Items per page

#### Get User Balance
```
GET /accounting/credit/{id}/balance
```

Query Parameters:
- `current_user` (string, required)

### Bills

#### List Bills
```
GET /accounting/credit/{id}/bills
```

Query Parameters:
- `scene` (int): Bill scene (10, 11, 12, 20)
- `start_date` (string): Start date (YYYY-MM-DD)
- `end_date` (string): End date (YYYY-MM-DD)
- `current_user` (string, required)
- `page` (int)
- `per` (int)

### Statements

#### List Statements
```
GET /accounting/credit/{id}/statements
```

Query Parameters:
- `scene` (int): Statement scene (10, 11, 12, 20)
- `instance_name` (string, required)
- `start_time` (string): Start time (YYYY-MM-DD HH:MM:SS)
- `end_time` (string): End time (YYYY-MM-DD HH:MM:SS)
- `current_user` (string, required)
- `page` (int)
- `per` (int)

### Recharge

#### Create Pay Order
```
POST /accounting/recharge/create-pay-order
```

#### Get Recharge Status
```
GET /accounting/recharge/{id}/status
```

#### List Recharges
```
GET /accounting/recharge/list
GET /accounting/recharge/user-recharge-list
GET /accounting/recharges
GET /accounting/weekly_recharges
```

### Invoices

#### List Invoices
```
GET /accounting/invoice/list
POST /accounting/invoice/list
```

#### Get Invoice
```
GET /accounting/invoice/{id}
```

#### Create Invoice
```
POST /accounting/invoice/create
```

#### Admin Invoices
```
POST /accounting/invoice/admin/list
GET /accounting/invoice/admin/{id}
PUT /accounting/invoice/admin/{id}
DELETE /accounting/invoice/admin/{id}
```

#### Invoice Dashboard
```
POST /accounting/invoice/dashboard
```

#### Invoice Titles
```
GET /accounting/invoice/title/list
POST /accounting/invoice/title
PUT /accounting/invoice/title/{id}
DELETE /accounting/invoice/title/{id}
```

### Subscriptions

```
GET /accounting/subscriptions
POST /accounting/subscriptions
GET /accounting/subscriptions/bills
GET /accounting/subscriptions/status
GET /accounting/subscriptions/status/batch
```

### Pricing

```
GET /accounting/price
POST /accounting/price
GET /accounting/price/{id}
PUT /accounting/price/{id}
DELETE /accounting/price/{id}
```

### Low Balance Warning

```
PUT /accounting/credit/low-balance-warn
```

Request Body:
```json
{
  "threshold": 100
}
```

## Agent Operations

### Instances

```
GET /agent/instances
POST /agent/instances
GET /agent/instances/{id}
PUT /agent/instances/{id}
DELETE /agent/instances/{id}
GET /agent/instances/by-content-id/{type}/{content_id}
GET /agent/instances/status
GET /agent/instances/monitor
```

### Sessions

```
GET /agent/instances/{id}/sessions
POST /agent/instances/{id}/sessions
GET /agent/instances/{id}/sessions/{session_uuid}
PUT /agent/instances/{id}/sessions/{session_uuid}
DELETE /agent/instances/{id}/sessions/{session_uuid}
```

### Session History

```
GET /agent/instances/{id}/sessions/{session_uuid}/histories
POST /agent/instances/{id}/sessions/{session_uuid}/histories
PUT /agent/instances/{id}/sessions/{session_uuid}/histories/{msg_uuid}
DELETE /agent/instances/{id}/sessions/{session_uuid}/histories/{msg_uuid}
```

### Feedback

```
PUT /agent/instances/{id}/sessions/{session_uuid}/histories/{msg_uuid}/feedback
```

### Rewrite

```
PUT /agent/instances/{id}/sessions/{session_uuid}/histories/{msg_uuid}/rewrite
```

### Knowledge Bases

```
GET /agent/knowledge-bases
POST /agent/knowledge-bases
GET /agent/knowledge-bases/{id}
PUT /agent/knowledge-bases/{id}
DELETE /agent/knowledge-bases/{id}
GET /agent/knowledge-bases/content-id/{content_id}
```

### Templates

```
GET /agent/templates
POST /agent/templates
GET /agent/templates/{id}
PUT /agent/templates/{id}
DELETE /agent/templates/{id}
GET /agent/templates/{id}/instances
```

### Prompts

```
GET /agent/prompts
POST /agent/prompts
GET /agent/prompts/{id}
PUT /agent/prompts/{id}
DELETE /agent/prompts/{id}
```

### Optimize Prompt

```
POST /agent/prompts/optimize
```

### Tasks

```
GET /agent/tasks
POST /agent/tasks
GET /agent/tasks/{id}
PUT /agent/tasks/{id}
DELETE /agent/tasks/{id}
```

### MCP Servers

```
GET /agent/mcp-servers
POST /agent/mcp-servers
GET /agent/mcp-servers/{id}
PUT /agent/mcp-servers/{id}
DELETE /agent/mcp-servers/{id}
GET /agent/mcp-servers/status
GET /agent/mcp-servers/monitor
POST /agent/mcp-servers/inspect
```

### User Preferences

```
GET /agent/user-preferences
PUT /agent/user-preferences
```

### Shared Sessions

```
GET /agent/shared/session
POST /agent/shared/session
```

## Evaluation Operations

### List Evaluations
```
GET /evaluations
```

### Get Evaluation
```
GET /evaluations/{id}
```

### Create Evaluation
```
POST /evaluations
```

### Update Evaluation
```
PUT /evaluations/{id}
```

### Delete Evaluation
```
DELETE /evaluations/{id}
```

### Evaluation Metrics
```
GET /evaluations/{id}/metrics
```

### Evaluation Results
```
GET /evaluations/{id}/results
```

## Runtime Framework Operations

### List Runtime Frameworks
```
GET /runtime_framework
```

### Get Runtime Framework
```
GET /runtime_framework/{id}
```

### Runtime Framework Models
```
GET /runtime_framework/{id}/models
GET /runtime_framework/models
```

### Update Runtime Framework Models
```
PUT /runtime_framework/{id}/models
DELETE /runtime_framework/{id}/models
```

## Cluster Operations

### List Clusters
```
GET /cluster
GET /cluster/public
```

### Get Cluster
```
GET /cluster/{id}
```

### Cluster Deploys
```
GET /cluster/deploys
GET /cluster/admin/deploys
GET /cluster/deploys_report
```

### Cluster Nodes
```
GET /cluster/admin/nodes
GET /cluster/admin/nodes/{id}
PUT /cluster/admin/nodes/{id}/set_access_mode
PUT /cluster/admin/nodes/{id}/vxpu/enable
PUT /cluster/admin/nodes/{id}/vxpu/disable
```

### Cluster Workflows
```
GET /cluster/admin/workflows
```

### Cluster Usage
```
GET /cluster/usage
```

## Tag Operations

### List Tags
```
GET /tags
```

### Get Tag
```
GET /tags/{id}
```

### Create Tag
```
POST /tags
```

### Update Tag
```
PUT /tags/{id}
```

### Delete Tag
```
DELETE /tags/{id}
```

### Tag Categories
```
GET /tags/categories
POST /tags/categories
GET /tags/categories/id
PUT /tags/categories/id
DELETE /tags/categories/id
```

## Discussion Operations

### List Discussions
```
GET /{repo_type}/{namespace}/{name}/discussions
```

### Create Discussion
```
POST /{repo_type}/{namespace}/{name}/discussions
```

### Get Discussion
```
GET /{repo_type}/{namespace}/{name}/discussions/{id}
```

### Update Discussion
```
PUT /{repo_type}/{namespace}/{name}/discussions/{id}
```

### Delete Discussion
```
DELETE /{repo_type}/{namespace}/{name}/discussions/{id}
```

### Discussion Comments
```
GET /{repo_type}/{namespace}/{name}/discussions/{id}/comments
POST /{repo_type}/{namespace}/{name}/discussions/{id}/comments
PUT /{repo_type}/{namespace}/{name}/discussions/{id}/comments/{comment_id}
DELETE /{repo_type}/{namespace}/{name}/discussions/{id}/comments/{comment_id}
```

## Response Format

All API responses follow this structure:

```json
{
  "code": 200,
  "msg": "success",
  "data": { ... }
}
```

### Success Response

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "id": "...",
    "name": "...",
    ...
  }
}
```

### Error Response

```json
{
  "code": 400,
  "msg": "error message",
  "data": null
}
```

### List Response

```json
{
  "code": 200,
  "msg": "success",
  "data": [
    { ... },
    { ... }
  ]
}
```

## Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad request - invalid parameters |
| 401 | Unauthorized - invalid or missing token |
| 403 | Forbidden - insufficient permissions |
| 404 | Not found - resource doesn't exist |
| 500 | Internal server error |

## Pagination

List endpoints support pagination via query parameters:

- `page`: Page number (1-indexed)
- `per`: Items per page (default varies by endpoint, typically 20)

Example:
```
GET /models?page=2&per=50
```

## Rate Limiting

Some endpoints may have rate limits. Check response headers:
- `X-RateLimit-Limit`: Request limit
- `X-RateLimit-Remaining`: Remaining requests
- `X-RateLimit-Reset`: Reset timestamp

## OpenAI Compatible Endpoints

CSGHub provides OpenAI-compatible endpoints for inference:

### Chat Completions
```
POST /v1/chat/completions
```

Request Body:
```json
{
  "model": "namespace/model-name",
  "messages": [
    {"role": "user", "content": "Hello!"}
  ]
}
```

### Embeddings
```
POST /v1/embeddings
```

Request Body:
```json
{
  "model": "namespace/model-name",
  "input": "text to embed"
}
```

### List Models
```
GET /v1/models
GET /v1/models/{model}
```

## MCP Resources

### List MCP Resources
```
GET /v1/mcp/resources
```
