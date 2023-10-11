from city_functions import city_country_population_format as ccpf


def test_city_country():
    """Does 'Santiago, Chile' work?"""
    formatted_name = ccpf('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'

def test_city_country_population():
    """Does 'Santiago, Chile - population 5000000' work?"""
    formatted_name = ccpf('santiago', 'chile', 5000000)
    assert formatted_name == 'Santiago, Chile - population 5000000'