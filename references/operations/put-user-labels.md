# PUT /user/labels

**Resource:** [User](../resources/User.md)
**Update user labels**
**Operation ID:** `put--user-labels`

Update the labels of a specified user

## Request Body

Update user labels body

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.UserLabelsRequest](../schemas/types-UserLabelsRequest/types-UserLabelsRequest.md)

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
