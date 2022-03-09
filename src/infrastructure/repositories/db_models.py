import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB, UUID

metadata = sa.MetaData()

locks = sa.Table(
    "locks",
    metadata,
    sa.Column("data", JSONB, nullable=False),
)

