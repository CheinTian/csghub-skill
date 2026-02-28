# types.MCPToolSchema

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `$schema` | string | No | JSON Schema for the tool's input data structure |
| `additionalProperties` | boolean | No | Optional, indicates if additional properties are allowed |
| `properties` | object | No |  |
| `required` | string[] | No | Optional, list of required properties |
| `type` | object | No | Should be "object" for a schema representing an object with properties. Optional, but recommended for clarity. |

