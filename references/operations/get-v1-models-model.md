# GET /v1/models/{model}

**Resource:** [AIGateway](../resources/AIGateway.md)
**Get model details**
**Operation ID:** `get--v1-models-{model}`

Returns information about a specific model

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `model` | path | string | Yes | Model ID |

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 404 | Model not found |
| 500 | Internal server error |

**Success Response Schema:**

[opencsg_com_csghub-server_aigateway_types.Model](../schemas/opencsg/opencsg-com-csghub-server-aigateway-types-Model.md)

## Security

- **ApiKey**
