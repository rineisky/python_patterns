class ConnectionMeta(type):
    _connections = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._connections:
            instance = super().__call__(*args, **kwargs)
            cls._connections[cls] = instance
        return cls._connections[cls]


class PostgresConnection(metaclass=ConnectionMeta):
    def exec_request(self):
        pass


if __name__ == "__main__":
    connect_1 = PostgresConnection()
    connect_2 = PostgresConnection()
    print(f'Используется одно соединение: {connect_1 is connect_2}')
