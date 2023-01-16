user_name = input("이름 입력>> ")
age = input("나이 입력>> ")
email = input("이메일 입력>> ")
phone = input("전화번호 입력>> ")

print("{:-^60}".format("입력 결과"))
print("{: ^10}|{: ^5}|{: ^20}| {: ^20}".format("name","age", "email", "phone"))
print("-"^65)
print("{: ^10}|{: ^5}|{: ^20}| {: ^20}".format(user_name, age, email, phone))