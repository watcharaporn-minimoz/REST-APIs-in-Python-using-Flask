import requests

try:
    api_url = "http://127.0.0.1:5000/test"
    todo = {
    "language" : "Python",
    "framework" : "Flask",
    "website" : "Scotch",
    "version_info" : {
        "python" : 3.4,
        "flask" : 0.12
    },
    "examples" : ["query", "form", "json"],
    "boolean_test" : true
}

    response = requests.post(api_url, json=todo)
    print(response.json())
    response.raise_for_status()

except requests.exceptions.HTTPError as error:
    print(error)
    # This code will run if there is a 404 error.