from services.data_loader.dal import DAL
from services.data_loader.api import MyAPI


def create_app():
    dal = DAL()
    api = MyAPI(dal)
    new_app = api.app

    @new_app.on_event("shutdown")
    def _shutdown():
        dal.close()

    return new_app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)