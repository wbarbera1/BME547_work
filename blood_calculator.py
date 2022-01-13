def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1-HDL")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "1"
            choice = "HDL"
        elif choice == "9":
            keep_running = False
    return


def accept_input(test_name):
    entry = input("Enter the {} test result: ".format(test_name))
    return int(entry)


def check_HDL(HDL_val)
    if HDL_val >= 60
        answer = "Normal"
    elif 60 > HDL >= 40
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def print_result(test_name, test_value, test_class)
    out_string = "The test value of {} for {} is {}.".format(test_value, test_name, test_class)
    print(out_string)
    return
    
  
def HDL_driver(test_selection):
    HDL_val = accept_input("HDL")
    classification = check_HDL(HDL_val)
    print_result("HDL", HDL_value, classification)
    
 
interface()