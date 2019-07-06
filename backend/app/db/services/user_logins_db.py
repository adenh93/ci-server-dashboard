from datetime import datetime
from ..tables import user_logins
from .. import db


async def insert_user_login(user_id: int):
    query = user_logins.insert().values(
        user_id=user_id,
        login_date=datetime.now()
    )
    return await db.execute(query)
