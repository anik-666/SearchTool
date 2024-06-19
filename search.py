import json

def load_student_database(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def search_students(student_database, ids=None, names=None, emails=None):
    results = []
    for student in student_database:
        if ids and student['student_id'] in ids:
            results.append(student)
        elif names and student['name'] in names:
            results.append(student)
        elif emails and student['email'] in emails:
            results.append(student)
    return results

def get_input_set(prompt):
    input_set = set()
    print(prompt)
    while True:
        user_input = input("Enter value (or press Enter to finish): ")
        if user_input == "":
            break
        input_set.add(user_input)
    return input_set

def main():
    file_path = 'C:/Users/admin/Desktop/anik.json'
    student_database = load_student_database(file_path)

    print("Choose search criteria:")
    print("1. Student IDs")
    print("2. Names")
    print("3. Emails")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        input_ids = get_input_set("Enter student IDs:")
        results = search_students(student_database, ids={int(id) for id in input_ids})
    elif choice == "2":
        input_names = get_input_set("Enter names:")
        results = search_students(student_database, names=input_names)
    elif choice == "3":
        input_emails = get_input_set("Enter emails:")
        results = search_students(student_database, emails=input_emails)
    else:
        print("Invalid choice.")
        return

    if results:
        print("Found the following students:")
        for student in results:
            print(student)
    else:
        print("No matching students found.")

if __name__ == "__main__":
    main()