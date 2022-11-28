from locust import HttpUser, between, task
import getpass
from random import randrange
from fastapi.security import HTTPBasic, HTTPBasicCredentials

randnr = randrange(99999999)
class PerformanceTests(HttpUser):
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("/")

    @task
    def test_prime(self):
        self.client.get("/prime/"+ str(randnr))

    @task
    def test_picture(self):
        self.client.get("/picture/invert/"+ str("image.jpg"))

    @task
    def test_login(self):
        self.client.get("/login", auth=('username', 'password '))