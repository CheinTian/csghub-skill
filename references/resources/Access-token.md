# Access token

## Operations

| Method | Path | Summary | Details |
|--------|------|---------|----------|
| PUT | `/token/{app}/{token_name}` | Refresh a access token for a user | [View](../operations/put-token-app-token-name.md) |
| POST | `/token/{app}/{token_name}` | Create access token for an special application | [View](../operations/post-token-app-token-name.md) |
| DELETE | `/token/{app}/{token_name}` | Delete access token of a app | [View](../operations/delete-token-app-token-name.md) |
| GET | `/token/{token_value}` | Get token and owner's detail by the token value | [View](../operations/get-token-token-value.md) |
| GET | `/user/{username}/tokens` | Get all access tokens for a user | [View](../operations/get-user-username-tokens.md) |
| POST | `/user/{username}/tokens` | [Deprecated: use POST:/token/{app}/{username} instead] | [View](../operations/post-user-username-tokens.md) |
| GET | `/user/{username}/tokens/first` | Get or create first available access token for a user | [View](../operations/get-user-username-tokens-first.md) |
| DELETE | `/user/{username}/tokens/{token_name}` | [Deprecated: use DELETE:/token/{app}/{token_name} instead] | [View](../operations/delete-user-username-tokens-token-name.md) |
