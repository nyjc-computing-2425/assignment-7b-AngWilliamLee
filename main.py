# Built-in imports
import math

# Your code below
GRADE = {}
for score in range(100+1):
    if score >= 70:
        GRADE[score] = 'A'
    elif score >= 60:
        GRADE[score] = 'B'
    elif score >= 55:
        GRADE[score] = 'C'
    elif score >= 50:
        GRADE[score] = 'D'
    elif score >= 45:
        GRADE[score] = 'E'
    elif score >= 40:
        GRADE[score] = 'S'
    else:
        GRADE[score] = 'U'
        

def read_testscores(filename):
    """
    Given a a csv file, returns a list of dictionaries

    Parameter
    ---------
    filename
        csv file containing student data

    Returns
    -------
    list
        list of dicitonaries, with each dictionary representing a student's data
    """
    with open(filename, 'r') as f:
        f.readline() == "" #ignore header
        allstudentdata = []
        for row in f:
            row_str = row.strip().split(",")
            studentdata = {}
            studentdata["class"] = row_str[0]
            studentdata['name'] = row_str[1]
            p1 = int(row_str[2])
            p2 = int(row_str[3])
            p3 = int(row_str[4])
            p4 = int(row_str[5])
            overall = math.ceil((p1/30 * 15) + (p2/40 * 30) + (p3/80 * 35) + (p4/30 * 20))
            studentdata["overall"] = overall
            grade = GRADE[overall]
            studentdata["grade"] = grade
            allstudentdata.append(studentdata)

    return allstudentdata    
    

def analyze_grades(studentdata):
    """
    Given a list of dictionaries of student's data, returns a dictionary contianing each class's grades data

    Parameter
    ---------
    studentdata
        list of dictionaries

    Returns
    -------
    analysis
        dictionary of dictionaries
    """

    analysis = {}

    for student in studentdata:
        class_ = student['class']
        grade = student["grade"]   
        if class_ not in analysis:
            analysis[class_] = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'S': 0, 'U': 0}

        if grade in analysis[class_]:
            analysis[class_][grade] += 1

    return analysis




