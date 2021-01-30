#Student Name: Clariza Look
#Student ID: 22860721
#Sample input: output = main("sample_accounts.csv",2, True)
#Notes: This program calculates the frequency distribution of a number up to 10 digits only.
#.......During data processing stage, it skips the entire cell in the csv file if it finds characters that are letters, empty cells or non alpha numeric in that certain cell
#.......It checks if file is not found, if no_place is = 0 or greater than 10




#####Function that counts the number of occurrences 
def get_fraction(lst, num):
    r= lst.count(num)
    freq=r/len(lst)
    return freq

#####Function that counts the number of occurrences 
def count_num(lst, num):
    r= lst.count(num)
    return r

#####Rounds the fraction of the frequency to 4 decimal places
def round_fraction(fraction_arr):
    rounded_fraction_arr=[]
    for h in fraction_arr:
        m=round(h,4)
        rounded_fraction_arr.append(m)
    return rounded_fraction_arr

#####Function that gets the count and fraction of the frequence of a number
def get_count_and_fraction(array,r):
    count_arr=[]
    fraction_arr=[]
    for c in range (10):
        if c != 0:
            count_arr.append(count_num(array, c))
            fraction_arr.append(get_fraction(array, c))
        elif c == 0:
            temp=count_num(array, c)
            temp2=get_fraction(array, c)  

            
    #####Stores the count of the frequency
    count_arr.append(temp)
            
    #####Stores the fraction of the frequency
    fraction_arr.append(temp2)
            
    #####If "reguralisation" is False, then show the "Count" output
    if r == False:
        return count_arr
    
    #####If "reguralisation" is True, then show the "fraction" output
    else:
        round_fraction(fraction_arr)
        return round_fraction(fraction_arr)
  
 
