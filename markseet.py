students = {}

def add_student(name, marks):
    students[name] = marks
    print(f"Added {name}")

def grade(score):
    if score >= 90: return "A"
    elif score >= 75: return "B"
    elif score >= 60: return "C"
    elif score >= 40: return "D"
    else: return "F"

def show_stats():
    if not students:
        print("No data.")
        return
    all_scores = [sum(m.values())/len(m) for m in students.values()]
    print(f"Class Average: {sum(all_scores)/len(all_scores):.2f}")
    print(f"Highest Average: {max(all_scores):.2f}")
    print(f"Lowest Average: {min(all_scores):.2f}")

def rank_students():
    ranked = sorted(students.items(), key=lambda x: sum(x[1].values())/len(x[1]), reverse=True)
    print("\n--- Rankings ---")
    for i, (n, m) in enumerate(ranked, 1):
        avg = sum(m.values())/len(m)
        print(f"{i}. {n} - Avg: {avg:.2f} Grade: {grade(avg)}")

def search_student(name):
    if name in students:
        marks = students[name]
        avg = sum(marks.values())/len(marks)
        print(f"\n{name}'s Report:")
        for subj, score in marks.items():
            print(f"{subj}: {score}")
        print(f"Average: {avg:.2f} | Grade: {grade(avg)}")
    else:
        print("Student not found!")

def main():
    while True:
        print("\n--- Marks Analyzer Menu ---")
        print("1. Add Student")
        print("2. Show Class Stats")
        print("3. Rank Students")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")
            marks = {}
            while True:
                subj = input("Enter subject (or blank to stop): ")
                if not subj: break
                score = int(input(f"Enter marks for {subj}: "))
                marks[subj] = score
            add_student(name, marks)

        elif choice == "2":
            show_stats()

        elif choice == "3":
            rank_students()

        elif choice == "4":
            name = input("Enter student name: ")
            search_student(name)

        elif choice == "5":
            print("Closing Marks Analyzer. Bye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
