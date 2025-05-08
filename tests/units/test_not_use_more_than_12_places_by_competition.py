class TestNoMoreThanTwelvePoints:
    def test_try_booking_with_more_than_12_points(self, client, clubs, competitions):
        nbOfPlacesBooked = 13
        response = client.post(
            '/purchasePlaces',
            data={
                'club': clubs[0]['name'],
                'competition': competitions[0]['name'],
                'places': nbOfPlacesBooked,
            }
        )
        assert response.status_code == 200
        expected_response = "<li>You can&#39;t take more than 12 places</li>"
        assert expected_response in response.get_data(as_text=True)
