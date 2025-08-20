from fastapi import FastAPI

class MyAPI:

    def __init__(self, dal):
        self.dal = dal
        self.app = FastAPI()
        self._routes_listener()


    def _routes_listener(self) -> None:

        @self.app.get("/health")
        def health():
            return {"status": "ok"}


        @self.app.get("/get_all")
        def get_all():
            return {"all_docs" : self.dal.read_all()}

























