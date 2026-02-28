# Accounting

## Operations

| Method | Path | Summary | Details |
|--------|------|---------|----------|
| GET | `/accounting/credit/balance` | Get all users balance | [View](../operations/get-accounting-credit-balance.md) |
| PUT | `/accounting/credit/low-balance-warn` | Set low balance warning threshold | [View](../operations/put-accounting-credit-low-balance-warn.md) |
| GET | `/accounting/credit/{id}/balance` | Get user balance by user uuid | [View](../operations/get-accounting-credit-id-balance.md) |
| GET | `/accounting/credit/{id}/bills` | List user bills by user uuid and start date and end date | [View](../operations/get-accounting-credit-id-bills.md) |
| PUT | `/accounting/credit/{id}/recharge` | Recharge fee for account | [View](../operations/put-accounting-credit-id-recharge.md) |
| GET | `/accounting/credit/{id}/recharge/list` | List recharges by user uuid and start time and end time | [View](../operations/get-accounting-credit-id-recharge-list.md) |
| GET | `/accounting/credit/{id}/statements` | List statements by user uuid and start time and end time | [View](../operations/get-accounting-credit-id-statements.md) |
| GET | `/accounting/metering/{id}/statements` | List meterings by user uuid and start time and end time | [View](../operations/get-accounting-metering-id-statements.md) |
| GET | `/accounting/multisync/download` | Get account quota statement | [View](../operations/get-accounting-multisync-download.md) |
| POST | `/accounting/multisync/downloads` | Add download count | [View](../operations/post-accounting-multisync-downloads.md) |
| GET | `/accounting/multisync/quota` | Get account quota by user id | [View](../operations/get-accounting-multisync-quota.md) |
| POST | `/accounting/multisync/quotas` | Add or update account quota | [View](../operations/post-accounting-multisync-quotas.md) |
| GET | `/accounting/price` | List sku prices | [View](../operations/get-accounting-price.md) |
| POST | `/accounting/price` | Add sku price | [View](../operations/post-accounting-price.md) |
| GET | `/accounting/price/{id}` | Get price by id | [View](../operations/get-accounting-price-id.md) |
| PUT | `/accounting/price/{id}` | Update sku price | [View](../operations/put-accounting-price-id.md) |
| DELETE | `/accounting/price/{id}` | Delete price by id | [View](../operations/delete-accounting-price-id.md) |
| POST | `/accounting/recharge/create-pay-order` | Create recharge order | [View](../operations/post-accounting-recharge-create-pay-order.md) |
| GET | `/accounting/recharge/list` | List recharges by user name, order no, status, payment type and time range | [View](../operations/get-accounting-recharge-list.md) |
| GET | `/accounting/recharge/user-recharge-list` | List current user recharge list by start_time and end_time and query | [View](../operations/get-accounting-recharge-user-recharge-list.md) |
| GET | `/accounting/recharge/{id}/status` | Fetch recharge order status by recharge id | [View](../operations/get-accounting-recharge-id-status.md) |
| GET | `/accounting/recharges` | List recharges by user name, order no, status, payment type and time range | [View](../operations/get-accounting-recharges.md) |
| GET | `/accounting/statements` | List statements by user name, instance name, scene and time range | [View](../operations/get-accounting-statements.md) |
| GET | `/accounting/stripe/pay/cancel` | Mark stripe pay session as cancel | [View](../operations/get-accounting-stripe-pay-cancel.md) |
| GET | `/accounting/stripe/pay/sessions` | List pay sessions by user uuid and start time and end time | [View](../operations/get-accounting-stripe-pay-sessions.md) |
| POST | `/accounting/stripe/pay/sessions` | Create stripe pay session | [View](../operations/post-accounting-stripe-pay-sessions.md) |
| GET | `/accounting/stripe/pay/sessions/{id}` | Get a stripe pay session | [View](../operations/get-accounting-stripe-pay-sessions-id.md) |
| DELETE | `/accounting/stripe/pay/sessions/{id}` | Close a stripe pay session | [View](../operations/delete-accounting-stripe-pay-sessions-id.md) |
| GET | `/accounting/stripe/pay/success` | Mark stripe pay session as success | [View](../operations/get-accounting-stripe-pay-success.md) |
| GET | `/accounting/subscriptions` | List subscriptions by user uuid and start time and end time | [View](../operations/get-accounting-subscriptions.md) |
| POST | `/accounting/subscriptions` | Post a subscription change for a user | [View](../operations/post-accounting-subscriptions.md) |
| GET | `/accounting/subscriptions/bills` | List bills by user uuid and start time and end time | [View](../operations/get-accounting-subscriptions-bills.md) |
| GET | `/accounting/subscriptions/status` | Get user subscription status | [View](../operations/get-accounting-subscriptions-status.md) |
| GET | `/accounting/subscriptions/status/batch` | Get a bunch of subscriptions status | [View](../operations/get-accounting-subscriptions-status-batch.md) |
| GET | `/accounting/weekly_recharges` | Trigger weekly recharges calculation | [View](../operations/get-accounting-weekly-recharges.md) |
