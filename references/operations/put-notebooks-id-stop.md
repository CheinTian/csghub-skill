# PUT /notebooks/{id}/stop

**Resource:** [Notebook](../resources/Notebook.md)
**Stop notebook**
**Operation ID:** `put--notebooks-{id}-stop`

stop notebook

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

