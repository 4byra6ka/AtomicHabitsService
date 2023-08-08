import json
from datetime import datetime, timedelta

from celery import shared_task

from users.models import User
from users.services import tg_get_updates, tg_send_message


@shared_task
def telegram_bot_updates():
    tg_data = tg_get_updates()
    users = User.objects.filter(is_active=False)
    if tg_data['ok'] and tg_data['result'] != []:
        for message in tg_data['result']:
            if message['message']['text'] == "/start":
                for user_one in users:
                    if user_one.username.lower() == message['message']['from']['username'].lower():
                        password = User.objects.make_random_password()
                        user_one.set_password(password)
                        user_one.tg_user_id = message['message']['from']['id']
                        user_one.first_name = message['message']['from']['first_name']
                        user_one.last_name = message['message']['from']['last_name']
                        user_one.is_active = True
                        user_one.save()
                        tg_get_updates(message['update_id'])
                        text = f'Ваша учетная запись активирована. Пароль для входа:\n{password}'
                        tg_send_message(message['message']['from']['id'], text)
                    # else:
                    #     tg_send_message(
                    #         message['message']['from']['id'],
                    #         'Вы уже активированы или не прошли регистрацию'
                    #         )
            tg_get_updates(message['update_id'])





from django_celery_beat.models import PeriodicTask, IntervalSchedule

# # Создаем интервал для повтора
# schedule, created = IntervalSchedule.objects.get_or_create(
#      every=60,
#      period=IntervalSchedule.SECONDS,
#  )
#
# # Создаем задачу для повторения
# PeriodicTask.objects.create(
#      interval=schedule,
#      name='TelegramBotUpdates',
#      task='users.tasks.telegram_bot_updates',
#      args=json.dumps({}),
#      kwargs=json.dumps({}),
#      expires=datetime.utcnow() + timedelta(seconds=30)
#  )



