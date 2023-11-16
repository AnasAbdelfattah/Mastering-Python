from function import rectangular_to_polar

#start program
def main():
    x=input("enter the x coordinate : ")
    y=input("enter the y coordinate : ")
    result=rectangular_to_polar(x,y)

    print(f"r={result[0]:.2f}  theta ={result[1]:.2f}")
#end program


if __name__ == "__main__":
    main()