#####Function that calculates the frequency of numbers occured in a given list
def calculate_frequency(arr, place, reg):
    
    #####Put arr elements into a temp_arr to preserve elements of arr
    temp_arr=arr
    
    #####Initialize arrays to store first to tenth digits
    get_first_digit_array = []
    get_second_digit_array = []
    get_third_digit_array = []
    get_fourth_digit_array = []
    get_fifth_digit_array = []
    get_sixth_digit_array = []
    get_seventh_digit_array = []
    get_eight_digit_array = []
    get_ninth_digit_array = []
    get_tenth_digit_array = []
    combined_digits_array = []
    
    #####Access each character of each  temp_arr and store in a sub-array by digit position from the left
    for l in range(len(temp_arr)):
        counter=0
        #####Need to convert integer to string to be able to split the number by digit then convert again to int
        for i in str(temp_arr[l]):
            if counter == 0:
                get_first_digit_array.append(int(i))
            if counter == 1:
                get_second_digit_array.append(int(i))
            if counter == 2:
                get_third_digit_array.append(int(i))
            if counter == 3:
                get_fourth_digit_array.append(int(i))
            if counter == 4:
                get_fifth_digit_array.append(int(i))
            if counter == 5:
                get_sixth_digit_array.append(int(i))
            if counter == 6:
                get_seventh_digit_array.append(int(i))
            if counter == 7:
                get_eight_digit_array.append(int(i))
            if counter == 8:
                get_ninth_digit_array.append(int(i))
            if counter == 9:
                get_tenth_digit_array.append(int(i))
            counter += 1

    #print("Regularization:",reg)
    
    ####################################################
    #This is where the calculations happen
    ####################################################
    
    if place == 1:
        #####If array is not empty, then proceed calculating for frequency
        if get_first_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            combined_digits_array.append(output)
            return(combined_digits_array)
        
        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The",place,"no_place list is empty. The number of places in each numerical data to analyse is lower than",place,".")
            print("Please input a lower number of no_places value.")
            raise SystemExit
        
    if place == 2:
        #####If array is not empty, then proceed calculating for frequency
        if get_second_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            output2 = get_count_and_fraction(get_second_digit_array, reg)
            combined_digits_array.append(output)
            combined_digits_array.append(output2)
            return(combined_digits_array)
        
        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The",place,"no_place list is empty. The number of places in each numerical data to analyse is lower than",place,".")
            print("Please input a lower number of no_places value.")
            raise SystemExit
    
    if place == 3:
        #####If array is not empty, then proceed calculating for frequency
        if get_third_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            output2 = get_count_and_fraction(get_second_digit_array, reg)
            output3 = get_count_and_fraction(get_third_digit_array, reg)
            combined_digits_array.append(output)
            combined_digits_array.append(output2)
            combined_digits_array.append(output3)
            return(combined_digits_array)
        
        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The",place,"no_place list is empty. The number of places in each numerical data to analyse is lower than",place,".")
            print("Please input a lower number of no_places value.")
            raise SystemExit
    
    if place == 4:
        #####If array is not empty, then proceed calculating for frequency        
        if get_fourth_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            output2 = get_count_and_fraction(get_second_digit_array, reg)
            output3 = get_count_and_fraction(get_third_digit_array, reg)
            output4 = get_count_and_fraction(get_fourth_digit_array, reg)
            combined_digits_array.append(output)
            combined_digits_array.append(output2)
            combined_digits_array.append(output3)
            combined_digits_array.append(output4)
            return(combined_digits_array)
        
        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The",place,"no_place list is empty. The number of places in each numerical data to analyse is lower than",place,".")
            print("Please input a lower number of no_places value.")
            raise SystemExit
        
    if place == 5:
        #####If array is not empty, then proceed calculating for frequency        
        if get_fifth_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            output2 = get_count_and_fraction(get_second_digit_array, reg)
            output3 = get_count_and_fraction(get_third_digit_array, reg)
            output4 = get_count_and_fraction(get_fourth_digit_array, reg)
            output5 = get_count_and_fraction(get_fifth_digit_array, reg)
            combined_digits_array.append(output)
            combined_digits_array.append(output2)
            combined_digits_array.append(output3)
            combined_digits_array.append(output4)
            combined_digits_array.append(output5)
            return(combined_digits_array)
        
        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The",place,"no_place list is empty. The number of places in each numerical data to analyse is lower than",place,".")
            print("Please input a lower number of no_places value.")
            raise SystemExit
    
    
    if place == 6:
        #####If array is not empty, then proceed calculating for frequency
        if get_sixth_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            output2 = get_count_and_fraction(get_second_digit_array, reg)
            output3 = get_count_and_fraction(get_third_digit_array, reg)
            output4 = get_count_and_fraction(get_fourth_digit_array, reg)
            output5 = get_count_and_fraction(get_fifth_digit_array, reg)
            output6 = get_count_and_fraction(get_sixth_digit_array, reg)
            combined_digits_array.append(output)
            combined_digits_array.append(output2)
            combined_digits_array.append(output3)
            combined_digits_array.append(output4)
            combined_digits_array.append(output5)
            combined_digits_array.append(output6)
            return(combined_digits_array)
        
        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The",place,"no_place list is empty. The number of places in each numerical data to analyse is lower than",place,".")
            print("Please input a lower number of no_places value.")
            raise SystemExit
            
    if place == 7:
        #####If array is not empty, then proceed calculating for frequency
        if get_seventh_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            output2 = get_count_and_fraction(get_second_digit_array, reg)
            output3 = get_count_and_fraction(get_third_digit_array, reg)
            output4 = get_count_and_fraction(get_fourth_digit_array, reg)
            output5 = get_count_and_fraction(get_fifth_digit_array, reg)
            output6 = get_count_and_fraction(get_sixth_digit_array, reg)
            output7 = get_count_and_fraction(get_seventh_digit_array, reg)
            combined_digits_array.append(output)
            combined_digits_array.append(output2)
            combined_digits_array.append(output3)
            combined_digits_array.append(output4)
            combined_digits_array.append(output5)
            combined_digits_array.append(output6)
            combined_digits_array.append(output7)
            return(combined_digits_array)
    
        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The",place,"no_place list is empty. The number of places in each numerical data to analyse is lower than",place,".")
            print("Please input a lower number of no_places value.")
            raise SystemExit
    
    if place == 8:
        #####If array is not empty, then proceed calculating for frequency
        if get_eight_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            output2 = get_count_and_fraction(get_second_digit_array, reg)
            output3 = get_count_and_fraction(get_third_digit_array, reg)
            output4 = get_count_and_fraction(get_fourth_digit_array, reg)
            output5 = get_count_and_fraction(get_fifth_digit_array, reg)
            output6 = get_count_and_fraction(get_sixth_digit_array, reg)
            output7 = get_count_and_fraction(get_seventh_digit_array, reg) 
            output8 = get_count_and_fraction(get_eight_digit_array, reg)
            combined_digits_array.append(output)
            combined_digits_array.append(output2)
            combined_digits_array.append(output3)
            combined_digits_array.append(output4)
            combined_digits_array.append(output5)
            combined_digits_array.append(output6)
            combined_digits_array.append(output7)
            combined_digits_array.append(output8)
            return(combined_digits_array)

        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The",place,"no_place list is empty. The number of places in each numerical data to analyse is lower than",place,".")
            print("Please input a lower number of no_places value.")
            raise SystemExit

    if place == 9:
        #####If array is not empty, then proceed calculating for frequency
        if get_ninth_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            output2 = get_count_and_fraction(get_second_digit_array, reg)
            output3 = get_count_and_fraction(get_third_digit_array, reg)
            output4 = get_count_and_fraction(get_fourth_digit_array, reg)
            output5 = get_count_and_fraction(get_fifth_digit_array, reg)
            output6 = get_count_and_fraction(get_sixth_digit_array, reg)
            output7 = get_count_and_fraction(get_seventh_digit_array, reg) 
            output8 = get_count_and_fraction(get_eight_digit_array, reg)
            output9 = get_count_and_fraction(get_ninth_digit_array, reg)
            combined_digits_array.append(output)
            combined_digits_array.append(output2)
            combined_digits_array.append(output3)
            combined_digits_array.append(output4)
            combined_digits_array.append(output5)
            combined_digits_array.append(output6)
            combined_digits_array.append(output7)
            combined_digits_array.append(output8)
            combined_digits_array.append(output9)
            return(combined_digits_array)

        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The",place,"no_place list is empty. The number of places in each numerical data to analyse is lower than",place,".")
            print("Please input a lower number of no_places value.")
            raise SystemExit

    if place == 10:
        #####If array is not empty, then proceed calculating for frequency
        if get_ninth_digit_array:
            output = get_count_and_fraction(get_first_digit_array, reg)
            output2 = get_count_and_fraction(get_second_digit_array, reg)
            output3 = get_count_and_fraction(get_third_digit_array, reg)
            output4 = get_count_and_fraction(get_fourth_digit_array, reg)
            output5 = get_count_and_fraction(get_fifth_digit_array, reg)
            output6 = get_count_and_fraction(get_sixth_digit_array, reg)
            output7 = get_count_and_fraction(get_seventh_digit_array, reg) 
            output8 = get_count_and_fraction(get_eight_digit_array, reg)
            output9 = get_count_and_fraction(get_ninth_digit_array, reg)
            output10 = get_count_and_fraction(get_tenth_digit_array, reg)
            combined_digits_array.append(output)
            combined_digits_array.append(output2)
            combined_digits_array.append(output3)
            combined_digits_array.append(output4)
            combined_digits_array.append(output5)
            combined_digits_array.append(output6)
            combined_digits_array.append(output7)
            combined_digits_array.append(output8)
            combined_digits_array.append(output9)
            combined_digits_array.append(output10)
            return(combined_digits_array)

        #####Checks if array is empty, else it will exit because there's nothing to calculate
        else:
            print("The ",place," no_place list is empty. That means that your file does not a value of more than ",place," numbers.")
            print("Please input a lower number of no_places value.")
            raise SystemExit
        
