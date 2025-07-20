from flask import Flask, request

from database import insertUser

app = Flask("UserAPI")

@app.route("/helloWorld", methods=["GET"])
def helloWorld():
    return{"hello": "world"}

@app.route("/cadastra/usuario", methods=["POST"])
def registerUser():

    body = request.get_json() 
    
    if ("name" not in body):
        return generateResponse(400, "O parâmetro name é obrigatório")
    
    if ("email" not in body):
        return generateResponse(400, "O parâmetro email é obrigatório")
    
    if ("password" not in body):
        return generateResponse(400, "O parâmetro senha é obrigatório")
    
    user = insertUser(body["name"], body["email"], body["password"])

    return generateResponse(200, "Usuário criado", "user", user)
    

def generateResponse(status, message, contentName = False, content = False):
    response = {}
    response["status"] = status
    response["message"] = message 

    if(contentName and content):
        response[contentName] = content

    return response

app.run()