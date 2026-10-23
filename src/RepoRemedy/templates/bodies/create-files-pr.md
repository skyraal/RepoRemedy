## What this PR does

${change_summary}

${response}

## Why this PR was opened

This PR was proposed because an automated check reported a gap: `${check}`
(source: ${origin}, repository: ${repository}).

- **OSSF** is the [OpenSSF Scorecard](https://github.com/ossf/scorecard), a public tool that
  scores a repository's security and project-health practices from 0 to 10.
- **RA** is RepoAuditor, a tool that checks a repository for expected files and settings.

A low score or a "gap" is a prompt to review, not a verdict on the project. The raw
result is below for reference.

<details>
<summary>Raw audit result</summary>

${evidence}

</details>

## How to review

1. Read the added file(s) in the "Files changed" tab.
2. Edit anything that doesn't match your project; this PR is only a starting point.
3. Merge when you're happy, or close the PR if you don't want it.

## Validation plan

${verification_steps}

This is a draft proposal, and these checks still need to be performed. The PR only
creates new files; it never overwrites existing content.
