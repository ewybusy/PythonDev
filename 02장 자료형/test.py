# 사용자로부터 이름과 성적을 입력받아 총점과 평균을 구해 출력하는 
# 프로그램을 작성하시오.
name = input("이름를 입력하세요: ")
kor = input("국어 점수를 입력하세요: ")
eng = input("영어 점수를 입력하세요: ")
math = input("수학 점수를 입력하세요: ")

total = int(kor) + int(eng) + int(math) # str --> int
avg = total / 3

print(name, "님의 총점=", total, "평균= ", avg, "입니다.")
print("%s님의 총점= %d, 평균= %f입니다." % (name, total, avg))
print("{}님의 총점= {}}, 평균= {}}입니다.".format(name, total, avg))
print(f"{name}님의 총점= {total}, 평균= {avg}입니다.")

# print("입력하신 이름은 : ", name, "입니다.")
# print(type(data))