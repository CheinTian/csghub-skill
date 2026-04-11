# POST /api/v1/sandboxes

**Resource:** [Sandbox](../resources/Sandbox.md)
**Create sandbox**
**Operation ID:** `post--api-v1-sandboxes`

This endpoint creates a new sandbox for the currently logged-in user. It only completes the sandbox initialization (creates only, does not start the sandbox). Returns 409 conflict if a sandbox with the same name already exists.

## Request Body

Sandbox creation configuration parameters

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.SandboxCreateRequest](../schemas/types-SandboxCreateRequest/types-SandboxCreateRequest.md)

## Responses

| Status | Description |
|--------|-------------|
| 201 | Created successfully |
| 400 | Invalid request parameters - such as missing required parameters, incorrect parameter format, etc. |
| 403 | Forbidden - current user does not have permission to create sandbox |
| 409 | Resource conflict - sandbox with the same name already exists |
| 500 | Internal server error - such as failure to create sandbox resources |
| 503 | Service unavailable - insufficient resources, cluster unavailable, or resources unavailable |

## Security

- **ApiKey**
