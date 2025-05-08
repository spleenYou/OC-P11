import random
from locust import HttpUser, task, between
from server import competitions, clubs


class testWebsite(HttpUser):
    wait_time = between(1, 4)
    host = 'http://localhost:5000'

    def on_start(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task(3)
    def point_display(self):
        self.client.get("/scoreboard")

    @task(2)
    def load_homepage(self):
        self.client.get("/")

    @task(3)
    def book_competition(self):
        choosen_comptetition = competitions[random.randrange(len(competitions))]
        choosen_club = clubs[random.randrange(len(clubs))]
        nbOfPlacesInComp = int(choosen_comptetition['numberOfPlaces'])
        nbOfPlacesBooked = random.randrange(int(choosen_club['points']))
        if nbOfPlacesBooked <= nbOfPlacesInComp:
            self.client.get('/resetData')
            self.client.post("/showSummary", data={"email": choosen_club['email']})
            self.client.get(f"/book/{ choosen_comptetition['name'] }/{ choosen_club['name'] }")
            self.client.post(
                '/purchasePlaces',
                data={
                    'club': choosen_club['name'],
                    'competition': choosen_comptetition['name'],
                    'places': nbOfPlacesBooked,
                }
            )

    @task
    def logout(self):
        self.client.get('/logout')
