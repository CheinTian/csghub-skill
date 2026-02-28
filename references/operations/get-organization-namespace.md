# GET /organization/{namespace}

**Resource:** [Organization](../resources/Organization.md)
**Get organization info**
**Operation ID:** `get--organization-{namespace}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | the op user |
| `namespace` | path | string | Yes | namespace |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
