# noqa: CPY001
"""Explain catalog inputs in the review form without contributing proposal content."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class InputGuidance:
    """Plain-language help and an example shown only while a field is empty."""

    help: str
    sample: str = ""


# Angle-bracket slots mark project-specific details in samples. Samples are examples,
# never defaults: a value still containing one of its slots has not been filled in.
INPUT_GUIDANCE = {
    "verification_steps": InputGuidance(
        "How a reviewer can confirm this worked. Generated from the catalog; add project-specific checks."
    ),
    "security_reporting_instructions": InputGuidance(
        "How to report a vulnerability privately. Include a link or an email address.",
        "Use GitHub's private vulnerability reporting: <repository URL>/security/advisories/new\n"
        "Or email <security contact address>.",
    ),
    "supported_versions": InputGuidance(
        "Which releases receive security fixes.",
        "| Version | Supported |\n| --- | --- |\n| <latest version> | Yes |\n| <older versions> | No |",
    ),
    "response_timeline": InputGuidance(
        "What reporters can expect, and when. Only promise what the maintainers can keep.",
        "We aim to acknowledge reports within <number> business days and to share an "
        "initial assessment within <number> business days.",
    ),
    "development_setup": InputGuidance(
        "The commands a new contributor runs to get a working copy. Check that they work.",
        "git clone <repository URL>\ncd <project directory>\n<command that installs dependencies>",
    ),
    "test_instructions": InputGuidance(
        "The commands that run the tests, and anything that must pass before a PR.",
        "Run the tests with:\n<test command>",
    ),
    "contribution_process": InputGuidance(
        "The steps from a change to an open PR, plus any branch, commit or style rules.",
        "1. Fork the repository and create a branch from <default branch>.\n"
        "2. Make your change and run the tests.\n"
        "3. Open a pull request and describe the change.\n"
        "4. Update the pull request until a maintainer approves it.",
    ),
    "review_expectations": InputGuidance(
        "How pull requests are reviewed and how long it usually takes. Only promise what "
        "the maintainers can keep.",
        "We aim to review pull requests within <time frame>. Maintainers may ask for "
        "changes before merging, and pull requests must pass <required checks>.",
    ),
    "community_channels": InputGuidance(
        "Where contributors can ask questions and discuss ideas.",
        "Ask questions and discuss ideas in <GitHub Issues, Discussions or chat link>.",
    ),
    "project_name": InputGuidance("The name shown as the README title.", "<project name>"),
    "project_summary": InputGuidance(
        "One or two sentences: what the project does and who it is for.",
        "<project name> helps <audience> to <main benefit>.",
    ),
    "installation_instructions": InputGuidance(
        "The commands that install the project. Check that they work.", "<install command>"
    ),
    "usage_instructions": InputGuidance(
        "The smallest example that shows the project working.",
        "<command or code example>\n\n<expected result>",
    ),
    "support_instructions": InputGuidance(
        "Where people can ask questions or report problems.",
        "Open an issue at <repository URL>/issues.",
    ),
    "approved_license_text": InputGuidance(
        "The complete license text, chosen by a maintainer; see https://choosealicense.com/. "
        "RepoRemedy does not choose a license.",
        "<license name>\n\nCopyright (c) <year> <copyright holder>\n\n<complete license text>",
    ),
    "approved_codeowners": InputGuidance(
        "Who reviews which paths. Each owner must have write access to the repository.",
        "# Default owners\n* @<organization>/<team>\n\n# Documentation\n/docs/ @<username>",
    ),
    "approved_citation_metadata": InputGuidance(
        "How to cite the project, in Citation File Format; see https://citation-file-format.github.io/.",
        "cff-version: 1.2.0\n"
        'message: "If you use this software, please cite it as below."\n'
        'title: "<project name>"\n'
        "authors:\n"
        '  - family-names: "<family name>"\n'
        '    given-names: "<given name>"\n'
        'version: "<version>"\n'
        "date-released: <YYYY-MM-DD>",
    ),
    "approved_code_of_conduct": InputGuidance(
        "The complete policy, including who receives reports; see https://www.contributor-covenant.org/.",
        "<complete code of conduct>\n\nReport concerns to <enforcement contact>.",
    ),
}


def find_unfilled_slots(name: str, value: str) -> list[str]:
    """Return the sample slots that a supplied value still contains."""
    guidance = INPUT_GUIDANCE.get(name)
    if guidance is None:
        return []
    return [slot for slot in re.findall(r"<[^<>\n]+>", guidance.sample) if slot in value]
