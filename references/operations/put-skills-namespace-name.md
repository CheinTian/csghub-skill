# PUT /skills/{namespace}/{name}

**Resource:** [Skill](../resources/Skill.md)
**Update a exists skill**
**Operation ID:** `put--skills-{namespace}-{name}`

update a exists skill

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateSkillReq](../schemas/types-UpdateSkillReq/types-UpdateSkillReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
