"""
Journal module for saving and restoring entries

"""
import os


def load(name):
    """
    This method creates and loads a new journal
    :param name: The base name of the journal to load
    :return: the new journal data
    """
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as f:
            for line in f.readlines():
                data.append(line.rstrip())
    return data


def save(name, journal_data):
    """
    Saves an existing journal
    :param name: filename of the journal to save
    :param journal_data: data to save
    :return: None
    """
    filename = get_full_pathname(name)
    print('.... saving to{}'.format(filename))
    with open(filename, 'w') as f:
        for entry in journal_data:
            f.write(entry + '\n')


def get_full_pathname(name):
    """
    Returns the full path of where the journal is saved.
    :param name: name of journal
    :return: full path of journal filename
    """
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    """
    Adds an entry to our journal
    :param text: entry to be added
    :param journal_data: journal
    :return: None
    """
    journal_data.append(text)
