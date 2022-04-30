import importlib.util

# load email gen module
spec = importlib.util.spec_from_file_location("generate_email_address", "./email_gen/email_gen.py")
emailMod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(emailMod)

# load group moduel
spec = importlib.util.spec_from_file_location("get_sorted_birth_dates", "./group_work/group_work.py")
groupMod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(groupMod)

menu_exit = False
error_msg = ""
answ = ''
answList = [0, 1, 2]
while not menu_exit:
    if len(error_msg) > 0:
        print(error_msg)
    print("\nWelcome to interface 2.0\n")
    print("1 - Generate Email")
    print("2 - List group sorted by birth dates")
    print("0 - Exit")
    answ = input()

    if int(answ) not in answList:
        error_msg = "Wrong answer"
    else:
        if int(answ) == 1:
            print(emailMod.generate_email_address(), '\n')
        elif int(answ) == 2:
            print(groupMod.get_sorted_birth_dates(), '\n')
        elif int(answ) == 0:
            menu_exit = True



