# openai.CompletionUsage

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `completion_tokens` | integer | No | Number of tokens in the generated completion. |
| `completion_tokens_details` | object | No | Breakdown of tokens used in a completion. |
| `prompt_tokens` | integer | No | Number of tokens in the prompt. |
| `prompt_tokens_details` | object | No | Breakdown of tokens used in the prompt. |
| `total_tokens` | integer | No | Total number of tokens used in the request (prompt + completion). |

