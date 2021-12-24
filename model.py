import json
from typing import Dict
import numpy as np
from mlserver import MLModel, types
from mlserver.utils import get_model_uri


class ExampleModel(MLModel):
    async def load(self) -> bool:

        model_uri = await get_model_uri(self._settings)

        # load model
        with open(model_uri, "r") as f:
            self.model = json.load(f)

        # mark model as ready
        self.ready = True

        # print debug message
        print(f"--------- Model Readiness: {self.ready} ---------")

        return self.ready

    async def predict(self, payload: types.InferenceRequest) -> types.InferenceResponse:
        inputs = self._extract_inputs(payload)["data_points"]
        predictions = [self.model["a"] * i + self.model["b"] for i in inputs]

        return types.InferenceResponse(
            id=payload.id,
            model_name=self.name,
            model_version=self.version,
            outputs=[
                types.ResponseOutput(
                    name="points",
                    datatype="int",
                    data=predictions,
                    shape=[len(predictions)],
                )
            ],
        )

    def _extract_inputs(self, payload: types.InferenceRequest) -> Dict[str, np.ndarray]:
        inputs = {}
        for inp in payload.inputs:
            inputs[inp.name] = np.array(inp.data)

        return inputs
