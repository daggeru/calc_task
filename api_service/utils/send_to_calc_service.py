import requests


def send_data_to_parse(calc_url, data):
    response = requests.post(calc_url, data=data)
    return response
