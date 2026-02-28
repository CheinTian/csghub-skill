# PUT /mirror/sources/{id}

**Resource:** [Mirror](../resources/Mirror.md)
**Update mirror source, used for admin**
**Operation ID:** `put--mirror-sources-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateMirrorSourceReq](../schemas/types-UpdateMirrorSourceReq/types-UpdateMirrorSourceReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
