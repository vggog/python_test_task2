from typing import Sequence

from sqlalchemy import insert, select, desc, create_engine
from sqlalchemy.orm import Session

from .models import QueryHistoryModel, BaseModel, SubscriptionToNotificationsModel
from .config import db_config


class Repository:

    def __init__(
            self,
            engine=create_engine(db_config.alchemy_url)
    ):
        self.engine = engine

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

    def add_record(
            self,
            user_id: int,
            vendor_code: int,
            table: type[BaseModel],
    ):
        """
        Метод для добавления данных в таблицы subscription_to_notifications
        или query_history
        """
        stmt = insert(table).values(
            user_id=user_id,
            vendor_code=vendor_code
        )

        with Session(self.engine) as session:
            session.execute(stmt)
            session.commit()

    def is_subscribe_in_db(
            self,
            user_id: int,
            vendor_code: int,
    ) -> SubscriptionToNotificationsModel | None:
        """Метод для проверки наличия записи о подписание на уведомление"""
        stmt = (
            select(SubscriptionToNotificationsModel)
            .where(SubscriptionToNotificationsModel.user_id == user_id)
            .where(SubscriptionToNotificationsModel.vendor_code == vendor_code)
        )

        with Session(self.engine) as session:
            return session.execute(stmt).scalars().first()
