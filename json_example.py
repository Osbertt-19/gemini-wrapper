import os
from dotenv import load_dotenv
from geminiwrapper import JsonWrapper

if __name__ == "__main__":
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
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    json_model = JsonWrapper(api_key, [json1, json2])

    prompt = "Write about Myanmar, Singapore, United States and Germany"
    response = json_model.generate_content(prompt)
    for country in response:
        print(f"The name of the country: {country['name']}")
        print(f"The capital of the country: {country['capital']}")
        print(f"The population of the country: {country['population']}")
        print(f"The neighbouring countries: {country['neighbouring_countries']}")
