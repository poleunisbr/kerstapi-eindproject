# fillDb.py

from sqlalchemy.orm import Session
from database import create_database, SessionLocal
from models import Kerstmarkt, Kerstgerecht, Kerstdecoratie, User

# Initialize the database tables
create_database()

# Create a session
db = SessionLocal()

# Insert sample data
sample_markt_1 = Kerstmarkt(naam="Kerstmarkt 1", locatie="Locatie 1", datum="2023-12-25")
sample_markt_2 = Kerstmarkt(naam="Kerstmarkt 2", locatie="Locatie 2", datum="2023-12-20")

sample_gerecht_1 = Kerstgerecht(naam="Kerstgerecht 1", beschrijving="Beschrijving 1", prijs=15.99)
sample_gerecht_2 = Kerstgerecht(naam="Kerstgerecht 2", beschrijving="Beschrijving 2", prijs=12.50)

sample_decoratie_1 = Kerstdecoratie(naam="Kerstdecoratie 1", type="Type 1", prijs=9.99)
sample_decoratie_2 = Kerstdecoratie(naam="Kerstdecoratie 2", type="Type 2", prijs=14.75)

# Add data to the session
db.add(sample_markt_1)
db.add(sample_markt_2)
db.add(sample_gerecht_1)
db.add(sample_gerecht_2)
db.add(sample_decoratie_1)
db.add(sample_decoratie_2)


# Commit the changes
db.commit()

# Close the session
db.close()
