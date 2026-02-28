# PUT /space_resources/{id}

**Resource:** [SpaceReource](../resources/SpaceReource.md)
**Update a exist space resource**
**Operation ID:** `put--space_resources-{id}`

update a exist space resource

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateSpaceResourceReq](../schemas/types-UpdateSpaceResourceReq/types-UpdateSpaceResourceReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