#####Function that put all elements of the list in one array list
def combine_number_list_into_one(numlist):

    one_array_list=[]
    
    #####Read all elements in the "numlist" array, the numlist are all numbers
    for r in range (len(numlist)):
        #print("\nnumlist list [",r,"] is: ", numlist[r])
        one_array_list=one_array_list+numlist[r]
        
    #print("\n one_array_list:",one_array_list)
    return one_array_list

#####Function that checks if string is a number int and float
def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

#####Function that converts string numbers into int
def convert_string_to_int(alist):
    blist = []
    ####Store alist value to temp, to preserve alist value
    temp=alist
    
    for item in temp:
        #####Checks if item is a number or letters, if not number, convert to float
        if is_number(item):
            
            item=int(float(item))
            if item > 0:
                #print("ITEM IS GREATER THAN 0: ", item)
                blist.append(item)
            else:
                #print("ITEM IS LESS THAN 0: ", item)
                item=abs(item)
                #print("ABSOLUTE VALUE: ", item)
                blist.append(item)
        else:
            #####Make the entire item empty (or make the cell empty) to be removed empty cells later. 
            item=""
            blist.append(item)

    return blist

#####Function that removes empty strings/cells in the list
def remove_empty_strings_in_list(li):
    updated_list=[]
    
    #####Transfered the value of "li" to "updated_list" to preserve the original value of "li"
    updated_list=li
    
    #####If it sees "", this means that there is an empty element, then remove the element in the list
    while("" in updated_list) :
        updated_list.remove("")
        
    return updated_list

