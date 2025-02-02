from django.apps import Appdecouple_config


class Usersdecouple_config(Appdecouple_config):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
