# PUT /spaces/{namespace}/{name}

**Resource:** [Space](../resources/Space.md)
**Update a exists space**
**Operation ID:** `put--spaces-{namespace}-{name}`

update a exists space

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | Yes | current_user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateSpaceReq](../schemas/types-UpdateSpaceReq/types-UpdateSpaceReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
