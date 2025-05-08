class TestNotUseMoreThanTheirPoints:
    def test_booking_with_less_than_their_points_ok(self, client, clubs, competitions):
        nbOfPlacesInComp = int(competitions[0]['numberOfPlaces'])
        nbOfPlacesBooked = 2
        response = client.post(
            '/purchasePlaces',
            data={
                'club': clubs[0]['name'],
                'competition': competitions[0]['name'],
                'places': nbOfPlacesBooked,
            }
        )
        assert response.status_code == 200
        assert 'Great-booking complete' in response.get_data(as_text=True)
        assert f"Number of Places: { nbOfPlacesInComp - nbOfPlacesBooked }" in response.get_data(as_text=True)

    def test_booking_with_equal_than_their_points_ok(self, client, clubs, competitions):
        nbOfPlacesInComp = int(competitions[0]['numberOfPlaces'])
        nbOfPlacesBooked = int(clubs[1]['points'])
        response = client.post(
            '/purchasePlaces',
            data={
                'club': clubs[1]['name'],
                'competition': competitions[0]['name'],
                'places': nbOfPlacesBooked,
            }
        )
        assert response.status_code == 200
        assert 'Great-booking complete' in response.get_data(as_text=True)
        assert f"Number of Places: { nbOfPlacesInComp - nbOfPlacesBooked }" in response.get_data(as_text=True)

    def test_booking_with_more_than_their_points_failed(self, client, clubs, competitions):
        nbOfPlacesBooked = int(clubs[1]['points']) + 1
        response = client.post(
            '/purchasePlaces',
            data={
                'club': clubs[1]['name'],
                'competition': competitions[0]['name'],
                'places': nbOfPlacesBooked,
            }
        )
        assert response.status_code == 200
        expected_response = "<li>You don&#39;t have enough points</li>"
        assert expected_response in response.get_data(as_text=True)
