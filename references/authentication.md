## Authentication

All requests must include the following header:

Authorization: Bearer {CSGHUB_USER_TOKEN}

Where:
- `CSGHUB_USER_TOKEN` is an environment variable.

Rules:
1. Treat `CSGHUB_USER_TOKEN` as the single source of truth.
2. Do not hardcode or fabricate tokens.
3. Do not proceed without this header.
4. If unavailable, explicitly report an authentication failure.
