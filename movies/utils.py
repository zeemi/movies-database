import re


def convert_to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def normalize_keys(dictionary):
    return {convert_to_snake_case(k): v for k, v in dictionary.items()}