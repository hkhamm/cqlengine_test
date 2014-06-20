from cass_models import Event
from cqlengine import connection

connection.setup(['54.200.175.168:9160'])
all_objects = Event.objects.all()

print(all_objects[0].id)