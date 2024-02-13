import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["student_management"]
collection = db["students"]

def add_student(name, age, grade):
    student = {"name": name, "age": age, "grade": grade}
    collection.insert_one(student)
    print("Student added successfully.")

def display_students():
    students = collection.find()
    print("List of Students:")
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = input("Enter student's grade: ")
            add_student(name, age, grade)
        elif choice == "2":
            display_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
