# POST /notebooks

**Resource:** [Notebook](../resources/Notebook.md)
**Create notebook**
**Operation ID:** `post--notebooks`

create notebook

## Request Body

body

**Content Types:** `application/json`

**Schema:** [types.CreateNotebookReq](../schemas/types-CreateNotebookReq/types-CreateNotebookReq.md)

## Responses

| Status | Description |
|--------|-------------|
| 200 | OK |
| 400 | Bad request |
| 500 | Internal server error |

**Success Response Schema:**

[types.NotebookRes](../schemas/types-NotebookRes/types-NotebookRes.md)

