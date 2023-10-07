# if 조건문에 else 구문을 추가해서짝수와 홀수 구분하기
# 입력
number = input("정수 입력> ")
number = int(number)            # 입력받은 정수(문자열)을 정수로 변환하여 number에 저장

# 조건문 사용
if number % 2 == 0:
    # 조건이 참일 때, 짝수 조건
    print("짝수입니다.")

else:
    # 조건이 거짓일 때, 홀수 조건
    print("홀수입니다.")