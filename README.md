## GeminiWrapper

GeminiWrapper is a library for generating consistent Gemini API outputs and wrapping them with json and python objects. It takes python dictionaries(as json files) or python objects as few-shot examples to output valid json or python objects.

### Getting Started

**Installation**

```console
pip install geminiwrapper
```

**Basic Usage**

1. Import:

```python
import geminiwrapper
```

2. Obtain Gemini AI API key:
   [Get Gemini AI API key](https://ai.google.dev/tutorials/setup)

3. Create example objects:

- For json output, create a few python dictionaries. For example,

```python
json1 = {
    "name": "England",
    "capital": "London",
    "population": "56.3 million",
    "neighbouring_countries": ["Scotland", "Wales"],
}
json2 = {
    "name": "Thailand",
    "capital": "Bangkok",
    "population": "70.4 million",
    "neighbouring_countries": ["Myanmar (Burma)", "Laos", "Cambodia", "Malaysia"],
}
```

- For python object output, create a class and a few objects. For example,

```python
class Country:
    def __init__(self, name, capital, population, neighbouring_countries) -> None:
        self.name = name
        self.capital = capital
        self.population = population
        self.neighbouring_countries = neighbouring_countries
country1 = Country("England", "London", "56.3 million", ["Scotland", "Wales"])
country2 = Country(
    "Thailand",
    "Bangkok",
    "70.4 million",
    ["Myanmar (Burma)", "Laos", "Cambodia", "Malaysia"],
)
```

4. Instantiate the wrapper:

- For json output,

```python
json_model = JsonWrapper(api_key, [json1, json2])
```

api_key is the Gemini API key obtained from [this link](https://ai.google.dev/tutorials/setup)

- For python object output,

```python
object_model = ObjectWrapper(api_key, __name__, [country1, country2])
```

api_key is the Gemini API key obtained from [this link](https://ai.google.dev/tutorials/setup)
**name** is to pass the name of the module.

5. Generate Content:

- For json output,

```python
prompt = "Write about Myanmar, Singapore, United States and Germany"
response = json_model.generate_content(prompt)
```

response is a list of dictionaries that can be processed as follow.

```python
for country in response:
    print(f"The name of the country: {country['name']}")
    print(f"The capital of the country: {country['capital']}")
    print(f"The population of the country: {country['population']}")
    print(f"The neighbouring countries: {country['neighbouring_countries']}")
```

- For python object output,

```python
prompt = "Write about Myanmar, Singapore, United States and Germany"
response: List[Country] = object_model.generate_content(prompt)
```

response is a list of Country objects that can be processed as follow.

```python
for country in response:
    print(f"The name of the country: {country.name}")
    print(f"The capital of the country: {country.capital}")
    print(f"The population of the country: {country.population}")
    print(f"The neighbouring countries: {country.neighbouring_countries}")
```
