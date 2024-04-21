import json
from typing import List
import google.generativeai as genai


class JsonWrapper:
    def __init__(self, api_key: str, examples: List[dict]) -> None:
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            "gemini-pro", generation_config=genai.GenerationConfig(temperature=0.1)
        )
        instruction_message = """
Please output VALID JSON. Output MUST be able to be used as a json file.
Follow the exact format of the example json objects. 
Follow the properties of the example objects EXACTLY.
Do not include the examples in the output.
The following are example json objects.
        """
        examples_message = "["
        for j in examples:
            examples_message = examples_message + json.dumps(j) + ","
        examples_message = (
            examples_message[:-1] + "]"
        )  # to remove the last comma and add closing square bracket
        self.message = instruction_message + examples_message

    def generate_content(self, prompt: str) -> List[dict]:
        self.message = self.message + prompt
        response = self.model.generate_content(self.message).text
        response = self._sanitize(response)
        response = eval(response)
        return response

    def _sanitize(self, response: str) -> str:
        if response[0] == "`":
            return response[7:-3]
        return response
