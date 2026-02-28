# Prompt

## Operations

| Method | Path | Summary | Details |
|--------|------|---------|----------|
| GET | `/prompts` | Get Visiable Prompt repos for current user | [View](../operations/get-prompts.md) |
| POST | `/prompts` | Create a new prompt repo | [View](../operations/post-prompts.md) |
| GET | `/prompts/conversations` | List conversations of user | [View](../operations/get-prompts-conversations.md) |
| POST | `/prompts/conversations` | Create new conversation | [View](../operations/post-prompts-conversations.md) |
| GET | `/prompts/conversations/{id}` | Get a conversation by uuid | [View](../operations/get-prompts-conversations-id.md) |
| PUT | `/prompts/conversations/{id}` | Update a conversation title | [View](../operations/put-prompts-conversations-id.md) |
| POST | `/prompts/conversations/{id}` | Submit a conversation message | [View](../operations/post-prompts-conversations-id.md) |
| DELETE | `/prompts/conversations/{id}` | Delete a conversation | [View](../operations/delete-prompts-conversations-id.md) |
| PUT | `/prompts/conversations/{id}/message/{msgid}/hate` | Hate a conversation message | [View](../operations/put-prompts-conversations-id-message-msgid-hate.md) |
| PUT | `/prompts/conversations/{id}/message/{msgid}/like` | Like a conversation message | [View](../operations/put-prompts-conversations-id-message-msgid-like.md) |
| PUT | `/prompts/conversations/{id}/summary` | Summarize a conversation title | [View](../operations/put-prompts-conversations-id-summary.md) |
| GET | `/prompts/{namespace}/{name}` | List prompts | [View](../operations/get-prompts-namespace-name.md) |
| PUT | `/prompts/{namespace}/{name}` | Update a exists prompt repo | [View](../operations/put-prompts-namespace-name.md) |
| DELETE | `/prompts/{namespace}/{name}` | Delete a exists prompt repo | [View](../operations/delete-prompts-namespace-name.md) |
| GET | `/prompts/{namespace}/{name}/branches` | Get the branches of prompt repository | [View](../operations/get-prompts-namespace-name-branches.md) |
| POST | `/prompts/{namespace}/{name}/prompt/file` | Create prompt in repo | [View](../operations/post-prompts-namespace-name-prompt-file.md) |
| PUT | `/prompts/{namespace}/{name}/prompt/file/{file_path}` | Update prompt in repo | [View](../operations/put-prompts-namespace-name-prompt-file-file-path.md) |
| DELETE | `/prompts/{namespace}/{name}/prompt/file/{file_path}` | Delete prompt in repo | [View](../operations/delete-prompts-namespace-name-prompt-file-file-path.md) |
| GET | `/prompts/{namespace}/{name}/prompt/view/{file_path}` | Get prompts by file | [View](../operations/get-prompts-namespace-name-prompt-view-file-path.md) |
| GET | `/prompts/{namespace}/{name}/relations` | Get prompt related assets | [View](../operations/get-prompts-namespace-name-relations.md) |
| PUT | `/prompts/{namespace}/{name}/relations` | Set model relation for prompt | [View](../operations/put-prompts-namespace-name-relations.md) |
| POST | `/prompts/{namespace}/{name}/relations/model` | add model relation for prompt, used for admin | [View](../operations/post-prompts-namespace-name-relations-model.md) |
| DELETE | `/prompts/{namespace}/{name}/relations/model` | delete model relation for prompt, used for admin | [View](../operations/delete-prompts-namespace-name-relations-model.md) |
| GET | `/prompts/{namespace}/{name}/tags` | Get the tags of prompt repository | [View](../operations/get-prompts-namespace-name-tags.md) |
| POST | `/prompts/{namespace}/{name}/tags/{category}` | update the tags of a certain category | [View](../operations/post-prompts-namespace-name-tags-category.md) |
| GET | `/prompts_info/{namespace}/{name}` | Prompt Detail | [View](../operations/get-prompts-info-namespace-name.md) |
