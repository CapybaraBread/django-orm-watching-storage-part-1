import os
import django  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard 

if __name__ == '__main__':
    print('Количество пропусков:', Passcard.objects.count())  
    passcard = Passcard.objects.all()
    print(passcard[0].created_at)
    print(passcard[0].is_active)
    print(passcard[0].owner_name)
    print(passcard[0].passcode)

    published_posts = passcard.filter(is_active=True)
    print('Количество активных пропусков:', len(published_posts))