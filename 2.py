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
    elif query == 'Где все мои друзья?':
        return 'Я поняла, это вопрос про города!'

# Приветствие и ввод вопроса пользователем
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))

# Вызов функции с аргументом 'Где все мои друзья?'
print(process_anfisa('Где все мои друзья?'))
