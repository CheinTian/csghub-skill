# PUT /mirror_namespace_mappings/{id}

**Resource:** [Mirror](../resources/Mirror.md)
**Update mirror namespace mapping, used for admin**
**Operation ID:** `put--mirror_namespace_mappings-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateMirrorNamespaceMappingReq](../schemas/types-UpdateMirrorNamespaceMappingReq/types-UpdateMirrorNamespaceMappingReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
