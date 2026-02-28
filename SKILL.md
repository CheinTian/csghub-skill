---
name: csghub-server-api
description: CSGHub Server API.. Use when working with the CSGHub Server API or when the user needs to interact with this API.
metadata:
  api-version: "1.0"
  openapi-version: "3.0.1"
---

# CSGHub Server API

CSGHub Server API.

## How to Use This Skill

This API documentation is split into multiple files for on-demand loading.

**Directory structure:**
```
references/
├── resources/      # 51 resource index files
├── operations/     # 509 operation detail files
└── schemas/        # 441 schema groups, 443 schema files
```

**Navigation flow:**
1. Find the resource you need in the list below
2. Read `references/resources/<resource>.md` to see available operations
3. Read `references/operations/<operation>.md` for full details
4. If an operation references a schema, read `references/schemas/<prefix>/<schema>.md`

## Base URL

- `http://opencsg-stg.com/api/v1`
- `https://opencsg-stg.com/api/v1`

## Authentication

Supported methods: **ApiKey**. See `references/authentication.md` for details.

## Resources

- **Agent** → `references/resources/Agent.md` (52 ops)
- **Repository** → `references/resources/Repository.md` (48 ops)
- **User** → `references/resources/User.md` (45 ops)
- **Model** → `references/resources/Model.md` (37 ops)
- **Accounting** → `references/resources/Accounting.md` (35 ops)
- **Prompt** → `references/resources/Prompt.md` (26 ops)
- **Mirror** → `references/resources/Mirror.md` (17 ops)
- **Accounting-Invoices** → `references/resources/Accounting-Invoices.md` (15 ops)
- **Cluster** → `references/resources/Cluster.md` (13 ops)
- **RuntimeFramework** → `references/resources/RuntimeFramework.md` (13 ops)
- **Organization** → `references/resources/Organization.md` (12 ops)
- **Space** → `references/resources/Space.md` (11 ops)
- **LLMService** → `references/resources/LLMService.md` (10 ops)
- **Notifications** → `references/resources/Notifications.md` (10 ops)
- **Discussion** → `references/resources/Discussion.md` (9 ops)
- **Dataset** → `references/resources/Dataset.md` (9 ops)
- **Notebook** → `references/resources/Notebook.md` (9 ops)
- **Tag** → `references/resources/Tag.md` (9 ops)
- **Collection** → `references/resources/Collection.md` (8 ops)
- **License** → `references/resources/License.md` (8 ops)
- **Access token** → `references/resources/Access-token.md` (8 ops)
- **MCP** → `references/resources/MCP.md` (7 ops)
- **Code** → `references/resources/Code.md` (6 ops)
- **Skill** → `references/resources/Skill.md` (6 ops)
- **Monitor** → `references/resources/Monitor.md` (6 ops)
- **ApiRateLimit** → `references/resources/ApiRateLimit.md` (5 ops)
- **Broadcasts** → `references/resources/Broadcasts.md` (5 ops)
- **Member** → `references/resources/Member.md` (5 ops)
- **SpaceTemplate** → `references/resources/SpaceTemplate.md` (5 ops)
- **AIGateway** → `references/resources/AIGateway.md` (5 ops)
- **Moderation** → `references/resources/Moderation.md` (4 ops)
- **StorageGateway** → `references/resources/StorageGateway.md` (4 ops)
- **Finetune** → `references/resources/Finetune.md` (4 ops)
- **SpaceReource** → `references/resources/SpaceReource.md` (4 ops)
- **SpaceSdk** → `references/resources/SpaceSdk.md` (4 ops)
- **Evaluation** → `references/resources/Evaluation.md` (3 ops)
- **Import** → `references/resources/Import.md` (3 ops)
- **Invitations** → `references/resources/Invitations.md` (3 ops)
- **List** → `references/resources/List.md` (3 ops)
- **OrganizationVerify** → `references/resources/OrganizationVerify.md` (3 ops)
- **Sync** → `references/resources/Sync.md` (3 ops)
- **UserVerify** → `references/resources/UserVerify.md` (3 ops)
- **SSH Key** → `references/resources/SSH-Key.md` (3 ops)
- **Captcha** → `references/resources/Captcha.md` (2 ops)
- **JWT** → `references/resources/JWT.md` (2 ops)
- **Stat** → `references/resources/Stat.md` (2 ops)
- **Events** → `references/resources/Events.md` (1 ops)
- **Namespace** → `references/resources/Namespace.md` (1 ops)
- **InternalOnly** → `references/resources/InternalOnly.md` (1 ops)
- **Recommendation** → `references/resources/Recommendation.md` (1 ops)
- **Telemetry** → `references/resources/Telemetry.md` (1 ops)
