# GET /notebooks/{id}

**Resource:** [Notebook](../resources/Notebook.md)
**Get notebook**
**Operation ID:** `get--notebooks-{id}`

get notebook

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | notebook id |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.NotebookRes](../schemas/types-NotebookRes/types-NotebookRes.md)

