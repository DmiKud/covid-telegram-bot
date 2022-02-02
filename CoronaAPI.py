from datetime import date
import requests


today = date.today()


def qet_number_infected(temp_country):
    temp_date = date.today()
    api_url = f'https://api.covid19api.com/total/country/{temp_country}/status/confirmed?from=2022-01-20T00:00:00Z&to={temp_date}T00:00:00Z'
    res = requests.get(api_url)
    temp_list = list(res.json())
    temp_country = temp_list[-1]['Country']
    cases = temp_list[-1]['Cases']
    return str(temp_country), str(temp_date), str(cases)