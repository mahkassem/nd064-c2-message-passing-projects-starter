import os

from app import create_app
from app.udaconnect.person_grpc import PersonGRPCServer

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    grpc_server = PersonGRPCServer(app)
    app.run(debug=True, host="0.0.0.0")
