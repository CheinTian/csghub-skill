# POST /skills

**Resource:** [Skill](../resources/Skill.md)
**Create a new skill**
**Operation ID:** `post--skills`

create a new skill

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user, the owner |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateSkillReq](../schemas/types-CreateSkillReq/types-CreateSkillReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
