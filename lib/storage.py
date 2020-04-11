import rocksdb


class Storage(object):
    def __init__(self, path):
        self.__handler = rocksdb.DB(
            path,
            rocksdb.Options(create_if_missing=True)
        )

    def put(self, key, value):
        written = self.__handler.put(
            key.encode(),
            value.encode()
        )
        return written

    def get(self, key):
        data = self.__handler.get(key.encode())

        return data.decode() if data else None
