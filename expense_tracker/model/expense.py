from datetime import datetime
from dataclasses import dataclass
@dataclass
class Expense():
    amount: float
    date: datetime
    description: str = ""
