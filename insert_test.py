import uuid

from cqlengine import connection
from cqlengine.management import sync_table

from cass_models import Event


connection.setup(['54.200.175.168:9160'])
sync_table(Event)

event1 = Event.create(api_key='apikey-ajksdlf',
                      app_id='app_id-jsdkfl',
                      collection='test',
                      device_code=uuid.uuid4(),
                      at_school='1')

print(dict(event1))  # how is this different from django serializing?

event1['collection'] = 'TEST'

print(event1['collection'])