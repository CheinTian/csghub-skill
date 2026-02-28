# DELETE /organization/{namespace}

**Resource:** [Organization](../resources/Organization.md)
**Delete organization**
**Operation ID:** `delete--organization-{namespace}`

delete organization

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `current_user` | query | string | No | the op user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
