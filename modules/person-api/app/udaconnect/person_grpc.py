# create class PersongRPCService: that will inherit from PersonService and it will have a Get method that will return a List of Person
import time
from typing import List
import logging
from concurrent import futures

from app.udaconnect.services import PersonService
from app.udaconnect.models import Person
from app.udaconnect import person_pb2
from app.udaconnect import person_pb2_grpc
import grpc

logger = logging.getLogger('person-grpc-server')


class PersonServicer(person_pb2_grpc.PersonServiceServicer):
    def __init__(self, app):
        self.app = app

    def GetAll(self, request, context):
        persons: List[Person] = PersonService.retrieve_grpc(self.app)
        result = person_pb2.PersonMessageList()
        for person in persons:
            person_message = person_pb2.PersonMessage(
                id=person.id,
                first_name=person.first_name,
                last_name=person.last_name,
                company_name=person.company_name
            )
            result.persons.extend([person_message])

        return result


# Initialize gRPC server
class PersonGRPCServer:
    def __init__(self, app):
        self.app = app
        self.server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=2))
        person_pb2_grpc.add_PersonServiceServicer_to_server(
            PersonServicer(self.app), self.server)

        print("gRPC Server starting on port 5005...")

        self.server.add_insecure_port("[::]:5005")
        self.server.start()
