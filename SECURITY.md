# Security and privacy

## API credential

The original classroom source contained an OpenAI API credential directly in the Python file. That credential is **not** included in this public-repository version.

Before publishing:

1. Revoke/rotate the credential that appeared in the original source if it is still active.
2. Keep the replacement credential outside the repository.
3. Set it through the `OPENAI_API_KEY` environment variable when running locally.
4. Do not commit `.env`, Streamlit secrets, screenshots containing credentials, or shell history containing credentials.

Deleting a secret from the latest version of a file is not sufficient if it was already committed to Git history.

## Student-profile privacy

`student_profile.json` may contain personal information. It is excluded by `.gitignore`. Only `student_profile.example.json` should be public.

## Presentation privacy

The original presentation includes a team-introduction slide with a personal photo plus current school/location/age details. The Git-ready repository contains a public-safe presentation with that slide removed.
