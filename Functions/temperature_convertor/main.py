from conversion import F_to_C, F_to_K

def main():
    degree = input("Enter the degree: ")

    which_degree = input("Do you want to convert to 1. Celsius or 2. Kelvin? ")
    while not which_degree.isdigit() or int(which_degree) not in [1, 2]:
        print('Error, enter only 1 or 2')
        which_degree = input()

    if which_degree == '1':
        print(f"The degree in Celsius = {F_to_C(degree):.2f}")

    if which_degree == '2':
        print(f"The degree in Kelvin = {F_to_K(degree):.2f}")

if __name__ == "__main__":
    main()
