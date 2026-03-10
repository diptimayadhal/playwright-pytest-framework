import pytest

@pytest.mark.api
@pytest.mark.regression
def test_get_employees(orange_api):

    response = orange_api.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees"
    )

    assert response.status_code == 200

    body = response.json()

    assert "data" in body

    assert isinstance(body["data"], list)