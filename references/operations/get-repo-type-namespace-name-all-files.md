# GET /{repo_type}/{namespace}/{name}/all_files

**Resource:** [Repository](../resources/Repository.md)
**Get all files of a repo**
**Operation ID:** `get--{repo_type}-{namespace}-{name}-all_files`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `namespace` | path | string | Yes | namespace |
| `name` | path | string | Yes | name |
| `current_user` | query | string | No | current user |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **ApiKey**
