# GET /invitations/activities

**Resource:** [Invitations](../resources/Invitations.md)
**List invitation activities of current inviter**
**Operation ID:** `get--invitations-activities`

list invitation activities of current inviter

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `status` | query | string | No | status |
| `start_date` | query | string | No | start_date |
| `end_date` | query | string | No | end_date |
| `per` | query | integer | No | per |
| `page` | query | integer | No | page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
