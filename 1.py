DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        for friend in DATABASE:
            friends_string += friend + ' '
        return 'Твои друзья: ' + friends_string
    else:
        return '<неизвестный запрос>'

# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
