class TestLoginUnknownMail:
    def test_login(self, client, clubs):
        response = client.post('/showSummary', data={'email': clubs[0]['email']})
        assert response.status_code == 200
        expected_response = "john@simplylift.co"
        response_data = response.get_data(as_text=True)
        assert expected_response in response_data

    def test_login_with_unknown_email(self, client):
        response = client.post('/showSummary', data={'email': 'email@unknown.com'})
        assert response.status_code == 200
        expected_response = "<li>Email not found</li>"
        assert expected_response in response.get_data(as_text=True)
