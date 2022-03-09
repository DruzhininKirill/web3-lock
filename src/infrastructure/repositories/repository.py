from sqlalchemy import select

from .db_models import locks


class Repository:
    def __init__(self, db):
        self._db = db

    async def get_locks(self) -> bool:
        query = select([locks.c.data])
        async with self._db.connect() as conn:
            result = await conn.execute(query)
        if row := result.fetchone():
            return True
