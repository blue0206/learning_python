def city_country_population_format(city, country, population=''):
    """Takes in city and country name and 
    outputs in 'city, country - population' format."""
    if population:
        formatted_name = f"{city}, {country}"
        formatted_name = formatted_name.title() + f" - population {population}"
        return formatted_name
    else:
        formatted_name = f"{city}, {country}"
        return formatted_name.title()