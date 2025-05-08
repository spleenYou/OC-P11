class TestBookingPlacesInPastCompetition:
    def test_booking_in_past_competition(self, client, clubs, competitions):
        response = client.get(f"/book/{ competitions[0]['name'] }/{ clubs[0]['name'] }")
        assert response.status_code == 200
        expected_response = "<li>The competition is already finished</li>"
        assert expected_response in response.get_data(as_text=True)

    def test_show_book_page(self, client, clubs, competitions):
        competitions[0]['date'] = '2026-03-27 10:00:00'
        response = client.get(f"/book/{ competitions[0]['name'] }/{ clubs[0]['name'] }")
        assert response.status_code == 200
        hidden_element_club = f"<input type=\"hidden\" name=\"club\" value=\"{ clubs[0]['name'] }\">"
        assert hidden_element_club in response.get_data(as_text=True)
        hidden_element_comp = f"<input type=\"hidden\" name=\"competition\" value=\"{ competitions[0]['name'] }\">"
        assert hidden_element_comp in response.get_data(as_text=True)
