# Repository

## Operations

| Method | Path | Summary | Details |
|--------|------|---------|----------|
| GET | `/admin/repos` | Get repo paths with search query | [View](../operations/get-admin-repos.md) |
| POST | `/admin/{repo_type}/{namespace}/{name}/change_path` | Change the namespace of a repository | [View](../operations/post-admin-repo-type-namespace-name-change-path.md) |
| GET | `/models/runtime_framework` | List repo runtime framework | [View](../operations/get-models-runtime-framework.md) |
| GET | `/models/{namespace}/{name}/finetune/{id}/logs/{instance}` | get finetune instance logs | [View](../operations/get-models-namespace-name-finetune-id-logs-instance.md) |
| POST | `/repos/batch_migrate_to_xnet` | Batch migrate all repos to Xnet | [View](../operations/post-repos-batch-migrate-to-xnet.md) |
| POST | `/repos/create` | Create a new repository, compatible with hf api | [View](../operations/post-repos-create.md) |
| GET | `/repos/migration_stats` | Get xnet migration statistics | [View](../operations/get-repos-migration-stats.md) |
| POST | `/repos/stop_all_migrate_to_xnet` | Stop all repo migrations to Xnet | [View](../operations/post-repos-stop-all-migrate-to-xnet.md) |
| POST | `/validate-yaml` | Validate yaml, compatible with hf api | [View](../operations/post-validate-yaml.md) |
| GET | `/{repo_type}/{namespace}/{name}/all_files` | Get all files of a repo | [View](../operations/get-repo-type-namespace-name-all-files.md) |
| GET | `/{repo_type}/{namespace}/{name}/blob/{file_path}` | Get the repo file information like size, content, sha etc | [View](../operations/get-repo-type-namespace-name-blob-file-path.md) |
| GET | `/{repo_type}/{namespace}/{name}/branches` | Get the branches of repository | [View](../operations/get-repo-type-namespace-name-branches.md) |
| GET | `/{repo_type}/{namespace}/{name}/commit/{commit_id}` | Get commit diff of repository and data field of response need to be decode with base64 | [View](../operations/get-repo-type-namespace-name-commit-commit-id.md) |
| POST | `/{repo_type}/{namespace}/{name}/commit/{revision}` | Create commit with batch files | [View](../operations/post-repo-type-namespace-name-commit-revision.md) |
| GET | `/{repo_type}/{namespace}/{name}/commits` | Get all commits of repository | [View](../operations/get-repo-type-namespace-name-commits.md) |
| GET | `/{repo_type}/{namespace}/{name}/diff` | Get commit diff of repository and data field of response need to be decode with base64 | [View](../operations/get-repo-type-namespace-name-diff.md) |
| GET | `/{repo_type}/{namespace}/{name}/download/{file_path}` | Download a repo file [Depricated: use 'resolve' api instead] | [View](../operations/get-repo-type-namespace-name-download-file-path.md) |
| PUT | `/{repo_type}/{namespace}/{name}/incr_downloads` | Increase repo download count by 1 | [View](../operations/put-repo-type-namespace-name-incr-downloads.md) |
| GET | `/{repo_type}/{namespace}/{name}/last_commit` | Get the last commit of repository | [View](../operations/get-repo-type-namespace-name-last-commit.md) |
| POST | `/{repo_type}/{namespace}/{name}/migrate_to_xnet` | Migrate repo to Xnet | [View](../operations/post-repo-type-namespace-name-migrate-to-xnet.md) |
| GET | `/{repo_type}/{namespace}/{name}/migrate_to_xnet_progress` | Migrate repo to Xnet progress | [View](../operations/get-repo-type-namespace-name-migrate-to-xnet-progress.md) |
| GET | `/{repo_type}/{namespace}/{name}/mirror` | Get a mirror | [View](../operations/get-repo-type-namespace-name-mirror.md) |
| PUT | `/{repo_type}/{namespace}/{name}/mirror` | Update a mirror for a existing repository | [View](../operations/put-repo-type-namespace-name-mirror.md) |
| POST | `/{repo_type}/{namespace}/{name}/mirror` | Create mirror for a existing repository | [View](../operations/post-repo-type-namespace-name-mirror.md) |
| DELETE | `/{repo_type}/{namespace}/{name}/mirror` | Delete a mirror | [View](../operations/delete-repo-type-namespace-name-mirror.md) |
| GET | `/{repo_type}/{namespace}/{name}/mirror/progress` | Get Mirror sync progress | [View](../operations/get-repo-type-namespace-name-mirror-progress.md) |
| POST | `/{repo_type}/{namespace}/{name}/mirror/sync` | Triggers the mirror synchronization | [View](../operations/post-repo-type-namespace-name-mirror-sync.md) |
| POST | `/{repo_type}/{namespace}/{name}/mirror_from_saas` | Mirror repo from OpenCSG Saas(only on-premises) | [View](../operations/post-repo-type-namespace-name-mirror-from-saas.md) |
| POST | `/{repo_type}/{namespace}/{name}/preupload/{revision}` | Get upload mode for files | [View](../operations/post-repo-type-namespace-name-preupload-revision.md) |
| GET | `/{repo_type}/{namespace}/{name}/raw/{file_path}` | Get the last commit of repository | [View](../operations/get-repo-type-namespace-name-raw-file-path.md) |
| PUT | `/{repo_type}/{namespace}/{name}/raw/{file_path}` | Update existing file in repository | [View](../operations/put-repo-type-namespace-name-raw-file-path.md) |
| POST | `/{repo_type}/{namespace}/{name}/raw/{file_path}` | Create a new file in repository | [View](../operations/post-repo-type-namespace-name-raw-file-path.md) |
| DELETE | `/{repo_type}/{namespace}/{name}/raw/{file_path}` | Delete existing file in repository | [View](../operations/delete-repo-type-namespace-name-raw-file-path.md) |
| GET | `/{repo_type}/{namespace}/{name}/refs/{ref}/logs_tree/{path}` | Get last commit for file tree | [View](../operations/get-repo-type-namespace-name-refs-ref-logs-tree-path.md) |
| GET | `/{repo_type}/{namespace}/{name}/refs/{ref}/remote_tree/{path}` | Get file tree | [View](../operations/get-repo-type-namespace-name-refs-ref-remote-tree-path.md) |
| GET | `/{repo_type}/{namespace}/{name}/refs/{ref}/tree/{path}` | Get file tree | [View](../operations/get-repo-type-namespace-name-refs-ref-tree-path.md) |
| GET | `/{repo_type}/{namespace}/{name}/remote_diff` | Get diff between local last commit and remote commit | [View](../operations/get-repo-type-namespace-name-remote-diff.md) |
| GET | `/{repo_type}/{namespace}/{name}/resolve/{file_path}` | Download a rep file | [View](../operations/get-repo-type-namespace-name-resolve-file-path.md) |
| GET | `/{repo_type}/{namespace}/{name}/run` | List repo deploys | [View](../operations/get-repo-type-namespace-name-run.md) |
| GET | `/{repo_type}/{namespace}/{name}/run/{id}` | Get repo deploy detail | [View](../operations/get-repo-type-namespace-name-run-id.md) |
| PUT | `/{repo_type}/{namespace}/{name}/run/{id}` | Update deploy parameters | [View](../operations/put-repo-type-namespace-name-run-id.md) |
| GET | `/{repo_type}/{namespace}/{name}/run/{id}/logs/{instance}` | get deploy instance logs | [View](../operations/get-repo-type-namespace-name-run-id-logs-instance.md) |
| GET | `/{repo_type}/{namespace}/{name}/run/{id}/status` | get deploy status | [View](../operations/get-repo-type-namespace-name-run-id-status.md) |
| GET | `/{repo_type}/{namespace}/{name}/serverless/{id}/versions/{commit_id}` | get serverless logs by version (commitid) | [View](../operations/get-repo-type-namespace-name-serverless-id-versions-commit-id.md) |
| POST | `/{repo_type}/{namespace}/{name}/stop_migrate_to_xnet` | Stop single repo migration to Xnet | [View](../operations/post-repo-type-namespace-name-stop-migrate-to-xnet.md) |
| GET | `/{repo_type}/{namespace}/{name}/tags` | Get the tags of repository | [View](../operations/get-repo-type-namespace-name-tags.md) |
| POST | `/{repo_type}/{namespace}/{name}/tags/{category}` | update the tags of a certain category | [View](../operations/post-repo-type-namespace-name-tags-category.md) |
| GET | `/{repo_type}/{namespace}/{name}/tree` | Get repository file tree | [View](../operations/get-repo-type-namespace-name-tree.md) |
