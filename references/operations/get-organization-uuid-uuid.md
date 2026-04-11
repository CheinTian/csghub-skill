# GET /organization/uuid/{uuid}

**Resource:** [Organization](../resources/Organization.md)
**Get organization by UUID**
**Operation ID:** `get--organization-uuid-{uuid}`

get organization by UUID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `uuid` | path | string | Yes | organization uuid |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
