from fastapi import FastAPI
import base_model_objects as bm_object

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


        @self.app.post("/insert")
        def add_doc(doc : bm_object.Soldier):
            try:
                self.dal.write(doc.__dict__)
                return {"message": f"inserted soldier {doc.first_name}, {doc.last_name}, with id {doc.soldier_ID} into the collection {self.dal.col}", "status" : "succeeded"}
            except Exception as e:
                return {"message": e, "status" : "error"}


        @self.app.put("/update")
        def update_doc(update_object : bm_object.UpdateSoldierField):
            try:
                self.dal.update(update_object.__dict__)
                return {"message": f"updated field {update_object.field} in soldier id - {update_object.soldier_ID} successfully", "status" : "succeeded"}
            except Exception as e:
                return {"message": e, "status": "error"}
































