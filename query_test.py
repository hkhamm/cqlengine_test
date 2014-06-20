from cqlengine import connection

from cass_models import Event


connection.setup(['54.200.175.168:9160'])
all_objects = Event.objects.all()

for event in all_objects:
    print(dict(event))