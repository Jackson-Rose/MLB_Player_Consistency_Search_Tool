import csv

stat_list = []
list_with_years = []
fixed_row = 'blank'

def print_csv_file(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for c in csv_reader:
                fixed_row = (','.join(c))
                stat_list.append(fixed_row)

        search_text1 = 'AL'
        for string in stat_list:
            if search_text1 in string:
                list_with_years.append(string)
            else:
                continue

        data_table = []

#the following code finds the year, PA, and OPS+, and appends those values to a new list called line_data
        for line in list_with_years:
            line_data = []
            comma_counter = 0
            line_data.append(line[0:4])
            plate_appearances = ""
            ops_adjusted = ""
            type(plate_appearances)
            for character in line:
                if (character == ','):
                    comma_counter += 1
                if (comma_counter == 5 and character != ','):
                    plate_appearances = plate_appearances + character
                if (comma_counter == 6 and character == ','):
                    line_data.append(plate_appearances)
                elif (comma_counter == 21 and character != ','):
                    ops_adjusted = ops_adjusted + character
                elif (comma_counter == 22 and character == ','):
                    line_data.append(ops_adjusted)

#the following code looks through the data in line_data and filters out any instances of a year with fewer than 502 PAs
#it then adds the values to a list called data_table_2
            data_table.append(line_data)
        data_table_2 = []
        for lineNum in data_table:
            if(int(lineNum[1]) > 502):
                data_table_2.append(lineNum)

#this removes the PA integer from the array because we don't need it anymore
        new_array = []
        for a in data_table_2:
            a.pop(1)
            new_array.append(a)

#this finds and returns the highest OPS+ value from our data
        highest_OPS_value = 0
        int_new_array = 0
        indexing_variable = 1
        length_of_data = len(data_table_2)
        for data in new_array:
            int_new_array = int(new_array[indexing_variable][1])
            indexing_variable = indexing_variable + 1
            if int_new_array > highest_OPS_value:
                highest_OPS_value = int_new_array
            if indexing_variable >= length_of_data:
                break

        OPS_list = []
        for index, item in enumerate(new_array):
            OPS_list.append(item[1])

    #this will return a list of each OPS+ subtracted by the previous one, in absolute value
        OPS_delta = []
        OPS_delta_list = []
        current_position = 0
        current_position_minus_one = 0
        index_counter = 0
        for data in OPS_list:
            if index_counter == 0:
                index_counter = index_counter + 1
                continue
            else:
                current_position = OPS_list[index_counter] #sets the current position to be equal to the value we're on. To start, it's the second value
                current_position = int(current_position)
                one_back = OPS_list[index_counter - 1] #establishes the prior value in the list
                one_back = int(one_back)
                OPS_delta = current_position - one_back #finds the delta
                OPS_delta = int(OPS_delta)
                OPS_delta = abs(OPS_delta) #converts the numbers to absolute value form
                OPS_delta_list.append(OPS_delta) #appends the value to our list
                index_counter = index_counter + 1 #increments the index counter

    #this creates a new list with just the years as integers
        year_list = []
        int_year = 0
        for a in new_array:
            int_year = int(a[0])
            year_list.append(int_year)

        #this prints the year that had the smallest delta from the previous year, and that delta
        year_list_sub_one = year_list[1:]
        mindelta = min(OPS_delta_list)
        year_position = OPS_delta_list.index(mindelta)
        corresponding_year = year_list_sub_one[year_position]
        print(corresponding_year,',',mindelta)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = input('Enter file name: ')
#if __name__ == "__main__":
file_path = file_name
if file_name != 'Exit':
    print_csv_file(file_path)
else:
    print('Exiting the program.')
