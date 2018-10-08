# Python 2.7.12
1. Start server
   >> python server.py

   # Server:
   # - accepts car data from client and save it to DB;
   # - by provided serial number it retrieve car data from DB and send it back to client.

2. Start client
   >> python client.py

   # Client recognizes two command:
   # "1" - generate message with random car data and send it to server;
   # "2" - retrive info about car by serial number, provied by user.
   #
   # Note: Right now client can perform one command.
   #       Need to start new client to perform another command.

# Note:
# Protobuf can be compiled with:
# >> protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/Data.proto
