print("Welcome to Students Record Analyzer.")

students = {
    "Alice": {"Math": 90, "Science": 85, "English": 78},
    "Bob": {"Math": 75, "Science": 88, "English": 92},
    "Charlie": {"Math": 60, "Science": 70, "English": 35},
    "David": {"Math": 45, "Science": 42, "English": 44},
}

# print(students)


def get_total(scores):
    return sum(scores.values())


def get_result(scores, pass_mark=40):
    for mark in scores.values():
        if mark < pass_mark:
            return "Fail"
    return "Pass"

# def get_top_student(data):
#     pass


def get_top_student(data):
    top_name = ""
    top_total = 0

    for name, marks in data.items():
        total = get_total(marks)

        if total > top_total:
            top_total = total
            top_name = name
    print("Top Student:", top_name, "with", top_total, "marks")
    

def get_attention_students(data):
    attention_list = []
    num_subjects = len(next(iter(data.values())))
    max_total = num_subjects * 100

    for name, marks in data.items():
        # pass
        total = get_total(marks)
        result = get_result(marks)

        if total < (max_total / 2) or result == "Fail":
            attention_list.append(name)
    print("Students needing attention:", attention_list)


def get_subject_totals(data):
    totals = {}

    for scores in data.values():
        for subject, mark in scores.items():
            totals[subject] = totals.get(subject, 0) + mark
    return totals

def get_easiest_subject(data):
    totals = get_subject_totals(data)

    easiest = max(totals, key=totals.get)

    return easiest, totals[easiest]


def get_hardest_subject(data):
    totals = get_subject_totals(data)
    hardest = min(totals, key=totals.get)
    return hardest, totals[hardest]

# def print_scores(data):

#     print("Student   | Math | Science | English ")
#     print("-------------------------------------")

#     for name, marks in data.items():
#         # print(name, marks["Math"], marks["Science"], marks["English"])

#         # total = get_total(marks)

#        print(f"{name:<9} | {marks['Math']:<4} | {marks['Science']:<7} | {marks['English']:<7}")

def print_scores(data):
    print("Student   | Math | Science | English | Total | Result")
    print("--------------------------------------------------------")
    for name, marks in data.items():
        total = get_total(marks)
        result = get_result(marks)
        print(f"{name:<9} | {marks['Math']:<4} | {marks['Science']:<7} | {marks['English']:<7} | {total:<5} | {result}")
    
print_scores(students)

get_top_student(students)

get_attention_students(students)

subject, total = get_easiest_subject(students)
print("Easiest Subject:", subject, "with", total, "total marks")

subject, total = get_hardest_subject(students)
print("Hardest Subject:", subject, "with", total, "total marks")


# # Menu System
# print("\nMenu:")
# print("1. Show All Student Scores")
# print("2. Show Top Student")
# print("3. Show Students Needing Attention")
# print("4. Show Easiest Subject")
# print("5. Show Hardest Subject")

# choice = int(input("\nEnter your choice (1-5): "))


# if choice == 1:
#     print_scores(students)
# elif choice == 2:
#     get_top_student(students)
# elif choice == 3:
#     get_attention_students(students)
# elif choice == 4:
#     subject, total = get_easiest_subject(students)
#     print("Easiest Subject:", subject, "with", total, "total marks")
# elif choice == 5:
#     subject, total = get_hardest_subject(students)
#     print("Hardest Subject:", subject, "with", total, "total marks")
# else:
#     print("Invalid choice. Please run again.")


while True:
    print("\nMenu:") 
    print("1. Show All Student Scores") 
    print("2. Show Top Student") 
    print("3. Show Students Needing Attention") 
    print("4. Show Easiest Subject") 
    print("5. Show Hardest Subject")
    print("0. Exit")

    choice = int(input("\nEnter your choice (1-5): "))
    if choice == 1:
        print_scores(students)
    elif choice == 2:
        get_top_student(students)
    elif choice == 3:
        get_attention_students(students)
    elif choice == 4:
        subject, total = get_easiest_subject(students)
        print("Easiest Subject:", subject, "with", total, "total marks")
    elif choice == 5:
        subject, total = get_hardest_subject(students)
        print("Hardest Subject:", subject, "with", total, "total marks")
    elif choice == 0:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please run again.")