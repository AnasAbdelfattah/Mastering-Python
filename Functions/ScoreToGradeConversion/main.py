from function import scorToGrade

# Start main
def main():
    scores = []

    try:
        howManySubjects = int(input("Enter how many subjects: "))

        # Getting the scores of subjects
        for subject in range(1, howManySubjects + 1):
            score = float(input(f'Enter score for subject {subject}: '))
            scores.append(score)

        grades = scorToGrade(scores)
        print("Grades:", grades)

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the number of subjects.")

# End main

if __name__ == "__main__":
    main()
