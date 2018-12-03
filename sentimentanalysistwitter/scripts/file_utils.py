from array_utils import *


def read_sentilex_mapping():
    sentilex_file = open("../../resources/data/SentiLex-flex-PT01.txt", "r")
    content = sentilex_file.read().decode("UTF-8")
    sentilex_mapping = {}
    for line in content.split("\n"):
        components = line.split(".")
        words = components[0].split(",")
        properties = components[1]
        polarity = int(properties.split(";")[3].split("=")[1])
        for word in words:
            sentilex_mapping[word] = polarity
    sentilex_file.close()
    return sentilex_mapping


def read_word_mapping():
    word_mapping_file = open("../../resources/data/word_mapping.txt", "r")
    content = word_mapping_file.read().decode("UTF-8")
    word_mapping = {}
    for line in content.split("\n"):
        components = line.split()
        if len(components) > 2:
            word_mapping[' '.join(components[:len(components) - 1])] = int(components[-1])
        else:
            word_mapping[components[0]] = components[-1]
    word_mapping_file.close()
    return word_mapping


def read_candidate_mapping(file_name):
    candidate_mapping_file = open("../../resources/data/{}".format(file_name), "r")
    candidates = candidate_mapping_file.readlines()
    candidates = map(lambda x: (x.strip().split(",")[0], x.strip().split(",")), candidates)
    candidates = flat_map_values(candidates)
    return set(map(lambda c: (c[1], c[0]), candidates))
