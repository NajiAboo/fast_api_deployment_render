from fastapi import FastAPI
from pydantic import BaseModel

user_data = {
    1: {"name": "naji", "age": 30},
    2: {"name": "john", "age": 25}
}

class User(BaseModel):
    name: str
    age: int


app = FastAPI()


@app.get("/users")
def get_userinfo():
    return user_data

@app.put("/user/{user_id}")
def update_userinfo(user_id: int, input_data: User):

    if user_id in user_data:
        user_data[user_id] = input_data.model_dump()
        return {"message": "successfully updated the user record"}
    else:
        return {"messsage": "failed ot update the user record"}

@app.delete("/user/{user_id}")
def delete_userinfo(user_id: int):
    if user_id in user_data:
        del user_data[user_id]
        return {"message": "successfully deleted the record"}
    else:
        return {"message": "failed to delete the recrod"}