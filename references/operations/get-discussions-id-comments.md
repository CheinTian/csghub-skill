# GET /discussions/{id}/comments

**Resource:** [Discussion](../resources/Discussion.md)
**List discussion comments**
**Operation ID:** `get--discussions-{id}-comments`

list discussion comments

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | the discussion id |
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
