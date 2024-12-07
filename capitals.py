# Using dictionary comprehension, write a program that receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line
# (again separated by comma and space ", "). Print each country with its capital on a separate line in the following
# format: "{country} -> {capital}".
# Hints
# •	You could use the zip() method.


countries = input().split(", ")
capitals = input().split(", ")

country_capital = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in country_capital.items():
    print(f"{country} -> {capital}")
  