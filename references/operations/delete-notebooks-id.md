# DELETE /notebooks/{id}

**Resource:** [Notebook](../resources/Notebook.md)
**Delete notebook**
**Operation ID:** `delete--notebooks-{id}`

delete notebook

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

[types.Response](../schemas/types-Response/types-Response.md)

