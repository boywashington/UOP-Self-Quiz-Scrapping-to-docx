# UoPeople Quiz Scraper

A Python script that logs into your **own** [University of the People](https://www.uopeople.edu/) student portal account (D2L Brightspace), pulls every question and answer from your **own past quiz attempts** for a chosen course, de-duplicates repeated questions, and compiles everything into a clean, printable study PDF.

> **Scope of access:** this tool only ever uses **your own login credentials** and only ever visits pages your own account is already authorized to view (your own quiz submission history). It does not access, brute-force, or bypass anything you couldn't already reach by clicking through the portal yourself. See [A note on responsible use](#a-note-on-responsible-use) before running it.

## Features

- 🔐 Logs in through a real, automated browser session (see [Why Selenium?](#why-selenium))
- 📋 Pick a course from a simple numbered menu instead of typing raw codes
- 🔎 Scans every week (1–8) automatically, skipping any week with no attempts without stopping early
- ❓ Extracts multiple-choice and True/False questions, along with all answer options
- ✅ Automatically detects and flags the correct answer for each question
- 🔁 De-duplicates questions that repeat across multiple attempts/weeks
- 📄 Outputs a formatted PDF, saved next to the script, with aligned circle markers for each option
- 📛 Names the PDF automatically based on the course and which weeks actually had data

## Example output

Each question is numbered, with its options listed below it. A filled circle (●) marks the correct answer; empty circles (○) mark the rest.

```
1.   Which model executes code line-by-line?
     ○ Static
     ● Interpreted
     ○ Compiled
     ○ Hybrid
```

The PDF title uses the course name and the weeks that were scraped, e.g.:

```
CS-4402 Comparative Programming Languages
Week 1, 2, 3 Quiz Compilation
```

## Requirements

- Python 3.9+
- [Google Chrome](https://www.google.com/chrome/) installed
- A UoPeople student account with quiz attempts to review

## Installation

```bash
git clone https://github.com/<your-username>/uopeople-quiz-scraper.git
cd uopeople-quiz-scraper
pip install -r requirements.txt
```

Or install the dependencies directly:

```bash
pip install selenium beautifulsoup4 reportlab
```

Selenium 4.6+ automatically downloads a matching `chromedriver` the first time it runs, so no manual driver setup is needed as long as Chrome is installed.

## Usage

```bash
python uopeople_quiz_scraper.py
```

You'll be prompted for:

| Prompt | Description |
|---|---|
| **Username** | Your UoPeople student ID |
| **Password** | Your portal password (hidden as you type) |
| **Course** | Chosen from a numbered menu (see [Adding a course](#adding-a-course) below) |

That's it — no week number to type. A Chrome window opens and drives itself through login and navigation (this is expected); it closes automatically once done.

The script checks weeks 1 through 8 for the chosen course, skipping any week with no attempted quizzes without stopping early (so a gap in the middle, like an empty week 4 followed by a non-empty week 5, is handled correctly). The resulting PDF is saved **in the same folder as the script** and named after only the weeks that actually had data, for example:

```
CS-4402_Week_1_2_3_Quiz_Compilation.pdf
```

### Adding a course

Courses live in a small list near the top of the script:

```python
COURSES = [
    {"label": "CS-4402 Comparative Programming Languages", "short_code": "CS-4402", "course_code": "8457", "week1_qi": 10141},
    {"label": "CS-4403 Software Engineering", "short_code": "CS-4403", "course_code": "8455", "week1_qi": 10185},
]
```

To add another course, add a new entry with:

- `label` — full name shown in the menu and in the PDF title
- `short_code` — short form used in the output filename (e.g. `CS-4402`)
- `course_code` — the `ou` number from the course's URL
- `week1_qi` — the `qi` number from the course's **Week 1** attempted-quizzes URL

To find `course_code` and `week1_qi` for a new course: open that course's Week 1 "attempted quizzes" list page in your browser and read the values out of the address bar:

```
https://learn.uopeople.edu/d2l/lms/quizzing/user/quiz_submissions.d2l?qi=10185&ou=8455
                                                                          ^^^^^     ^^^^
                                                                    week1_qi    course_code
```

Weeks 2–8 are computed automatically from `week1_qi` (it just increments by 1 per week), so you only ever need the Week 1 value.

## Why Selenium?

The D2L login page's "Log In" button is a plain `<button type="button">`, not a real submit button — sign-in is handled entirely by the site's own JavaScript, which attaches an anti-CSRF token that never appears in the static HTML. A plain HTTP POST request skips that handshake entirely, so the server quietly returns a fresh, unauthenticated session even though the response *looks* like a successful login. Driving an actual Chrome browser sidesteps this, since the site's own JS runs exactly as it does when you log in by hand.

## How it works

1. **Login** — drives Chrome through the real login form so the site's JS/XSRF handshake completes normally.
2. **Quiz list** — for each week 1–8, opens `quiz_submissions.d2l?qi=...&ou=...` and collects every "Attempt N" link, skipping weeks with none.
3. **Parsing** — opens each attempt page and extracts, per question:
   - the question text
   - every answer option
   - which option is marked correct (matches the "Correct Response" / "Correct Answer" indicators D2L renders)
4. **De-duplication** — questions with identical text and option sets are only kept once, even if they repeat across multiple attempts or weeks.
5. **PDF generation** — builds a formatted PDF via [ReportLab](https://www.reportlab.com/), with the answer-marker circles aligned under the first letter of each question, saved next to the script.

## Troubleshooting

- **`TimeoutException` on page load** — D2L pages sometimes hang on a slow-to-finish background resource (analytics, webfonts). The script already uses an "eager" page-load strategy and tolerates timeouts, but if you still see this, try increasing `PAGE_LOAD_TIMEOUT` near the top of the script.
- **Login fails immediately** — double-check your username/password. If UoPeople changes their login page structure, the button lookup (`//button[normalize-space(text())='Log In']`) may need updating.
- **"No attempts found" for every week** — double-check the course's `course_code` and `week1_qi` in the `COURSES` list; these values are course-specific and easy to mix up between courses.
- **A question type is skipped** — only single-select MCQ and True/False questions are supported. Matching, fill-in-the-blank, and other question types are intentionally skipped rather than mis-parsed.

## A note on responsible use

This script automates actions you're already permitted to take manually — signing into your own account and reviewing your own quiz history. That said, automated/scripted access may fall outside what your institution's acceptable-use policy technically permits, even when you're only touching your own data. Check your school's policy before running this against a live account, and use it only for your own personal study review.

## License

[MIT](LICENSE) — feel free to fork and adapt for your own courses.
