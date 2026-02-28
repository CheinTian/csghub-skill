# PUT /space_templates/{id}

**Resource:** [SpaceTemplate](../resources/SpaceTemplate.md)
**Update a exist space template**
**Operation ID:** `put--space_templates-{id}`

update a exist space template

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | integer | Yes | id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateSpaceTemplateReq](../schemas/types-UpdateSpaceTemplateReq/types-UpdateSpaceTemplateReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
