# types.ImageGenerationResponse

**Type:** object

## Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `background` | object | No | The background parameter used for the image generation. Either `transparent` or
`opaque`.

Any of "transparent", "opaque". |
| `created` | integer | No | The Unix timestamp (in seconds) of when the image was created. |
| `data` | openai.Image[] | No | The list of generated images. |
| `output_format` | object | No | The output format of the image generation. Either `png`, `webp`, or `jpeg`.

Any of "png", "webp", "jpeg". |
| `quality` | object | No | The quality of the image generated. Either `low`, `medium`, or `high`.

Any of "low", "medium", "high". |
| `size` | object | No | The size of the image generated. Either `1024x1024`, `1024x1536`, or
`1536x1024`.

Any of "1024x1024", "1024x1536", "1536x1024". |
| `usage` | object | No | For `gpt-image-1` only, the token usage information for the image generation. |

