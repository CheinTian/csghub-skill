# GET /organization/{namespace}/members

**Resource:** [Member](../resources/Member.md)
**Get organization members. Org member can get more details.**
**Operation ID:** `get--organization-{namespace}-members`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | No | the op user |
| `namespace` | path | string | Yes | namespace |
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
