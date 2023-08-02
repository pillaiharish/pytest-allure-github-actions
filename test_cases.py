import pytest
import allure

@allure.epic("EPIC_1")
@allure.parent_suite('Parent Suite 1')
@pytest.mark.sanity
@pytest.mark.master
@pytest.mark.basic_sanity
def test_function_1():
    """ Test function 1 """
    allure.dynamic.suite("SUITE_1")
    assert 5==5


@allure.epic("EPIC_1")
@allure.parent_suite('Parent Suite 1')
@pytest.mark.sanity
@pytest.mark.master
@pytest.mark.basic_sanity
def test_function_2():
    """ Test function two 2 """
    allure.dynamic.suite("SUITE_1")
    assert 1+1==2


@allure.epic("EPIC_1")
@allure.parent_suite('Parent Suite 1')
@pytest.mark.sanity
@pytest.mark.master
@pytest.mark.basic_sanity
def test_function_3():
    """ Test function three 3 """
    allure.dynamic.suite("SUITE_2")
    assert 3==4
