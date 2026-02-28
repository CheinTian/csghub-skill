# POST /collections

**Resource:** [Collection](../resources/Collection.md)
**create a collection**
**Operation ID:** `post--collections`

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
