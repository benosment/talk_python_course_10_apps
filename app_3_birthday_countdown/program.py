import datetime


def print_header():
    print('---------------------------------')
    print('      BIRTHDAY APP')
    print('---------------------------------')
    print()


def get_birthday_from_user():
    year = int(input('What year were you born [YYYY]? '))
    month = int(input('What month were you born [MM]? '))
    day = int(input('What day were you born [DD]? '))
    print('It looks like you were born on {}/{}/{}'.format(month, day, year))
    return datetime.date(year, month, day)


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    td = this_year - target_date
    return td.days


def print_birthday_information(number_of_days):
    if number_of_days < 0:
        print('Looks like your birthday was {} days ago'.format(abs(number_of_days)))
    elif number_of_days > 0:
        print('Looks like your birthday is in {} days.'.format(number_of_days))
        print('Hope you are looking forward to it!')
    else:
        print('Today is your birthday!')


if __name__ == '__main__':
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)