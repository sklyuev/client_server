from random import randint, getrandbits, random
from uuid import uuid4, uuid1

import Data_pb2

RAN_MIN = 1
RAN_MAX = 10

STORE = 'store'
RETRIEVE = 'retrieve'


def generate_car_info(message):
    message.car.ownerName = str(uuid4())
    message.car.serialNumber = uuid4().int>>64
    message.car.modelYear = uuid4().int>>64
    message.car.code = str(uuid4())
    message.car.vehicleCode = str(uuid4())

    # Engine
    message.car.engine.capacity = getrandbits(16)    # TODO: replace with uuid or numpy
    message.car.engine.numCylinders = getrandbits(8)
    message.car.engine.maxRpm = getrandbits(16)
    message.car.engine.manufacturerCode = str(uuid4())

    # FuelFigures
    message.car.fuelFigures.speed = getrandbits(16)
    message.car.fuelFigures.mpg = random()
    message.car.fuelFigures.usageDescription = str(uuid4())

    # PerformanceFigures
    message.car.performanceFigures.octaneRating = getrandbits(16)
    # Acceleration
    message.car.performanceFigures.acceleration.mph = getrandbits(16)
    message.car.performanceFigures.acceleration.seconds = random()

    message.car.manufacturer = str(uuid4())
    message.car.model = str(uuid4())
    message.car.activationalCode = str(uuid4())


def generate_message(action, serial_number=None):
    message = Data_pb2.Data()
    message.action = action
    if action == STORE:
        generate_car_info(message)
    elif action == RETRIEVE:
        message.car.serialNumber = serial_number
    else:
        print "Unknown {}".format(action)

    return message.SerializeToString()


if __name__ == "__main__":
    message = generate_message(STORE)
    print message
    proto_class = Data_pb2.Data()
    data = proto_class.ParseFromString(message)
    print proto_class






