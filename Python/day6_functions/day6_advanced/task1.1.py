def analyze_grades(grades):
    highest_grade=max(grades)
    lowest_grade=min(grades)
    average=sum(grades)/len(grades)
    print(highest_grade,lowest_grade,average)

grade_list=[25, 70, 45, 65, 10, 20, 30]
analyze_grades(grade_list)
