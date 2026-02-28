# GET /accounting/multisync/quota

**Resource:** [Accounting](../resources/Accounting.md)
**Get account quota by user id**
**Operation ID:** `get--accounting-multisync-quota`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | Yes | current_user |

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
