from dataclasses import dataclass, fields
from datetime import datetime
from typing import Optional
from uuid import UUID

from asyncpg.pgproto.pgproto import UUID as pgUUID
from pydantic import BaseModel


class DataModel(BaseModel):
    class Config:
        json_encoders = {datetime: lambda v: v.isoformat().replace("+00:00", "Z")}


@dataclass
class BaseDataclass:
    id: UUID

    @classmethod
    def from_row(cls, row: dict, alias: str = ""):
        def get_value(value):
            if isinstance(value, pgUUID):
                return UUID(str(value))
            if isinstance(value, list):
                return [get_value(v) for v in value]
            return value

        cls_dict = dict()
        for field in fields(cls):
            name = field.name
            try:
                raw_value = row[f"{alias}{name}"]
            except KeyError:
                continue
            cls_dict[name] = get_value(raw_value)
        return cls(**cls_dict)


class BaseFilter(BaseModel):
    page: Optional[int]
    per_page: int

    @property
    def offset(self) -> int:
        return self.page * self.per_page if self.page else 0

    @property
    def limit(self) -> Optional[int]:
        return self.per_page if self.page is not None else None
