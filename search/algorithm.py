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

    already_react = TgUser.objects.filter(received_reactions__sender__tg_id=tg_user.tg_id)
    reacted_tg_users = TgUser.objects.filter(sent_reactions__receiver=tg_user)

    return (TgUser.objects
            .exclude(tg_id=tg_user.tg_id).filter()
            .filter(city=tg_user.city)
            .exclude(sex=not_preferred_sex)
            .exclude(sex_preference=other_sex)
            .exclude(tg_id__in=already_react)
            .exclude(tg_id__in=reacted_tg_users)
            )
