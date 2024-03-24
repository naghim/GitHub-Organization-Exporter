# GitHub Organization Exporter

Donwload any content from GitHub organizations that you have access to. This includes GitHub Classrooms as well.

## How to use

1. Enable fine-grained access tokens on the profile of the organization you would like to export.

2. Create a [GitHub personal access token](https://github.com/settings/tokens?type=beta) on your account. Add access to the organization you would like to export, using `All repositories` repository access, and the following `Repository permissions`:

- `Contents`: Read-only
- `Metadata`: Read-only

3. Create a `github.json` file, containing the name of the organization and the token you've just created:

```json
[
  {
    "token": "github_pat_AAA_BBB",
    "organization": "student-organization"
  }
]
```

You can create/add multiple organizations this way.

4. Install the Python requirements:

```bash
python -m pip install -r requirements.txt
```

5. Run the project and choose the organization to download all repositories from:

```bash
python download_github.py
```
