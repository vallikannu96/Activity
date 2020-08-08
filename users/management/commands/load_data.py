from django.core.management.base import BaseCommand
from users.models import ActivityUsers, ActivityPeriods
from datetime import datetime
import json
import os
from activity.settings import BASE_DIR
class Command(BaseCommand):
    help = 'Activity: Load dummy data from json file'

    def handle(self, *args, **options):
        print(self.help)
        path = os.path.join(BASE_DIR, 'static', "dummy.json")
        members = list()
        with open(path) as f:
            data = json.loads(f.read())
            members = data['members']
        # print(len(members))
        for member in members:
            print(member)
            user = ActivityUsers()
            user.username = member['real_name']
            user.real_name = member['real_name']
            user.set_password(raw_password=member['password'])
            user.tz = member['tz']
            user.save()
            for period in member['activity_periods']:
                start_time = datetime.strptime(period['start_time'], '%b %d %Y %I:%M%p')
                end_time = datetime.strptime(period['end_time'], '%b %d %Y %I:%M%p')
                activity = ActivityPeriods()
                activity.start_time = start_time
                activity.user = user
                activity.end_time = end_time
                activity.save()


