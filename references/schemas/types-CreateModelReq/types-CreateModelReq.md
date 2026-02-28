# types.CreateModelReq

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `admin` | string | No | Admin user |
| `base_model` | string | No |  |
| `commit_files` | types.CommitFile[] | No | Files to commit |
| `default_branch` | string | No | The default branch of the repository |
| `description` | string | No | A description for the repository |
| `high_risk_count` | integer | No |  |
| `license` | string | No | The license for the repository |
| `medium_risk_count` | integer | No |  |
| `name` | string | No | The name of the repository |
| `namespace` | string | No | The namespace of the repository, which can be a user or an organization |
| `nickname` | string | No | The display name of the repository |
| `private` | boolean | No | Whether the repository is private |
| `report_url` | string | No |  |
| `star_count` | integer | No | Star count |
| `tool_count` | integer | No | Tool count |
| `type` | object | No | The type of the repository |

