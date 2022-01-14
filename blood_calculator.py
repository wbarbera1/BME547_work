def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Total")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            choice = "HDL"
            HDL_driver(choice)
        elif choice == "2":
            choice = "LDL"
            HDL_driver(choice)
        elif choice == "3":
            choice = "Total Cholesterol"
            HDL_driver(choice)
        elif choice == "9":
            keep_running = False
        else:
            print("ERROR: Input a number corresponding to a presented test option")
    return


def accept_input(test_name):
    entry = input("Enter the {} test result: ".format(test_name))
    return int(entry)


def check_HDL(test_name, HDL_val):
    if test_name == "HDL":
        if HDL_val >= 60:
            answer = "Normal"
        elif 60 > HDL_val >= 40:
            answer = "Borderline Low"
        else:
            answer = "Low"
    elif test_name == "LDL":
        if HDL_val < 130:
            answer = "Normal"
        elif 159 > HDL_val >= 130:
            answer = "Borderline High"
        elif 189 > HDL_val >= 160:
            answer = "High"
        else:
            answer = "Very High"
    elif test_name == "Total Cholesterol":
        if HDL_val < 200:
            answer = "Normal"
        elif 239 > HDL_val >= 200:
            answer = "Borderline High"
        else:
            answer = "High"
    return answer


def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}.".format(test_value, test_name, test_class)
    print(out_string)
    return
    
  
def HDL_driver(test_selection):
    HDL_val = accept_input(test_selection)
    classification = check_HDL(test_selection, HDL_val)
    print_result(test_selection, HDL_val, classification)
    
 
interface()