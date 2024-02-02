APP_TITLE = 'QRKot'
APP_DESCRIPTION = 'Благотворительный фонд поддержки котиков'
APP_URL = 'sqlite+aiosqlite:///./fastapi.db'
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
