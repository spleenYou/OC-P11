class TestDisplayScoreboard:
    def test_display_scoreboard_link(self, client, clubs):
        link = '<a href="/scoreboard">Scoreboard</a>'
        response = client.post('/showSummary', data={'email': clubs[0]['email']})
        assert link in response.get_data(as_text=True)

    def test_display_scoreboard(self, client, clubs):
        response = client.get('/scoreboard')
        response_data = response.get_data(as_text=True)
        assert '<table>' in response_data
        for club in clubs:
            assert club['name'] in response_data
            assert club['points'] in response_data

    def test_scoreboard_on_index_page(self, client):
        response = client.get('/')
        assert response.status_code == 200
        expected_answer = '<a href="/scoreboard">Scoreboard</a>'
        assert expected_answer in response.get_data(as_text=True)
