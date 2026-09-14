# Changes from the classroom prototype

This repository keeps the core project idea and behavior while making the code safer and cleaner for a public portfolio.

## Security/privacy changes

- Removed the hard-coded API credential from `app.py`.
- Read `OPENAI_API_KEY` from the environment instead.
- Excluded `student_profile.json` from Git.
- Added a public example profile.
- Added a public-safe presentation copy that omits the team slide containing current school/location/age details and a personal photo.

## Code cleanup

- Removed duplicate/unneeded imports.
- Made image generation explicit with a `!image` prefix.
- Added a clear error when the API key is missing.
- Added error handling for image generation.
- Preserved student-profile context after clearing the conversation.
- Added a short responsible-use notice in the UI.

These are portfolio-hardening changes, not a claim that they were all part of the original classroom submission.
