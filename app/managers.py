import sqlite3

from app.models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name)"
            "VALUES (?, ?)", (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list:
        actors_data = self._connection.execute(
            F"SELECT * FROM {self.table_name}"
        )
        return [Actor(*row) for row in actors_data]

    def update(
        self,
        id_to_update: int,
        new_name: str,
        new_last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (new_name, new_last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ?", (id_to_delete,)
        )
        self._connection.commit()