from pydantic import BaseModel


class CardSchema(BaseModel):
    name: str
    id: int
    salePriceU: int
    sale: int
    supplierRating: float
    wh: int
