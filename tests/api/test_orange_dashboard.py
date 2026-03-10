def test_dashboard_summary(orange_api):

    response = orange_api.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/action-summary"
    )

    assert response.status_code == 200