from fastapi import FastAPI

class MyAPI:

    def __init__(self, dal):
        self.dal = dal
        self.app = FastAPI()
        self._routes_listener()


    def _routes_listener(self) -> None:





















