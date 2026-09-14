# Architecture

The presentation's model-structure slide shows a sequence from user question -> student JSON profile -> restrictions/personalization -> text-or-image decision -> answer -> UI display.

```mermaid
flowchart TD
    A[Student enters a question] --> B[Load optional student_profile.json]
    B --> C[Combine counselor instructions + relevant profile context]
    C --> D{Explicit !image request?}
    D -- No --> E[Chat completion]
    D -- Yes --> F[Image generation]
    E --> G[Store response in Streamlit session state]
    F --> G
    G --> H[Display response in Streamlit UI]
```

## Components

- **Streamlit UI:** chat input, message display, image display, and clear-conversation control.
- **Student profile:** optional local JSON context.
- **Counselor instructions:** focus on guidance and avoid writing application submissions for students.
- **Text generation:** normal questions are sent through the chat path.
- **Image generation:** requests beginning with `!image` use the image path.
