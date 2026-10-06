# Ethan Smith — Engineering Portfolio

A responsive, dependency-free static website for GitHub Pages. The site contains a homepage and four project pages, with original figures extracted from the supplied presentation. No API keys, Node packages or paid services are required.

## Start locally

Open `docs/index.html` directly in your browser, or run:

```sh
python3 build.py
python3 -m http.server 8000 --directory docs
```

Visit http://localhost:8000. Windows users can substitute `py` for `python3`.

## Publish on GitHub Pages

1. Extract this ZIP. Create a GitHub repository, for example `engineering-portfolio`.
2. Upload the CONTENTS of this folder into the repository root. Keep `build.py`, `projects.json`, `assets/`, `reports/`, `docs/`, `style.css`, and `.github/`. Hidden directories may not be visible in a file picker; a terminal or VS Code git upload includes `.github/`.
3. Ensure the default branch is `main`.
4. In the repository, open **Settings → Pages → Build and deployment → Source → GitHub Actions**.
5. Open **Actions → Build and deploy portfolio → Run workflow** if deployment has not already started.
6. When it finishes, the Pages settings and deployment job show your published URL.

Alternative without a workflow: choose **Deploy from a branch**, select `main` and `/docs`. After every change, run `python3 build.py` locally and commit the updated docs folder. Relative links work both at `username.github.io/` and `username.github.io/engineering-portfolio/`.

Official guide: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

GitHub Pages publishes the site and its reports publicly. Include only reports you intend to share, removing private student details where necessary. The supplied structural-analysis PDF currently contains a student number on its cover; source PDFs are included unchanged. A shared coursework report should accurately credit the team.

## Add the report PDFs

The PowerPoint contains Google Drive hyperlinks, not embedded report files. All six supplied report PDFs are included in this package and connected to their project pages. To replace a report later, use these filenames in the ROOT `reports/` directory:

| Project report | Exact filename |
| --- | --- |
| Solar array group report | `solar-group-report.pdf` |
| Solar array manufacturing report | `solar-manufacturing-report.pdf` |
| Solar array technical report | `solar-technical-report.pdf` |
| Thermal comfort report | `thermal-comfort-report.pdf` |
| Lifting lug report | `lifting-lug-report.pdf` |
| SHM research report | `shm-report.pdf` |

The build automatically adds a report button only when its PDF exists. It generates a report page with the portfolio header, an embedded PDF reader and download/open links. All report URLs stay on the site's domain. Some mobile browsers open PDFs in their own viewer; the direct-open link remains on the same site.

Commit the PDFs to `main` and the workflow rebuilds and deploys. No JavaScript or HTML edits are required. For branch deployment or local use, rerun `python3 build.py`.

## Edit content

- `projects.json`: project descriptions, metrics, captions and report names.
- `build.py`: homepage copy, templates and report integration.
- `style.css`: styling and mobile layout.
- `assets/`: source images. Add files here, then reference their names in projects.json.
- `docs/`: generated publishable website; do not edit generated files as your source.

There is no web upload form: upload reports through GitHub or add them locally and push. GitHub Pages is static hosting.

## Content decisions and items to confirm

- The latest PowerPoint's SHM results take precedence over older CV figures: −40 dB is 0.744 NARX / 0.991 LSTM; −45 dB is 0.511 / 0.814. Confirm these are the final results you intend to publish.
- The original duplicate SHM hyperlink has been replaced with Major_Project-8.pdf, labelled as the undergraduate team report. The summer NARX benchmark is distinguished from this earlier report.
- The unfinished personal drone project is excluded. The ongoing Shay reconstruction is described briefly on the homepage; add original renders before making it a visual case study.
- Solar deployment time, mass and energy values are labelled as calculations/estimates; adjust only if supported by physical tests.
- FEA verification and probability-of-detection wording have been clarified. The site does not claim a 99% safety guarantee.
- Project dates follow the supplied PowerPoint. Report identities were checked against their opening pages.
- No CV download or LinkedIn button has been added because a final publication-ready CV and confirmed profile address have not been supplied for this build.

Original report hyperlinks are retained in `source-report-links.md` as reference only; that file is not copied into the deployed site.
