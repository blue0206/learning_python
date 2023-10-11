from city_functions import city_country_population_format as ccpf

print("This program outputs city, country, and population in a proper format.")
print("Enter blank to skip the population detail.")
print("Enter 'q' to quit.")

while True:
    city = input("Enter City: ")
    if city.lower() == 'q':
        break

    country = input("Enter Country: ")
    if country.lower() == 'q':
        break

    population = input("Enter Population: ")
    if population.lower() == 'q':
        break

    formatted_name = ccpf(city, country, population)
    print(f"\n{formatted_name}\n")
