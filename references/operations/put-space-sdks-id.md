# PUT /space_sdks/{id}

**Resource:** [SpaceSdk](../resources/SpaceSdk.md)
**Update a exist space sdk**
**Operation ID:** `put--space_sdks-{id}`

update a exist space sdk

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateSpaceSdkReq](../schemas/types-UpdateSpaceSdkReq/types-UpdateSpaceSdkReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
