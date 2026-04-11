# v1.NodeSelectorTerm

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `matchExpressions` | v1.NodeSelectorRequirement[] | No | A list of node selector requirements by node's labels.
+optional
+listType=atomic |
| `matchFields` | v1.NodeSelectorRequirement[] | No | A list of node selector requirements by node's fields.
+optional
+listType=atomic |

