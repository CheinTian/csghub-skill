# GET /space_resources

**Resource:** [SpaceReource](../resources/SpaceReource.md)
**Get space resources**
**Operation ID:** `get--space_resources`

get space resources

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `per` | query | integer | No | page size |
| `page` | query | integer | No | per page |
| `cluster_id` | query | string | No | cluster_id |
| `deploy_type` | query | enum: 0, 1, 2... | No | deploy type(0-space,1-inference,2-finetune,3-serverless,4-evaluation) |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
