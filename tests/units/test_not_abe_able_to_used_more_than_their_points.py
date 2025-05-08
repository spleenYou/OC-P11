class TestNotUseMoreThanTheirPoints:
    def test_booking_with_less_than_their_points(self, client, clubs, competitions):
        initialNbOfPlacesInComp = int(competitions[0]['numberOfPlaces'])
        initialNbOfPlacesInClub = int(clubs[0]['points'])
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
        assert f"Number of Places: { initialNbOfPlacesInComp - nbOfPlacesBooked }" in response.get_data(as_text=True)
        assert f"Points available: { initialNbOfPlacesInClub - nbOfPlacesBooked }" in response.get_data(as_text=True)

    def test_booking_with_equal_than_their_points(self, client, clubs, competitions):
        initialNbOfPlacesInComp = int(competitions[0]['numberOfPlaces'])
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
        assert f"Number of Places: { initialNbOfPlacesInComp - nbOfPlacesBooked }" in response.get_data(as_text=True)
        assert "Points available: 0" in response.get_data(as_text=True)

    def test_booking_with_more_than_their_points(self, client, clubs, competitions):
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
        expected_response = "<li>You don&#39;t have enough point</li>"
        assert expected_response in response.get_data(as_text=True)
