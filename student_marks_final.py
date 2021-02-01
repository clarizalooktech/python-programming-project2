'''
Name: Clariza Look

Task:
- Create a computer program which can read the data from a csv (comma separated values) file 
- and return different statistical aspects of the marks of the students and their ranking. 
- Your task is to write a program which
    • List containing the minimum marks for each subject followed by minimum total marks obtained by a student. 
    • List similar to above containing the maximum marks.
    • List similar to above containing the average marks.
    • List similar to above containing the standard deviations in marks.
    • List similar to above containing the correlation of the ranks of the subject marks and total marks. The highest mark will be ranked as ‘1’, the second highest mark will be ranked ‘2’ and so on.
 '''
 

#function that gets all marks from all students by subject
#E.g. all Maths scores
#Used to manipulate data to calculate the min, max, avg, and sd
def getSubjectTotalScore(stud_data): 
    num_rows = len(stud_data) #get total number of rows in sample_student_marks.csv
    num_cols = len(stud_data[0]) #get total number of columns in sample_student_marks.csv
    unsorted_scores_by_subject = [] #array where to put the data for scores by subject that is unsorted
    
    all_minimums = [] #array where to put all the minimum scores
    all_maximums = [] #array where to put all the maximum scores
    all_averages = [] #array where to put all the average scores
    all_stndrd_devs = [] #array where to put all the std scores
    
    col = 2 #loop starts at column 2 to get the number/figures by column from Maths to Civics scores
    
    while col in range (num_cols):
        for row in range (num_rows): #loop that gets the Maths up to Civics scores by column
            
            unsorted_scores_by_subject.append(stud_data[row][col])
        row +=1
        
        #This line refers to the array that computes the minimum, maximum etc by subject
        #The numbers with string type were converted to float so it can be used for the calculations
        all_minimums.append(mn(convStringToFloatArray(unsorted_scores_by_subject)))
        all_maximums.append(mx(convStringToFloatArray(unsorted_scores_by_subject)))
        all_averages.append(avg(convStringToFloatArray(unsorted_scores_by_subject)))
        all_stndrd_devs.append(std(getvariance(convStringToFloatArray(unsorted_scores_by_subject))))
        
        #Needs to clear the "unsorted_scores_by_subject" array so it can store a new set of data
        unsorted_scores_by_subject.clear();
        
        col +=1       
    
    #Function that computes for the minimum score of all subjects per student
    mn(studentTotalMarks(stud_data))
    #Function that computes for the maximum score of all subjects per student
    mx(studentTotalMarks(stud_data))
    #Function that computes for the avg score of all subjects per student
    avg(studentTotalMarks(stud_data))
    #Function that computes for the std of all subjects per student
    std(getvariance(studentTotalMarks(stud_data)))
    
    #append the minimums of all subjects per student to the all_minimums list
    all_minimums.append(mn(studentTotalMarks(stud_data))) 
    all_maximums.append(mx(studentTotalMarks(stud_data)))
    all_averages.append(avg(studentTotalMarks(stud_data)))
    all_stndrd_devs.append(std(getvariance(studentTotalMarks(stud_data))))
    
    roundnumbers(all_averages)
    roundnumbers(all_stndrd_devs)
    
    
    print("\nMinimums: ", all_minimums)                  
    print("\nMaximums: ", all_maximums)  
    print("\nAverages: ", all_averages)
    print("\nStandard Deviations: ", all_stndrd_devs)
    
    #function that computes correlation between subject and it's totals using the entire student data
    cor(stud_data)
    

#compute for minimum
def mn(minmum):
    return (min(minmum))   

#compute for maximum    
def mx(m):
    return(max(m))

#compute for avg
def avg(lst):
    return sum(lst) / len(lst)

#compute for variance to get standard deviation
def getvariance(mylist):
    mean_value = avg(mylist)
    return sum([(i - mean_value)**2 for i in mylist]) / (len(mylist) -1)

#compute for standard deviation
def std(n):
    if n < 0:
        return
    else:
        return n**0.5
    
def roundnumbers(num):
    for elements in range(len(num)): #round all averages to 4 decimals
        num[elements] = (round(num[elements],4))
    return num


def cor(data):
    #call the function that manipulate the data including extraction of data and calculate the correlation of subjects to total marks
    getNameWithSubjects(data)
    
    
