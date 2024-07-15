import requests

def execute_notebook(request):
    notebook_url = "URL_DE_TU_NOTEBOOK"  # Reemplaza esto con la URL de tu notebook de Colab
    headers = {
        "Authorization": "Bearer " + "TU_TOKEN_DE_AUTORIZACION"
    }

    data = {
        "parameter": {
            "timeoutMinutes": 30,
            "parameters": [
                {
                    "name": "param1",
                    "value": "value1"
                }
            ]
        }
    }

    response = requests.post(notebook_url, headers=headers, json=data)

    if response.status_code == 200:
        return "Notebook ejecutado con éxito"
    else:
        return f"Error al ejecutar el notebook: {response.content}"
