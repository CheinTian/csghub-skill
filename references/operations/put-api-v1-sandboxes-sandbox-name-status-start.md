# PUT /api/v1/sandboxes/{sandbox_name}/status/start

**Resource:** [Sandbox](../resources/Sandbox.md)
**Start a sandbox**
**Operation ID:** `put--api-v1-sandboxes-{sandbox_name}-status-start`

Starts a specific sandbox

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `sandbox_name` | path | string | Yes | Sandbox name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | Sandbox started successfully |
| 400 | Bad request |
| 403 | Forbidden |
| 404 | Sandbox not found |
| 500 | Internal server error |
| 503 | Service unavailable - insufficient resources, cluster unavailable, or resources unavailable |

**Success Response Schema:**

[opencsg_com_csghub-server_common_types.SandboxResponse](../schemas/opencsg/opencsg-com-csghub-server-common-types-SandboxResponse.md)

## Security

- **ApiKey**
