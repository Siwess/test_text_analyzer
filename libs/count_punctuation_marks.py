from libs import file_name


def count_punctuation_marks():
    ##
    # Count punctuation marks in file
    ##

    file = open(file_name.name_file)
    data = file.read()
    numbers_of_characters = len(data)
    # TODO: Implement: Count punctuation marks
