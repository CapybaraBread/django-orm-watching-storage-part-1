import os
import django  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    Passcard = Passcard.objects.all()
    print(Passcard[0].created_at)
    print(Passcard[0].is_active)
    print(Passcard[0].owner_name)
    print(Passcard[0].passcode)

    # passcard_active_person = 0
    # for passcard in Passcard:
    #     if passcard.is_active == True:
    #         passcard_active_person += 1
    # print(passcard_active_person)

    published_posts = Passcard.filter(is_active=True)
    print('Количество активных пропусков:', len(published_posts))