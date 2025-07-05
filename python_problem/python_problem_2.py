#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(students,info) :
    #사전에 학생 정보 저장하는 코딩 
    name=info[0]
    score1=int(info[1])
    score2=int(info[2])
    students[name]=[score1,score2,""]

##############  menu 2
def Menu2(students):
    for name, info in students.items():
        if info[2] == "":  
            avg = (info[0] + info[1]) / 2

            if avg >= 90:
                grade = "A"
            elif avg >= 80:
                grade = "B"
            elif avg >= 70:
                grade = "C"
            else:
                grade = "D"

            info[2] = grade  


##############  menu 3
def Menu3(students) :
    #출력 코딩
    print("-----------------------------")
    print(f"{'name':<10}{'mid':<6}{'final':<7}{'grade':<6}")
    print("-----------------------------")
    for name in students :
      info=students[name]
      print(f"{name:<10}{info[0]:<6}{info[1]:<7}{info[2]:<6}")

##############  menu 4
def Menu4(students,name):
    del students[name]
    
## 양의 정수 check
def is_positive_integer(s):
    return s.isdigit() and int(s) > 0

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
students={}
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        info = input("Enter name mid-score final-score: ").split()
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        if len(info) != 3:
          print("Num of data is not 3!")
        elif info[0] in students:
          print("Already exist name!")
        elif not (is_positive_integer(info[1]) and is_positive_integer(info[2])):
          print("Score is not positive integer!")
        #예외사항이 아닌 입력인 경우 1번 함수 호출 
        else: 
          Menu1(students, info)

    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if not students:
          print("No student data!")
        #예외사항이 아닌 경우 2번 함수 호출
        else:
          Menu2(students)
          print("grading to all students")

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        if not students:
          print("No student data!")
        elif any(check[2]=="" for check in students.values()):
          print("There is a student who did't get grade.")
        #예외사항이 아닌 경우 3번 함수 호출
        else:
          Menu3(students)
    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        if not students:
          print("No student data!")
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        else:
          name = input("Enter the name to delete : ")
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
          if name not in students:
            print("Not exist name!")
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
          else:
            Menu4(students, name)
            print(f"{name} student information is deleted.")

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        print("Exit Program!")
        #반복문 종료
        break
    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number. Choose again.")
    