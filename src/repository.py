from sqlalchemy import insert, create_engine
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
