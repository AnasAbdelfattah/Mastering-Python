def scorToGrade(scores):
    
    grades=[]
    for score in scores:
        if 100>= int(score) >=90:
            grades.append("A")
        elif 90> int(score) >=80:
            grades.append("B")
        elif 80> int(score) >=70:
            grades.append("C")
        elif 70> int(score) >=60:
            grades.append("D")
        else:
            grades.append("F")
    

    return grades