#!/usr/bin/env python3

import sqlite3

class UseDB:

    def __init__(self,db:str='TestVop.db') -> None:
        self.path = db

    def __enter__(self) -> 'cursor':
        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        return self.curs

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.curs.close()
        self.conn.close()
