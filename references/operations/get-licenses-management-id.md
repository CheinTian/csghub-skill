# GET /licenses/management/{id}

**Resource:** [License](../resources/License.md)
**Get a license by id**
**Operation ID:** `get--licenses-management-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |
| `create_license_file` | query | boolean | No | create license file |
| `current_user` | query | string | Yes | current user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
