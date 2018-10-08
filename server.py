import Data_pb2

from twisted.protocols import basic
from twisted.internet import reactor, protocol

# from twisted.python import log

from data import STORE, RETRIEVE
from db import dbpool, SQL_CREATE_CAR_TABLE, get_car_info_by_serial_number, insert_car_info

# log.startLogging(sys.stdout)


class CarCenter(basic.LineReceiver):

    def dataReceived(self, data):
        proto_class = Data_pb2.Data()
        proto_class.ParseFromString(data)
        print proto_class
        action = proto_class.action
        # log.msg("Server action: {}".format(action))
        if action == STORE:              # save to DB
            car_data = proto_class.car
            # log.msg("Store: {}".format(car_data))
            insert_car_info(car_data)
        if action == RETRIEVE:
            serial_number = str(proto_class.car.serialNumber)
            print "get data from DB, serial_number={}".format(serial_number)

            d = get_car_info_by_serial_number(serial_number)
            # TODO: if no data were found need to send correctly notify client
            d.addCallback(self.send_results)

    def send_results(self, results):
        # TODO: use protobuf structure to send it back to server
        s = ''
        for elt in results:
            s += str(elt)
        self.transport.write(s)


def main():
    dbpool.runQuery(SQL_CREATE_CAR_TABLE)

    factory = protocol.ServerFactory()
    factory.protocol = CarCenter
    reactor.listenTCP(8000, factory)
    reactor.run()


if __name__ == '__main__':
    main()