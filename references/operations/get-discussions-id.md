# GET /discussions/{id}

**Resource:** [Discussion](../resources/Discussion.md)
**Show a discussion and its comments with pagination**
**Operation ID:** `get--discussions-{id}`

show a discussion

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
