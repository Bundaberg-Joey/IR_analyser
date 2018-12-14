########################################################################################################################


def ir_database(path_to_file='ir_frequencies.txt'):
    """Reads text file and then returns as nested array including headers"""
    with open(path_to_file, 'r') as f:
        return [line.split('|') for line in f.readlines()]


########################################################################################################################


def user_frequencies():
    """Takes user frequencies and returns them in a list when user specifies is complete"""
    user_input = []
    while True:
        entry = input('Please enter wavenumber (cm^-1) or \'run\'  : ')
        if entry == 'run':
            break
        elif entry.isnumeric():
            user_input.append(int(entry))

    return user_input


########################################################################################################################


def ir_database_parser(user_input_list, ir_data):
    """Takes user input as input then parses loaded IR database for relevant rows, will then return relevant row"""
    parsed_frequencies = [['User_input']+ir_data[0]]  # add headers to the array that will be returned
    for user_freq in user_input_list:  # for every frequency inputted by the user
        for entry in ir_data[1:]:  # for every row in the loaded IR database (excluding the headers)
            if user_freq in range(int(entry[0]), int(entry[1])):  # builds search range from min and max wavenumbers
                parsed_frequencies.append([user_freq]+entry)  # adds user input wavenumber to start or appended list

    return parsed_frequencies  # returns nested array which is a trimmed down version of the original database


########################################################################################################################


def results_writer(filtered_ir):
    """Takes nested list as input and writes the result to a txt file with name specified by the user"""
    while True:
        user_file_name = input('Please enter a file name to save results to: ')
        if user_file_name.isalpha():
            print('Filename saved to :  '+user_file_name+'.txt')
            break
        else:
            print('Please enter valid filename: ')

    with open(user_file_name+'.txt', 'w') as f:  # writes nested array as a pipe delimited file
        for line in filtered_ir:
            for entry in line:
                f.write(str(entry)+'|')

    print('file written')

########################################################################################################################


def main():
    """Takes database file and user input to parse the database file, return a trimmed file and then save to new txt"""
    returned_analysis = ir_database_parser(user_frequencies(), ir_database())  # create filtered list of wavenumbers
    results_writer(returned_analysis)  # write the filtered list of wavenumbers to a file


########################################################################################################################

if __name__ == '__main__':
    main()
