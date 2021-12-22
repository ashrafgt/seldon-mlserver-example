## MLServer Issue: Multiple Model Loads

### Reproduction Steps:

0. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

1. Start the server:
    ```bash
    mlserver start .
    ```

    The logs should look like this:
    ```bash
    --------- Model Readiness: True ---------
    INFO:     Started server process [12556]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
    ```

2. Start the server in a seperate terminal:
    ```bash
    python test.py
    ```
    
    The test script logs should indicate inference success:
    ```python
    {'model_name': 'mlserver-example', 'model_version': None, 'id': '9ca77367-83a1-43e9-884d-3427bad82bad', 'parameters': None, 'outputs': [{'name': 'image_tags', 'shape': [4], 'datatype': 'int', 'parameters': None, 'data': [14.4, 9.6, 28.799999999999997, -2.4]}]}
    ```

    But the server logs should indicate that the `load()` method is being called multiple times unnecessarily:
    ```bash
    --------- Model Readiness: True ---------
    INFO:     127.0.0.1:61218 - "POST /v2/models/mlserver-example/infer HTTP/1.1" 200 OK
    --------- Model Readiness: True ---------
    --------- Model Readiness: True ---------
    --------- Model Readiness: True ---------
    ```
