from django.contrib.auth.models import User
from django.db.models import ImageField


class UserExtend(User):
    photo = ImageField(upload_to='static/images/user/', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
