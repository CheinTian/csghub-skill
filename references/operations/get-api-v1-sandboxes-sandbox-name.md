# GET /api/v1/sandboxes/{sandbox_name}

**Resource:** [Sandbox](../resources/Sandbox.md)
**Get sandbox details**
**Operation ID:** `get--api-v1-sandboxes-{sandbox_name}`

Retrieves details of a specific sandbox

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `sandbox_name` | path | string | Yes | Sandbox name |

## Responses

| Status | Description |
|--------|-------------|
| 200 | Sandbox details |
| 404 | Sandbox not found |

**Success Response Schema:**

[opencsg_com_csghub-server_common_types.SandboxResponse](../schemas/opencsg/opencsg-com-csghub-server-common-types-SandboxResponse.md)

