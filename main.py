import json

def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

print("Do you have an account?**")
ac = input("Yes\nNo\n").lower()

if ac == "no":
    username = input("Enter your name:--- ")
    mnumber = input("Enter your mobile number:--- ")

    userdata = {
        "name": username, 
        "Mobile Number": mnumber
    }

    try:
        with open("ac.json", 'r') as json_file:
            data = json.load(json_file)
            temp = data["accounts"]
            temp.append(userdata)
    except FileNotFoundError:
        data = {"accounts": [userdata]}

    write_json(data, "ac.json")

elif ac == "yes":
    uc = int(input("1. Yes \n2. No/exit \n: "))

    if uc == 1:
        subject = input("Enter the subject:---\n science \n maths\n:--").lower()
        if subject not in ["science", "maths"]:
            print("Select the correct subject")
            exit()
        num_questions = int(input("Enter the number of questions (Less than 10):---"))
        if num_questions > 10:
            print("Enter the questions less than 10")
            exit()

        try:
            with open("app.json", 'r') as json_file:
                data = json.load(json_file)
                temp = data["quiz"]
        except FileNotFoundError:
            data = {"quiz": []}
            temp = data["quiz"]

        for _ in range(num_questions):
            question = input("Enter the Question:--- ")
            opt1 = input("Enter option a:--- ")
            opt2 = input("Enter option b:--- ")
            opt3 = input("Enter option c:--- ")
            opt4 = input("Enter option d:--- ")
            ans = input("Enter the correct answer:--- ")

            new_question = {
                "question": question,
                "Ans1": opt1,
                "Ans2": opt2,
                "Ans3": opt3,
                "Ans4": opt4,
                "Ans": ans
            }

            temp.append(new_question)

        write_json(data, "app.json")

    else:
        print("Exiting...")

else:
    print("Invalid input. Exiting...")
