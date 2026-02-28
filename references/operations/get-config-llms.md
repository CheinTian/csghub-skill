# GET /config/llms

**Resource:** [LLMService](../resources/LLMService.md)
**Get LLM Config**
**Operation ID:** `get--config-llms`

Get LLMConfig in database. Return a list of LLM configurations with optional filtering by keyword and type.

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `page` | query | integer | No | define which batch of results to retrieve |
| `per` | query | integer | No | define the batch size to return in a single response |
| `keyword` | query | string | No | search in model_name |
| `type` | query | integer | No | search in type (e.g., 1: optimization, 2: comparison) |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

