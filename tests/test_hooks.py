# -*- coding: utf-8 -*-

import pytest

from requests import hooks


def hook(value):
    return value[1:]


def hook_tests_generator(*tests):
    for name in hooks.HOOKS:
        for test in tests:
            yield (name,) + test


@pytest.mark.parametrize(
    'hook_name, hooks_list, result', hook_tests_generator(
        (hook, 'ata'),
        ([hook, lambda x: None, hook], 'ta'),
    )
)
def test_hooks(hook_name, hooks_list, result):
    assert hooks.dispatch_hook(hook_name, {hook_name: hooks_list}, 'Data') == result


def test_default_hooks():
    assert hooks.default_hooks() == {'response': [], 'request': []}
