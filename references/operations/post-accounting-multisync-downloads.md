# POST /accounting/multisync/downloads

**Resource:** [Accounting](../resources/Accounting.md)
**Add download count**
**Operation ID:** `post--accounting-multisync-downloads`

## Parameters

| Name | In | Type | Required | Description |
|------|------|------|----------|-------------|
| `current_user` | query | string | Yes | current_user |

## Request Body

body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.AcctQuotaStatementReq](../schemas/types-AcctQuotaStatementReq/types-AcctQuotaStatementReq.md)

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
