# GET /accounting/multisync/download

**Resource:** [Accounting](../resources/Accounting.md)
**Get account quota statement**
**Operation ID:** `get--accounting-multisync-download`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `repo_path` | query | string | Yes | repo path |
| `repo_type` | query | string | Yes | repo type |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
