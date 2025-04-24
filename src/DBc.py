#!/usr/bin/env python3

import sqlite3


class UseDB:

    def __init__(self, dataBase: str = 'TestVop.db') -> None:
        self.pathOfBase = dataBase

    def __enter__(self) -> 'cursor':
        self.connectedBase = sqlite3.connect(self.pathOfBase)
        self.cursorInConnectedBase = self.connectedBase.cursor()
        return self.cursorInConnectedBase

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.connectedBase.commit()
        self.cursorInConnectedBase.close()
        self.connectedBase.close()
