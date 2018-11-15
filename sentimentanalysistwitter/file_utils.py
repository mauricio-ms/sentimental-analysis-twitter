def read_word_mapping():
    word_mapping_file = open("data/word_mapping.txt", "r")
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


def read_candidate_mapping():
    candidate_mapping_file = open("data/candidate_mapping.txt", "r")
    return candidate_mapping_file.readlines()