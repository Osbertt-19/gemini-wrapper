import importlib
import inspect
from typing import List
import google.generativeai as genai


class ObjectWrapper:
    def __init__(self, api_key: str, module: str, examples: List[object]):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            "gemini-pro", generation_config=genai.GenerationConfig(temperature=0.1)
        )
        self.module = importlib.import_module(module)
        instruction_message = """
Please output Valid Python List of objects.
Output MUST follow the format of the example.
Do not include the examples in the output.
The follow are example objects.
        """
        examples_message = self._examples_message(examples)
        self.message = instruction_message + examples_message + "\n"

    def generate_content(self, prompt: str):
        self.message = self.message + prompt
        response = self.model.generate_content(self.message).text
        response = self._sanitize(response)
        response = eval(response)
        return response

    def _sanitize(self, response: str) -> str:
        if response[0] == "`":
            return response[9:-3]
        return response

    def _examples_message(self, examples: List[object]) -> str:
        message = "["
        cls = type(examples[0]).__name__
        attributes = []
        for i in inspect.getmembers(examples[0]):
            # to remove private and protected functions
            if not i[0].startswith("_"):
                # to remove other methods that does not start with a underscore
                if not inspect.ismethod(i[1]):
                    attributes.append(i[0])
        for example in examples:
            e = f"self.module.{cls}"
            e = e + "("
            for attribute in attributes:
                value = getattr(example, attribute)
                if type(value) == str:
                    value = "'" + value + "'"
                e = e + f"{attribute}={value}" + ","
            e = (
                e[:-1] + ")" + ","
            )  # to remove the last comma and add closing round bracket and a comma
            message = message + e
        message = (
            message[:-1] + "]"
        )  # to remove the last comma and add closing square bracket
        return message
