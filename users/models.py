from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models import Max
# Create your models here.

class ActivityUsers(AbstractUser):
    id = models.CharField(primary_key=True, editable=False, max_length=10)
    real_name = models.CharField(max_length=30)
    tz=models.CharField(max_length=50)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['real_name']

    def save(self, **kwargs):
        if not self.id:
            max = ActivityUsers.objects.aggregate(id_max=Max('id'))['id_max']
            if max is None:
                max = 1
            else:
                max = int(max[1:]) + 1
            self.id = "{}{:05d}".format('A', max)
            print(self.id)
        super().save(*kwargs)

class ActivityPeriods(models.Model):
    user = models.ForeignKey(ActivityUsers, related_name='activity_user', on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=None, null=True)
    end_time = models.DateTimeField(default=None, null=True)