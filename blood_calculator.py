def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
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
    

interface()