# GET /accounting/weekly_recharges

**Resource:** [Accounting](../resources/Accounting.md)
**Trigger weekly recharges calculation**
**Operation ID:** `get--accounting-weekly_recharges`

Trigger the accounting service to calculate and process weekly recharges.

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 500 | Internal server error |

**Success Response Schema:**

[types.Response](../schemas/types-Response/types-Response.md)

## Security

- **ApiKey**
