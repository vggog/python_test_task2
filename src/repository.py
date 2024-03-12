from typing import Sequence

from sqlalchemy import insert, select, desc, create_engine
from sqlalchemy.orm import Session

from .models import QueryHistoryModel
from .config import db_config


class Repository:

    def __init__(
            self,
            engine=create_engine(db_config.alchemy_url)
    ):
        self.engine = engine

    def add_query_to_history(
            self,
            user_id: int,
            vendor_code: int,
    ):
        """Метод для добавления новой записи в историю просмотра артикула."""
        stmt = insert(QueryHistoryModel).values(
            user_id=user_id,
            vendor_code=vendor_code
        )

        with Session(self.engine) as session:
            session.execute(stmt)
            session.commit()

    def get_last_five_queries(self, user_id: int) -> Sequence[QueryHistoryModel]:
        """Метод для получения последних 5 созданных записей запросов"""
        stmt = (
            select(QueryHistoryModel)
            .where(QueryHistoryModel.user_id == user_id)
            .order_by(desc(QueryHistoryModel.created_at))
            .limit(5)
        )

        with Session(self.engine) as session:
            return session.execute(stmt).scalars().all()
