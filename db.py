from twisted.enterprise import adbapi

dbpool = adbapi.ConnectionPool("sqlite3", "cars.db", check_same_thread=False)

# TODO: need to split on several tables or switch to NoSQL DB if requests to DB have the same pattern
# TODO: use correct type for feilds
SQL_CREATE_CAR_TABLE = """CREATE TABLE IF NOT EXISTS car (
                                    id integer PRIMARY KEY,
                                    owner_name text NOT NULL,
                                    serial_number text NOT NULL,
                                    model_year text NOT NULL,
                                    code text NOT NULL,
                                    vechicle_code text NOT NULL
                                );"""


SQL_INSERT_CAR_INFO = """INSERT INTO car(
                                        owner_name,
                                        serial_number,
                                        model_year,
                                        code,
                                        vechicle_code
                                        )
                          VALUES(?,?,?,?,?)"""

SQL_GET_CAR_INFO_BY_SERIAL_NUMBER = """SELECT * FROM car WHERE serial_number = ?"""


def get_car_info_by_serial_number(serial_number):
    rows = dbpool.runQuery(SQL_GET_CAR_INFO_BY_SERIAL_NUMBER,
                           (serial_number,))
    return rows

def insert_car_info(info):
    dbpool.runQuery(SQL_INSERT_CAR_INFO, (info.ownerName,
                                          str(info.serialNumber),
                                          str(info.modelYear),
                                          info.code,
                                          info.vehicleCode,
                                          )
                    )