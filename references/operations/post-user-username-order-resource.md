# POST /user/{username}/order/resource

**Resource:** [User](../resources/User.md)
**create order for user's resource**
**Operation ID:** `post--user-{username}-order-resource`

## Request Body

create order request

**Required:** Yes

**Content Types:** `application/json`

**Schema:** [types.CreateUserResourceReq](../schemas/types-CreateUserResourceReq/types-CreateUserResourceReq.md)

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
