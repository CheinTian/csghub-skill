# PUT /notebooks/{id}/wakeup

**Resource:** [Notebook](../resources/Notebook.md)
**Wakeup notebook**
**Operation ID:** `put--notebooks-{id}-wakeup`

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

