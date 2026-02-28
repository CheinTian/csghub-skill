# GET /v1/mcp/resources

**Resource:** [AIGateway](../resources/AIGateway.md)
**List recommanded mcp servers**
**Operation ID:** `get--v1-mcp-resources`

Returns a list of recommended mcp servers

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `per` | query | integer | No | per |
| `page` | query | integer | No | per page |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 500 | Internal server error |

## Security

- **ApiKey**
