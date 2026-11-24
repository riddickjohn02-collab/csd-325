
# Name: Robert Cuevas
# Date: November 24, 2026
# Assignment: CSD-325 Module 7 - Test Cases
# Purpose: Format city and country names into a single string.


# Define a function that accepts a city and country.

# Format a city and country with optional population and language.
def city_country(city, country, population=None, language=None):
    result = f"{city}, {country}"

    if population is not None:
        result += f" - population {population}"

    if language is not None:
        result += f", {language}"

    return result



# Call the function three times using different parameters.
if __name__ == "__main__":

    # City and country only
    print(city_country("Santiago", "Chile"))

    # City, country, and population
    print(city_country("Orlando", "United States", 320742))

    # City, country, population, and language
    print(city_country("Tokyo", "Japan", 13960000, "Japanese"))

