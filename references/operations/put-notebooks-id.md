# PUT /notebooks/{id}

**Resource:** [Notebook](../resources/Notebook.md)
**Update notebook**
**Operation ID:** `put--notebooks-{id}`

update notebook

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | notebook id |

## Request Body

body

**Content Types:** `application/json`

**Schema:** [types.UpdateNotebookReq](../schemas/types-UpdateNotebookReq/types-UpdateNotebookReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

