from ninja import Schema
from decimal import Decimal

class CourseIn(Schema):
    title: str
    description: str
    price: Decimal
    duration: float
    rate: int
    category_id: int

class CourseOut(Schema):
    id: int
    title: str
    description: str
    price: Decimal
    duration: float
    rate: int