# GET /accounting/subscriptions/status/batch

**Resource:** [Accounting](../resources/Accounting.md)
**Get a bunch of subscriptions status**
**Operation ID:** `get--accounting-subscriptions-status-batch`

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.SubscriptionBatchStatusReq](../schemas/types-SubscriptionBatchStatusReq/types-SubscriptionBatchStatusReq.md)

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
