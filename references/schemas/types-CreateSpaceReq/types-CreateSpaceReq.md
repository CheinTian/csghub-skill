# types.CreateSpaceReq

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `admin` | string | No | Admin user |
| `cluster_id` | string | Yes |  |
| `commit_files` | types.CommitFile[] | No | Files to commit |
| `cover_image_url` | string | No |  |
| `default_branch` | string | No | The default branch of the repository |
| `description` | string | No | A description for the repository |
| `driver_version` | string | No |  |
| `env` | string | No |  |
| `license` | string | No | The license for the repository |
| `min_replica` | integer | No |  |
| `name` | string | No | The name of the repository |
| `namespace` | string | No | The namespace of the repository, which can be a user or an organization |
| `nickname` | string | No | The display name of the repository |
| `order_detail_id` | integer | No |  |
| `private` | boolean | No | Whether the repository is private |
| `resource_id` | integer | Yes |  |
| `sdk` | string | Yes |  |
| `sdk_version` | string | No |  |
| `secrets` | string | No |  |
| `star_count` | integer | No | Star count |
| `template` | string | No |  |
| `tool_count` | integer | No | Tool count |
| `type` | object | No | The type of the repository |
| `variables` | string | No |  |

