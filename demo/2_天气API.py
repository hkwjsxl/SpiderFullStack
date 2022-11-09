import requests


if __name__ == '__main__':
    url = 'https://geoapi.qweather.com/v2/city/lookup?key=456822efe8b245c4b621562d72e910e8&location=邯郸市'
    res = requests.get(url)
    print(res.text)

