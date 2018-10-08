import sys
from twisted.internet import reactor, protocol
# from twisted.python import log

from data import generate_message, STORE, RETRIEVE

# log.startLogging(sys.stdout)


class EchoClient(protocol.Protocol):

    def connectionMade(self):
        user_action = input('''Select user action:
                               - Type "1" to generate new format data and send it send it to server.
                               - Type "2" to request format data by ID
                               - Press ctrl-C to close connection.\n''')

        # log.msg('Action: {}'.format(user_action))
        if user_action == 1:
            data = generate_message(STORE)
        elif user_action == 2:
            sys.stdout.write('Enter serial number:')
            serial_number = input()
            # log.msg('Serial number: {}'.format(serial_number))
            data = generate_message(RETRIEVE, serial_number)
        else:
            pass
            # log.msg('Unknow action {}'.format(user_action))

        data = str(data)
        # log.msg('Client send: {}'.format(data))
        print('Client send: {}'.format(data))
        self.transport.write(data)
        # TODO: after data were send repeat user dialog

    def dataReceived(self, data):
        # log.msg("Server said: {}".format(data))
        print("Server said: {}".format(data))
        self.transport.loseConnection()

    def connectionLost(self, reason):
        # log.msg("Connection lost")
        self.transport.loseConnection()


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        reactor.stop()


def main():
    f = EchoFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()


if __name__ == '__main__':
    main()