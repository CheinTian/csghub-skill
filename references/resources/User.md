# User

## Operations

| Method | Path | Summary | Details |
|--------|------|---------|----------|
| GET | `/internal/user/emails` | Get all user emails for internal services | [View](../operations/get-internal-user-emails.md) |
| POST | `/user/email-verification-code/{email}` | GenerateVerificationCodeAndSendEmail | [View](../operations/post-user-email-verification-code-email.md) |
| GET | `/user/emails` | Get all user emails | [View](../operations/get-user-emails.md) |
| PUT | `/user/labels` | Update user labels | [View](../operations/put-user-labels.md) |
| PUT | `/user/phone` | Update current user phone | [View](../operations/put-user-phone.md) |
| POST | `/user/public/sms-code` | generate sms verification code and send it by sms (public endpoint) | [View](../operations/post-user-public-sms-code.md) |
| POST | `/user/public/sms-code/verify` | verify sms verification code (public endpoint) | [View](../operations/post-user-public-sms-code-verify.md) |
| POST | `/user/sms-code` | generate sms verification code and send it by sms | [View](../operations/post-user-sms-code.md) |
| POST | `/user/tags` | ResetUserTags | [View](../operations/post-user-tags.md) |
| GET | `/user/user_uuids` | Get user UUIDs | [View](../operations/get-user-user-uuids.md) |
| PUT | `/user/{id}` | Update user. If change user name, should only send 'new_username' in the request body. | [View](../operations/put-user-id.md) |
| GET | `/user/{username}` | Get user info. Admin and the user self can see full info, other users can only see basic info. | [View](../operations/get-user-username.md) |
| DELETE | `/user/{username}` | Delete user | [View](../operations/delete-user-username.md) |
| DELETE | `/user/{username}/close_account` | Delete user | [View](../operations/delete-user-username-close-account.md) |
| GET | `/user/{username}/codes` | Get user codes | [View](../operations/get-user-username-codes.md) |
| GET | `/user/{username}/collections` | Get user's collections | [View](../operations/get-user-username-collections.md) |
| GET | `/user/{username}/datasets` | Get user datasets | [View](../operations/get-user-username-datasets.md) |
| GET | `/user/{username}/evaluations` | Get user evaluations | [View](../operations/get-user-username-evaluations.md) |
| GET | `/user/{username}/finetune/instances` | Get user running notebook instances | [View](../operations/get-user-username-finetune-instances.md) |
| GET | `/user/{username}/finetune/jobs` | Get user backend fintunes | [View](../operations/get-user-username-finetune-jobs.md) |
| GET | `/user/{username}/likes/codes` | Get user likes codes | [View](../operations/get-user-username-likes-codes.md) |
| GET | `/user/{username}/likes/collections` | Get user likes collections | [View](../operations/get-user-username-likes-collections.md) |
| PUT | `/user/{username}/likes/collections/{id}` | Add collection likes | [View](../operations/put-user-username-likes-collections-id.md) |
| DELETE | `/user/{username}/likes/collections/{id}` | delete collection likes | [View](../operations/delete-user-username-likes-collections-id.md) |
| GET | `/user/{username}/likes/datasets` | Get user likes datasets | [View](../operations/get-user-username-likes-datasets.md) |
| GET | `/user/{username}/likes/mcps` | Get user likes mcp servers | [View](../operations/get-user-username-likes-mcps.md) |
| GET | `/user/{username}/likes/models` | Get user likes models | [View](../operations/get-user-username-likes-models.md) |
| GET | `/user/{username}/likes/skills` | Get user likes skills | [View](../operations/get-user-username-likes-skills.md) |
| GET | `/user/{username}/likes/spaces` | Get user likes spaces | [View](../operations/get-user-username-likes-spaces.md) |
| PUT | `/user/{username}/likes/{repoid}` | Add user likes | [View](../operations/put-user-username-likes-repoid.md) |
| DELETE | `/user/{username}/likes/{repoid}` | Delete user likes | [View](../operations/delete-user-username-likes-repoid.md) |
| GET | `/user/{username}/mcps` | Get user mcp servers | [View](../operations/get-user-username-mcps.md) |
| GET | `/user/{username}/models` | Get user models | [View](../operations/get-user-username-models.md) |
| GET | `/user/{username}/notebooks` | get user's notebooks | [View](../operations/get-user-username-notebooks.md) |
| POST | `/user/{username}/order/resource` | create order for user's resource | [View](../operations/post-user-username-order-resource.md) |
| GET | `/user/{username}/order/resources` | get user's resource | [View](../operations/get-user-username-order-resources.md) |
| DELETE | `/user/{username}/order/resources/{id}` | delete user's resource by order detail id | [View](../operations/delete-user-username-order-resources-id.md) |
| GET | `/user/{username}/prompts` | Get user prompts | [View](../operations/get-user-username-prompts.md) |
| GET | `/user/{username}/run/serverless` | Get serverless deploys | [View](../operations/get-user-username-run-serverless.md) |
| GET | `/user/{username}/run/{repo_type}` | Get user running deploys | [View](../operations/get-user-username-run-repo-type.md) |
| GET | `/user/{username}/spaces` | Get user spaces | [View](../operations/get-user-username-spaces.md) |
| GET | `/users` | Get users info. Only Admin | [View](../operations/get-users.md) |
| GET | `/users/by-uuids` | Find users by UUIDs | [View](../operations/get-users-by-uuids.md) |
| GET | `/users/stream-export` | Export users info. Only Admin | [View](../operations/get-users-stream-export.md) |
| GET | `/{namespace}/{name}/xet-{permission}-token/{branch}` | Get xnet write token | [View](../operations/get-namespace-name-xet-permission-token-branch.md) |
