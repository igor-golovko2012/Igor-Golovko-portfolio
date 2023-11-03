# объявление функции
def is_palindrome(text):
    text = text.lower()
    a = []
    for i in text:
        if i in('abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'):
             a.append(i)
    b = a[::-1]  

    if a == b:
        return True
    else: 
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))