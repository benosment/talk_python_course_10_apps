import bs4
import requests
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'loc, cond, temp, scale')


def main():
    print_header()
    zipcode = input('What zipcode do you want the weather for? ')
    html = get_html_from_web(zipcode)
    report = get_weather_from_html(html)
    # display the forecast
    print('The weather in {} is {} and {} {}'.format(
        report.loc,
        report.cond,
        report.temp,
        report.scale,
    ))


def print_header():
    print('---------------------------------')
    print('      WEATHER APP')
    print('---------------------------------')
    print()


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    return WeatherReport(loc=loc, cond=condition, temp=temp, scale=scale)


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()


if __name__ == '__main__':
    main()
