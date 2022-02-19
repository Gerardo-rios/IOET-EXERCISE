from datetime import datetime
from itertools import combinations

def read_txt(fpath):
    """
    function that reads the file with the input data
    Args:
        fpath(str): directory of the file to be read 
    return: data in file
    """
    data = ""
    with open(fpath) as file_out:
        for line in file_out:
            data += line 
    return data
    
def get_employes():
    """
    function to create an matrix with the schedules of each employee
    Args:
    return: matrix employes
    """
    rows = read_txt("input.txt").split("\n") 
    employes_schedules = []

    for row in rows:
        if row:
            employes_schedules.append(row.split("="))

    return employes_schedules

def is_encounter(arrival_employe1, exit_employe1, arrival_employe2, exit_employe2):
    """
    function that checks if two schedules intersect each other
    Args:
        arrival_employe1(datetime): arrival time employe 1
        exit_employe1(datetime): exit time employe 1
        arrival_employe2(datetime):arrival time employe 2
        exit_employe2(datetime):exit time employe 1
    return: bool
    """
    if ((arrival_employe1 <= exit_employe2) and (arrival_employe2 <= exit_employe1)):
        return True
    else:
        return False

def compare_schedules(schedule_employeA, schedule_employeB):
    """
    Counter of encounters between employee A and employee B
    Args:
        schedule_employeA(array): entries and exits of each day of the employee A
        schedule_employeB(array): entries and exits of each day of the employee B
    return: (int): number of encounters between employee a and b
    """
    encounters = 0

    for day_hours in schedule_employeA:
        
        start_end_employe1 = day_hours[2:].split("-")
        Start1 = datetime.strptime(start_end_employe1[0],"%H:%M")
        End1 = datetime.strptime(start_end_employe1[1],"%H:%M")

        for day_hour in schedule_employeB:

            start_end_employe2 = day_hour[2:].split("-")
            Start2 = datetime.strptime(start_end_employe2[0],"%H:%M")
            End2 = datetime.strptime(start_end_employe2[1],"%H:%M")
            
            if day_hours[:2] == day_hour[:2]:
                if is_encounter(Start1, End1, Start2, End2):
                    encounters += 1
            else:
                continue

    return encounters


def write_txt(employe_name1, employe_name2, encounters, fpath):
    """
    Function to store the result in a txt file
    Args:
        employe_name1(string): name of employe A
        employe_name2(string): name of employe B
        encounters(int): encounters between employee a and b
        fpath(string): directory of the file to be written
    return:
    """
    with open(fpath, "a") as file_in:
        file_in.write(employe_name1 + "-" + employe_name2 + ":" + str(encounters) + "\n")

def main_count():
    """
    main function to display and save results
    Args:
    return:
    """
    employes = get_employes()
    combinations_to_compare = list(combinations(employes, 2))
    for i in combinations_to_compare:
        print(i[0][0], "-", i[1][0], ":", compare_schedules(i[0][1].split(","), i[1][1].split(",")))
        write_txt(i[0][0], i[1][0], compare_schedules(i[0][1].split(","), i[1][1].split(",")), "results.txt")


main_count()


 
