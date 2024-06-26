APP_TITLE = 'QRKot'
APP_DESCRIPTION = 'Благотворительный фонд поддержки котиков'
APP_URL = 'sqlite+aiosqlite:///./fastapi.db'
MIN_LENGHT_PASSWORD = 3
USER_IS_REGISTERED = 'Пользователь {} зарегистрирован.'
WARNING_LENGHT_PASSWORD = 'Password should be at least 3 characters'
WARNING_PASSWORD_CONTAIN_EMAIL = 'Пароль не должен содержать e-mail'
WARNING_PROJECT_NOT_FOUND = 'Проект не найден!'
WARNING_PROJECT_NOT_EDIT = 'Закрытый проект нельзя редактировать!'
WARNING_PROJECT_NOT_DELETE = (
    'В проект были внесены средства, не подлежит удалению!'
)
WARNING_PROJECT_NAME_NOT_UNIQUE = 'Проект с таким именем уже существует!'
WARNING_PROJECT_INVEST = (
    'В проект были внесены средства, не подлежит удалению!'
)
WARNING_PROJECT_AMOUNT = (
    'Нелья установить значение full_amount меньше уже вложенной суммы.'
)
WARNING_USER_DELETE = 'Удаление пользователей запрещено!'
PROJECT_CREATE_EXAMPLES = {
    'project1': {
        'summary': 'Правильный запрос',
        'value': {
            'name': 'Хороший кот - здоровый кот!',
            'description': 'Средства на медицинское обслуживание',
            'full_amount': 200_000
        }
    },
    'project2': {
        'summary': 'Отсутствует обязательный параметр',
        'value': {
            'name': 'Всех по коммуналкам!',
            'full_amount': 100_000
        }
    },
    'project3': {
        'summary': 'Некорректная требуемая сумма пожертвований',
        'value': {
            'name': 'Счастливый кот - сытый кот!',
            'description': 'Средства на корм оставшимся без попечения кошкам',
            'full_amount': -500_000
        }
    }
}
PROJECT_UPDATE_EXAMPLES = {
    'project1': {
        'summary': 'Правильный запрос',
        'value': {
            'name': 'Хороший кот - мертвый кот!',
            'description': 'Средства на медицинское обслуживание',
            'full_amount': 300_000
        }
    },
    'project2': {
        'summary': 'Имя проекта уже есть в БД',
        'value': {
            'name': 'Хороший кот - здоровый кот!',
            'description': 'Средства на лечение',
            'full_amount': 400_000
        }
    },
    'project3': {
        'summary': 'Уменьшение суммы пожертвований',
        'value': {
            'description': 'Средства на корм оставшимся без попечения кошкам',
            'full_amount': 50_000
        }
    }
}
DONATION_CREATE_EXAMPLES = {
    'donation1': {
        'summary': 'Правильный запрос',
        'value': {
            'full_amount': 50,
            'comment': 'Пожертвования от мецената',
        }
    },
    'donation2': {
        'summary': 'Отсутствует обязательный параметр',
        'value': {
            'comment': 'Пожертвования от любителя котов',
        }
    },
    'donation3': {
        'summary': 'Некорректная сумма пожертвования',
        'value': {
            'full_amount': -100_000,
            'comment': 'Очень не люблю кошек',
        }
    }
}
