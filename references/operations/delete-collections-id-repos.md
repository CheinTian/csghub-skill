# DELETE /collections/{id}/repos

**Resource:** [Collection](../resources/Collection.md)
**remove repos from a collection**
**Operation ID:** `delete--collections-{id}-repos`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `id` | path | string | Yes | id |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UpdateCollectionReposReq](../schemas/types-UpdateCollectionReposReq/types-UpdateCollectionReposReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

## Security

- **JWT token**
