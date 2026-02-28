# GET /agent/instances/status

**Resource:** [Agent](../resources/Agent.md)
**Get status for multiple agent instances with SSE**
**Operation ID:** `get--agent-instances-status`

Monitor status of multiple agent instances using Server-Sent Events. Each event contains status update for a single instance.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `monitor_id` | query | string | Yes | Monitor UUID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | SSE stream with status updates |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
