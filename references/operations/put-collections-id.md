# PUT /collections/{id}

**Resource:** [Collection](../resources/Collection.md)
**update a collection**
**Operation ID:** `put--collections-{id}`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateCollectionReq](../schemas/types-CreateCollectionReq/types-CreateCollectionReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **JWT token**
