from configparser import ConfigParser, ParsingError
import os


def config(filename='../config/config.ini', section='camera'):
    """
    Reads configuration settings from a specified INI file.

    :param filename: Path to the INI configuration file.
    :param section: The section of the configuration file to read.
    :return: A dictionary containing configuration parameters.
    :raises: Exception if the file does not exist, is not accessible, or the section is not found.
    """
    # Check if the file exists
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The configuration file '{filename}' does not exist.")

    parser = ConfigParser()

    try:
        parser.read(filename)
    except ParsingError:
        raise ParsingError(f"Error parsing the configuration file '{filename}'.")

    # Check if the specified section exists
    if not parser.has_section(section):
        raise Exception(f"Section '{section}' not found in the '{filename}' file.")

    # Read parameters under the specified section
    camera = {}
    params = parser.items(section)
    for param in params:
        camera[param[0]] = param[1]

    return camera
