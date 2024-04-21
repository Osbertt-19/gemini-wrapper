from typing import List
import os
from dotenv import load_dotenv
from geminiwrapper import ObjectWrapper


class Country:
    def __init__(self, name, capital, population, neighbouring_countries) -> None:
        self.name = name
        self.capital = capital
        self.population = population
        self.neighbouring_countries = neighbouring_countries


if __name__ == "__main__":
    country1 = Country("England", "London", "56.3 million", ["Scotland", "Wales"])
    country2 = Country(
        "Thailand",
        "Bangkok",
        "70.4 million",
        ["Myanmar (Burma)", "Laos", "Cambodia", "Malaysia"],
    )
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    object_model = ObjectWrapper(api_key, __name__, [country1, country2])
    prompt = "Write about Myanmar, Singapore, United States and Germany"
    response: List[Country] = object_model.generate_content(prompt)

    for country in response:
        print(f"The name of the country: {country.name}")
        print(f"The capital of the country: {country.capital}")
        print(f"The population of the country: {country.population}")
        print(f"The neighbouring countries: {country.neighbouring_countries}")
