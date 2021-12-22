import requests


inputs = [5, 3, 11, -2]

inference_request = {
    "inputs": [
        {
            "name": "data_points",
            "shape": [len(inputs)],
            "datatype": "int",
            "data": inputs,
        }
    ]
}

endpoint = "http://localhost:8080/v2/models/mlserver-example/infer"
response = requests.post(endpoint, json=inference_request)

print(response.json())
