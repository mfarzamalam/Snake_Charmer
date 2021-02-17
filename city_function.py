def get_formatted_city_country(city,country,population=''):
    if population:
        detail = city + ', ' + country + ' - Population ' +population
    else:
        detail = city + ', ' + country

    return detail.title() 