#Function that gets total marks from all subjects by student e.g. total marks of Adam
#This will be used for computing mx, mn, avg, std
def studentTotalMarks(s_data): 
    unsorted_studenttotalmarks = []
    unsorted_student_sum_totals = []
    
    r = len(s_data)
    c = len(s_data[0])
    
    x = 1
    y = 1

    while x in range (r):
        for y in range (c): #loop that gets the scores by subject per student
            unsorted_studenttotalmarks.append(s_data[x][y])
        y +=1
        unsorted_student_sum_totals.append(sum(sortListStudentTotalMarks(unsorted_studenttotalmarks)))
        unsorted_studenttotalmarks.clear();
        x +=1

    return unsorted_student_sum_totals


#function that sorts the list by COLUMN in sample_student_marks.csv then convert all numbers to float and sort them
#this will be used for computing mx, mn, avg, std
def convStringToFloatArray(my_list): 
    sorted_list = []
    for item in my_list[1:]:
        item=float(item)
        sorted_list.append(item)
        sorted_list.sort()
    return sorted_list

#function that sorts the list by ROW (student name) in sample_student_marks.csv then convert all numbers to float and sort them
#this will be used for computing mx, mn, avg, std
def sortListStudentTotalMarks(s_list): 
    sorted_list2 = []
    for item in s_list[2:]:
        item=float(item)
        sorted_list2.append(item)
        sorted_list2.sort()
    return sorted_list2

# This function takes the student names and the marks per subject
# This will be placed in a dictionary to be sorted by mark then by name if having the same mark
# The output will be used in the correlation function
def getNameWithSubjects(d):
    n_rows = len(d) #get total number of rows in sample_student_marks.csv
    n_cols = len(d[0]) #get total number of columns in sample_student_marks.csv
    col = 0 #starts at column 0 to get Name and column 2 to get Maths
    row = 1
    studentnames = [] #empty key list
    subjects = [] #empty values list
    computed_corr =[] #array of computed correlation by subject to total marks of a student
    computed_corr_clean = []
    
    while col in range (n_cols):
        for row in range (n_rows): #loop that gets the name of student and his every subject's score
            if row != 0:
                if col == 0: #column is on STUDENT NAME
                    studentnames.append((d[row][col]))
                elif col > 1: #if column is on SUBJECT e.g. Math, Physics 
                    #print("row[",row,"]","col[",col,"]", d[row][col])
                    subjects.append((d[row][col]))
        #Create a dictionary from zip object of student names and subjects
        names_subjectmarks_dict = dict(zip(studentnames, subjects))
        #print("\nDICTIONARY",names_subjectmarks_dict)

        subjects.clear();
        row +=1
            
        #Function that converts the string numbers to float in the "names_subjectmarks_dict"
        #Then sort the float numbers to be stored in the "names_subjectmarks" which
        #includes student names and subject marks
        names_subjectmarks = sortDictList(convertStrToFloat(names_subjectmarks_dict))
        #print("\nSORTED NAMES WITH SUBJECTS:",names_subjectmarks)
            
        #functions that gets the ranks by subject per studentname
        names_subjectmarks_ranks = getRank(names_subjectmarks)

           
        #this function gets the total marks of all subjects per student and ranked
        namestotalmarks_ranks = getNamesWithTotalMarks(d)
            
           
        #function that gets the rank difference between names_subjectmarks_ranks and namestotalmarks_ranks
        computed_corr.append(getRanksDifference(names_subjectmarks_ranks, namestotalmarks_ranks))
            
            
        #print("\n namestotalmarks_ranks:",namestotalmarks_ranks)
        
        col +=1
    
    #f.append((getRanksDifference(sumbysubject, namestotalmarks_ranks)))   
    #print("\n FFFFFFFF:",f)
    #print("\nSUM OF TOTAL MARKS BY SUBJECT:",sumbysubject)
    #print("\nSUM OF SUMBY SUBJECT",sum(sumbysubject))
    #print("\nCOMPUTED CORR: ",computed_corr)
    #computed_corr.append(sum(sumbysubject))
    
    for e in range(len(computed_corr)): #LOOK FOR Null values in the array and remove
        if computed_corr[e] != None:
            computed_corr_clean.append(computed_corr[e])
    
    for el in range(len(computed_corr_clean)): #round all to 4 decimals
        computed_corr_clean[el] = (round(computed_corr_clean[el],4))
    print("\nCorrelations : ",computed_corr_clean)
    
    


