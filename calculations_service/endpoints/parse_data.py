def parse_data(data):
    # todo validate if there's any data, correct format of data etc.
    data_sum = len(data)
    avg = sum(item['v'] for item in data)/data_sum
    return {
        'avg': avg,
        'sum': data_sum
    }, 200
