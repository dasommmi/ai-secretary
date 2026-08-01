from dataclasses import dataclass
from datetime import datetime


@dataclass
class ContentSession:

    user_id: str
    content_type: str
    status: str = "WAITING_INPUT"
    created_at: datetime = datetime.now()
