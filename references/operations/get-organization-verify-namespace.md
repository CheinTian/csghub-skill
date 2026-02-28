# GET /organization/verify/{namespace}

**Resource:** [OrganizationVerify](../resources/OrganizationVerify.md)
**Get organization verification**
**Operation ID:** `get--organization-verify-{namespace}`

get organization verification info by organization ID

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
