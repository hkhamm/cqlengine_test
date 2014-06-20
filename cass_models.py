from cqlengine import columns
from cqlengine import models
import uuid
from datetime import datetime


class Event(models.Model):
    """
    Analytic Event
    """
    __keyspace__ = 'ans'
    __table_name__ = 'events'

    # unique identifier for this event
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    # collected using this api_key
    api_key = columns.Text(required=False)
    # real app id
    app_id = columns.Text(required=False)
    # Name of collection
    collection = columns.Text(required=False)

    # Event details
    # Event timestamp, for items, this is when the item was completed
    event_timestamp = columns.DateTime(default=datetime.utcnow())
    # unique device code
    device_code = columns.UUID(required=False)
    # (choices: -1 unknown, 0 no, 1 yes, )
    at_school = columns.Text(required=False, default=-1)