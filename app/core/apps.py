from django.apps import AppConfig


# core app is holding common things used in all sub apps,
# such as migrations, database, admin, models
class CoreConfig(AppConfig):
    name = 'core'
