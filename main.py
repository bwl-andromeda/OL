print("Добро пожаловать в мою компьютерную викторину!")

playing = input("Хотите поиграть?\n")

if playing.lower() != "да":
    quit()

print("Хорошо! Давайте поиграем :)")
score = 0

answer = input("Что означает процессор? ")
if answer.lower() == "центральное процессорное устройство":
    print("Правильно!")
    score += 1
else:
    print("Неправильно!")

answer = input("Что означает GPU? ")
if answer.lower() == "устройство обработки графики":
    print("Правильно!")
    score += 1
else:
    print("Неправильно!")

answer = input("Что означает оперативная память? ")
if answer.lower() == "память с произвольным доступом":
    print("Правильно!")
    score += 1
else:
    print("Неправильно!")

answer = input("Что означает PSU? ")
if answer.lower() == "источник питания":
    print("Правильно!")
    score += 1
else:
    print("Неправильно!")

answer = input("Что означает программа?")
if answer.lower() == "программное обеспечение":
    print("Правильно!")
    score += 1


answer = input("Что означает процессор? ")
if answer.lower() == "центральное процессорное устройство":
    print("Правильно!")
    score += 1
else:
    print("Неправильно!")

print("Ты получил " + str(score) + " правильных ответов!")
if (score / 4 * 100) > 80:
    print(f"Ты молодец! Вот твой результат в процентном соотношении: {(score/4)*100}%.")
elif (score / 4 * 100) <= 80 and (score / 4 * 100) >= 50:
    print(
        f"Очень даже хорошо! Твой результат в процентном соотношении: {(score/4)*100}%."
    )
else:
    print(
        f"Попробуй еще раз! Твой результат в процентном соотношении: {(score/4)*100}%."
    )
