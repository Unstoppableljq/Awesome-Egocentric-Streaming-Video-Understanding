# Publish to your personal GitHub

**This folder is a starter repository, not a repo published on GitHub yet.**

## Option A — GitHub CLI (recommended)

Ensure Git and [GitHub CLI](https://cli.github.com/) are installed. In a terminal, enter this folder:

```bash
cd awesome-ego-streaming-starter
gh auth login
git init -b main
git add .
git commit -m "Initial research-first awesome list"
gh repo create Awesome-Egocentric-Streaming-Video-Understanding --public --source=. --remote=origin --push
```

The last command creates a public repository in the **account authenticated with GitHub CLI**. It does not create it in someone else's account. Choose `--private` instead if you want to review before publishing. If Git asks you for an identity, configure `git config --global user.name` and `git config --global user.email` first.

## Option B — GitHub website

1. Visit https://github.com/new, choose your personal account, repository name `Awesome-Egocentric-Streaming-Video-Understanding`, public visibility, and **do not initialize** the repo with a GitHub README (one already exists here).
2. In this folder, run:

```bash
 git init -b main
 git add .
 git commit -m "Initial research-first awesome list"
 git remote add origin https://github.com/YOUR_GITHUB_USERNAME/Awesome-Egocentric-Streaming-Video-Understanding.git
 git push -u origin main
```

Replace `YOUR_GITHUB_USERNAME` with your own GitHub username. HTTPS pushes may require authentication via a credential manager, GitHub CLI, or token; account passwords do not work.

## Maintain

Edit `data/papers.json` (the source of truth) and then run:

```bash
python scripts/build_readme.py
python scripts/build_readme.py --check
```

The included GitHub Actions workflow checks consistency in every push and pull request. It does **not** autonomously add papers or certify that their claims are true; the maintainer does that.

## Before public launch

- Replace any descriptions you disagree with after reading the full original paper.
- Choose and add a repo license (e.g. CC BY 4.0 for prose; MIT for code, if desired).
- Add your own GitHub profile/contact and acknowledgement section.
- Optionally put the repo in your pinned repositories, add GitHub Topics (`awesome-list`, `egocentric-video`, `streaming-video`, `multimodal-llm`, `video-understanding`).
