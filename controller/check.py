from util.validation import is_valid_email, is_valid_password, is_valid_mobile

diction = {1: {"name": "ram", "age": 22, "mark": 77}, 2: {"name": "rahul", "age": 22, "mark": 77}}


print(diction.pop(1))
"""def get_customer():
    print("hii")
    for e in dict2:
        print(e)
        yield dict2[e]


values = get_customer()
for i in values:
    for i2 in i:
        print(i2, "-", i[i2])"""


result = is_valid_mobile("5876765431")
if result:
    print("valid")
else:
    print("Not valid")


"""def customer_validation():
    while True:
        customer_name = input("Enter the customer name: ")
        if is_valid_name(customer_name):
            customer_email = input("Enter the email: ")
            if is_valid_email(customer_email):
                password = input("Enter the password: ")
                if is_valid_password(password):
                    mobile_no = input("Enter the mobile number: ")
                    if is_valid_mobile(mobile_no):
                        account_no = input("Enter the account number: ")
                        return customer_name, customer_email, password, mobile_no, account_no
                    else:
                        print("Mobile number should've 10 digits,"
                              " and prefix with 6, 7, 8, 9")
                else:
                    print("Use least 8 characters, one uppercase letter, "
                          "one lowercase letter, one number and "
                          "must not contain space")
            else:
                print("Email shall contains lowercase letters,numbers, "
                      "and ends with suffix (@gmail.com)")
        else:
            print("Name should only contain lowercase, uppercase and space")"""

