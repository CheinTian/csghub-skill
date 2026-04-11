# GET /api/v1/sandboxes/{sandbox_name}/status/sse

**Resource:** [Sandbox](../resources/Sandbox.md)
**Stream sandbox status updates**
**Operation ID:** `get--api-v1-sandboxes-{sandbox_name}-status-sse`

Establishes a Server-Sent Events (SSE) connection to stream real-time status updates for a specific sandbox. The connection sends status updates every second until the client disconnects or an error occurs. Each event contains either a "status" event with the current sandbox state or an "error" event if retrieval fails.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `sandbox_name` | path | string | Yes | Sandbox name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | Stream of sandbox status updates sent as Server-Sent Events. Each event is formatted as:\n\n- Status update: `event: status\\ndata: {\"spec\": {...}, \"state\": {...}}\\n\\n`\n- Error event: `event: error\\ndata: \"error message\"\\n\\n` |
| 400 | Bad request - sandbox name is required or invalid |
| 401 | Unauthorized - authentication required |
| 403 | Forbidden - current user does not have permission to access this sandbox |
| 404 | Sandbox not found |
| 500 | Internal server error - failed to establish SSE connection or retrieve sandbox status |

## Security

- **ApiKey**
