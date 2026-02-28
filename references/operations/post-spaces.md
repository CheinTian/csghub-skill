# POST /spaces

**Resource:** [Space](../resources/Space.md)
**Create a new space**
**Operation ID:** `post--spaces`

create a new space

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | Yes | current_user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateSpaceReq](../schemas/types-CreateSpaceReq/types-CreateSpaceReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
