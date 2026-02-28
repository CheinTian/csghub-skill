# POST /accounting/subscriptions

**Resource:** [Accounting](../resources/Accounting.md)
**Post a subscription change for a user**
**Operation ID:** `post--accounting-subscriptions`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.SubscriptionUpdateReq](../schemas/types-SubscriptionUpdateReq/types-SubscriptionUpdateReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
