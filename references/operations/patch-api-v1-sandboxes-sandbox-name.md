# PATCH /api/v1/sandboxes/{sandbox_name}

**Resource:** [Sandbox](../resources/Sandbox.md)
**Update sandbox configuration**
**Operation ID:** `patch--api-v1-sandboxes-{sandbox_name}`

Updates configuration of a specific sandbox

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `sandbox_name` | path | string | Yes | Sandbox name |

## Request Body

Sandbox update configuration

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.SandboxUpdateRequest](../schemas/types-SandboxUpdateRequest/types-SandboxUpdateRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | Sandbox updated successfully |
| 400 | Bad request |
| 403 | Forbidden |
| 404 | Sandbox not found |
| 500 | Internal server error |

**Success Response Schema:**

[opencsg_com_csghub-server_common_types.SandboxResponse](../schemas/opencsg/opencsg-com-csghub-server-common-types-SandboxResponse.md)

## Security

- **ApiKey**
