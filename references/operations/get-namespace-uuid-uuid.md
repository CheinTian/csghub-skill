# GET /namespace/uuid/{uuid}

**Resource:** [InternalOnly](../resources/InternalOnly.md)
**Get namespace info by UUID [Internal Only].**
**Operation ID:** `get--namespace-uuid-{uuid}`

get namespace info by uuid

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `uuid` | path | string | Yes | namespace uuid |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
