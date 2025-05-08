from flask import url_for


class TestDisplayScoreboard:
    def test_display_scoreboard_link_ok(self, client, clubs):
        link = "<a href=\"" + url_for('scoreboard') + "\">Scoreboard</a>"
        response = client.post('/showSummary', data={'email': clubs[0]['email']})
        assert link in response.get_data(as_text=True)

    def test_display_scoreboard_ok(self, client, clubs):
        response = client.get('/scoreboard')
        response_data = response.get_data(as_text=True)
        assert '<table>' in response_data
        for club in clubs:
            assert club['name'] in response_data
            assert club['points'] in response_data
