# Git check-in steps for AJ's Windows computer

Target parent folder:

```text
C:\Users\ajayg\Github
```

Recommended repository folder:

```text
C:\Users\ajayg\Github\WPI-Frontiers-2026-AI-College-Counselor
```

## 1. Extract the ZIP
Extract `WPI-Frontiers-2026-AI-College-Counselor.zip` directly under `C:\Users\ajayg\Github`.

## 2. Open PowerShell in the repository

```powershell
cd C:\Users\ajayg\Github\WPI-Frontiers-2026-AI-College-Counselor
```

## 3. Initialize Git

```powershell
git init
git branch -M main
```

## 4. Stage and review

```powershell
git add .
git status
```

Confirm that a real `student_profile.json` and any API key are **not** being staged.

## 5. First commit

```powershell
git commit -m "Add WPI Frontiers 2026 AI college counselor project"
```

## 6. Create an empty GitHub repository
Suggested name: `wpi-frontiers-ai-college-counselor`

Suggested description: `WPI Frontiers 2026 team project: a Python and Streamlit conversational AI prototype for college-admissions guidance.`

Do not ask GitHub to pre-create a README, `.gitignore`, or license because those files are already included.

## 7. Connect and push

```powershell
git remote add origin https://github.com/YOUR-GITHUB-USERNAME/wpi-frontiers-ai-college-counselor.git
git remote -v
git push -u origin main
```

## Future changes: use branches

```powershell
git checkout -b update/readme-demo
git add .
git commit -m "Improve project demo and documentation"
git push -u origin update/readme-demo
```