#this function gets the ranks of the total marks of all subjects per student
#this will be used for calculation of correlation to compare sbjects marks vs. total marks
def getNamesWithTotalMarks(marks):
    num_rows = len(marks) #get total number of rows in sample_student_marks.csv
    num_cols = len(marks[0]) #get total number of columns in sample_student_marks.csv
    
    student_names = []

    
    row = 0
    col = 0

    while row in range (num_rows):
        for col in range (num_cols): #loop that gets the scores by subject per student in sample_student_marks.csv
            if row != 0:
                if col == 0: #if column is on STUDENT NAME, get the student name
                    student_names.append(marks[row][col])
                    #print("row[",row,"]","col[",col,"]", marks[row][col])
        row +=1
        col +=1
    
    #I created a dictionary list that stores the sum of all marks from all subjects per student which is from the "studentTotalMarks" function
    names_totalmarks = dict(zip(student_names, studentTotalMarks(marks)))
    #print("\nSTUDENTS with THEIR totalmarks DICTIONARY\n",names_totalmarks)
    
    #after creating the dictionary of all of the sum of marks by student name,
    #this function below will convert the numbers to float, then sort by highest number of total marks by student
    #e.g [('AHBAR', 587.0), ('ADAMA', 556.0),....)]
    sorted_names_totalmarks = sortDictList(convertStrToFloat(names_totalmarks))
    #print("\nSORTED TOTAL MARKS",sorted_names_totalmarks)
    
    #After sorting, then now gets the rank of the totalmarks by putting the it in the 3rd element of the tuple list
    #e.g [('AHBAR', 587.0, 1)
    names_totalmarks_ranks = getRank(sorted_names_totalmarks)
    #print("\n\n\n RANK OF TOTAL MARKS:",names_totalmarks_ranks)
    
    return names_totalmarks_ranks



#function that gets the rank of the tuple lists in "getNamesWithTotalMarks" function
#this will be used for calculation of getNamesWithTotalMarks() function
def getRank(tuple_list):
    
    rank_position = 0
    skip = 0
    prev = None
    i= 0
    result = []
    
    for stud_name, stud_mark in tuple_list:
        if stud_mark == prev:
            skip += 1
        else:
            rank_position += skip + 1
            skip = 0
        i +=1
        result.append((stud_name, stud_mark, i))    
        prev = stud_mark
    
    return result

#Function that gets the difference of ranks between two nested of tuples (RANK By SUBJECTS vs. RANK By TOTAL MARKS
#to be used in correlation function
def getRanksDifference(math_marks, totalmarks):
    stud_name = []
    rank_diff = []
    dsquared = []

    #for loop that takes the student name, his/her rank by subject and then total rank, then get the difference of both
    #the rank difference value is stored in rank_diff[]
    for i in range (len(math_marks)):
        for j in range (len(totalmarks)):
            if math_marks[i][0] == totalmarks[j][0]:
                stud_name.append(math_marks[i][0])
                rank_diff.append(math_marks[i][2]-totalmarks[j][2])
                break
    
    #for loop that appends the square of rank difference array which is stored in the dsquared array
    for x in range (len(rank_diff)):
        dsquared.append(getSquare(rank_diff[x]))
       
    #the dsquared array values will be used to get the sum of all numbers in the array then compute for the correlation 
    computed_corr = (computeCorrelation(sum(dsquared), rank_diff))
    return computed_corr 

#Function that computes correlation using the formula
#Refer to this url: https://www.youtube.com/watch?v=CV25hmd9O1c
def computeCorrelation(sum_dsquared, rank_difference):
    product_6dsquared = 6 * sum_dsquared
    n = len(rank_difference)
    n_squared = n*n
    val = n * (n_squared -1)
    
    while product_6dsquared != 0 and val != 0:
        r = 1 - (product_6dsquared/val)
        return r
        
    
    

#to be used in correlation function
def getSquare(num):
    square = num* num
    return square


#Function that converts numbers that are in string type to float type from a dictionary
#to be used in correlation function
def convertStrToFloat(dictionary):
    dictionary = [dict([key, float(value)]
            for key, value in dictionary.items())]
    return dictionary

#Function that sorts the dictionary list by highest subject score then student name to be used in correlation function
def sortDictList(dict_list):
    l=sorted(dict_list[0].items(), key=lambda x: (x[1],x[1]), reverse=True)
    return l


def main(csvfile): #main function
    student_data = [] #reading the csv file
    file = open(csvfile,"r")
    for line in file:
        List1 = line.split(",")
        List1[len(List1)-1] = List1[len(List1)-1].replace("\n", "") 
        student_data.append(List1)
    file.close()
    getSubjectTotalScore(student_data) #calling mn function
    


if __name__== "__main__":
    main('sample_student_marks.csv')

  