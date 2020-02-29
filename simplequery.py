from nhs import Session
from nhs.models import Location

sesh = Session()
locations = sesh.query(Location).first()
print(locations.gp_fulladdress)
sesh.close()