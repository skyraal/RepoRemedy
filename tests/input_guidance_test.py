"""Keep form guidance aligned with the catalog and separate from proposal content."""

import pytest

from RepoRemedy.catalog import load_catalog
from RepoRemedy.context.github import ContextError
from RepoRemedy.context.resolve import PROTECTED_INPUTS, resolve_template_inputs
from RepoRemedy.input_guidance import INPUT_GUIDANCE, find_unfilled_slots
from remedy_fixtures import make_report
from repository_context_test import FakeGitHub


def declared_inputs():
    remedies = load_catalog().remedies.values()
    routes = [route for remedy in remedies for route in (remedy.issue, remedy.pr) if route]
    return {key for route in routes for key in route.required_inputs}


def test_guidance_names_declared_inputs():
    assert INPUT_GUIDANCE.keys() <= declared_inputs() - PROTECTED_INPUTS


def test_every_pr_input_has_guidance():
    routes = [remedy.pr for remedy in load_catalog().remedies.values() if remedy.pr]
    inputs = {key for route in routes for key in route.required_inputs}
    assert inputs - PROTECTED_INPUTS <= INPUT_GUIDANCE.keys()
    assert all(guidance.help.strip() for guidance in INPUT_GUIDANCE.values())


def test_finds_only_the_inputs_own_slots():
    assert find_unfilled_slots("project_name", "<project name>") == ["<project name>"]
    assert find_unfilled_slots("project_name", "Demo <beta>") == []
    assert find_unfilled_slots("undocumented", "<project name>") == []


def test_supplied_sample_is_rejected():
    supplied = {"security-policy": {"supported_versions": "<latest version> only"}}
    with pytest.raises(ContextError, match="sample placeholders"):
        resolve_template_inputs(make_report("SecurityPolicy"), FakeGitHub().snapshot(), supplied)
