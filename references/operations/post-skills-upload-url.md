# POST /skills/upload_url

**Resource:** [Skill](../resources/Skill.md)
**Get skill package upload URL**
**Operation ID:** `post--skills-upload_url`

Get a presigned URL and form data for uploading skill package

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | current user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
