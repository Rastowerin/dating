from tg_users.models import TgUser


def search_algorithm(tg_user: TgUser):

    other_sex = {
        'MALE': 'FEMALE',
        'FEMALE': 'MALE'
    }[tg_user.sex]

    not_preferred_sex = {
        'MALE': 'FEMALE',
        'FEMALE': 'MALE',
        'ANY': None
    }[tg_user.sex_preference]

    return (TgUser.objects
            .exclude(tg_id=tg_user.tg_id).filter()
            .filter(city=tg_user.city)
            .exclude(sex=not_preferred_sex)
            .exclude(sex_preference=other_sex))