#####Function that process the data from the list
def process_data(data):

    #####Variable where to put if elements of the data are numbers
    numbers_list=[]
    temp_data=[]

    for row in range (len(data)):
        
        #####Checks if every cell in a row is numeric, if one of it is not, replace the entire cell with "" empty cell
        temp_data_f=convert_string_to_int(data[row])

        ####Removes empty strings/cells/arrays in the list
        #datafile=remove_empty_strings_in_list(temp_data_f)

        #####Checks if extracted "datafile" list is not empty, then remove empty elements
        if remove_empty_strings_in_list(temp_data_f):
            
            #####Call convert string to int function, if string is alpha(), then do not include in the tempfile
            tempfile=convert_string_to_int(remove_empty_strings_in_list(temp_data_f))

            #####Check if "tempfile" list is NOT empty, append all the elements of "tempfile" to "number_list" array
            if tempfile:
                numbers_list.append(tempfile)
 
    
    #####Call the function that put all elements of the list in one array list
    processed_data=combine_number_list_into_one(numbers_list)

    return processed_data
        

def read_file(file):
    
    try:
        f = open(file,"r") #opening the csv file
        temp_data_list = []
        for line in f: #reading file line by line and append in a list
            my_list = line.split(",")
            my_list[len(my_list)-1] = my_list[len(my_list)-1].replace("\n", "")
            temp_data_list.append(my_list)
        f.close()
        return temp_data_list
    
    except FileNotFoundError:
        print('File does not exist. Please choose another file.')
        quit()

####main function
def main(filename,no_places,regularise=False): 
    
    j=no_places >= 11
    #####Checks if no_places is not > 10. This program calculates the frequency of a number up to 10 digits only.
    if (j == False):
        
        #####Checks if no_places is not 0.
        if no_places != 0:
            
            #####Reads filename
            read_file(filename)
            all_data=read_file(filename)
            
            #####Checks if filename is empty
            if not all_data:
                print("Your file is empty. Please choose another file.")
                quit()
            else:
                #####If not empty, call function to process data/clean the data
                cleaned_data = process_data(all_data)
                
                ######################################
                #print(cleaned_data)
                r = calculate_frequency(cleaned_data,no_places,regularise)
                
                result = r
                print(result)
                
            return result
        else:
            print("ERROR, your input is zero. Please input no_places from numbers 1-10.")
    elif (j == True):
        print("ERROR, your input is out of range. This program calculates the frequency of a number up to 10 digits only.")
        print("Please input no_places from numbers 1-10.")


if __name__== "__main__":
    output = main("sample_accounts.csv",1)

