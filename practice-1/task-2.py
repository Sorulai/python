# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

x = 60
time = int(input('Введите время в секундах: '))

hours = time / x / x
minutes = (hours - int(hours)) * x
secs = (minutes - int(minutes)) * x

print(f'В {time} секундах - {int(hours)}:{int(minutes)}:{int(secs)}')
