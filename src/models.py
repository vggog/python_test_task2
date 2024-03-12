from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )


class QueryHistoryModel(BaseModel):
    __tablename__ = "query_history"

    user_id: Mapped[int] = mapped_column(BigInteger)
    vendor_code: Mapped[int] = mapped_column(BigInteger)
