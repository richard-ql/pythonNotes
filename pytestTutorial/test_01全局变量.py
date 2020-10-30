import pytest

@pytest.fixture(scope = 'module')
def global_data():
    return {'presentVal': 0}

@pytest.mark.parametrize('iteration', range(1, 6))
def test_global_scope(global_data, iteration):
    assert global_data['presentVal'] == iteration - 1
    global_data['presentVal'] = iteration
    print(global_data['presentVal'])
    assert global_data['presentVal'] == iteration
