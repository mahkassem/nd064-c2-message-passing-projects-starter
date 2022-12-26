import os

from app import create_app
from app.udaconnect.location_consumer import LocationConsumer

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    location_consumer = LocationConsumer(app)
    app.run(debug=True, host="0.0.0.0")
