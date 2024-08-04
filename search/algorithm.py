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

    tg_users_who_liked = TgUser.objects.filter(sent_likes__receiver=tg_user)

    return (TgUser.objects
            .exclude(tg_id=tg_user.tg_id).filter()
            .filter(city=tg_user.city)
            .exclude(sex=not_preferred_sex)
            .exclude(sex_preference=other_sex)
            .exclude(tg_id__in=tg_users_who_liked)
            )
