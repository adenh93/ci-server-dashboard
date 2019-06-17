import sqlalchemy

metadata = sqlalchemy.MetaData()

user = sqlalchemy.Table('user', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('username', sqlalchemy.String(100), nullable=False),
    sqlalchemy.Column('email', sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column('password_hash', sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column('created_date', sqlalchemy.DateTime, nullable=False)
)


user_login = sqlalchemy.Table('user_login', metadata,
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id")),
    sqlalchemy.Column('login_date', sqlalchemy.DateTime, nullable=False)
)


user_api_key = sqlalchemy.Table('user_api_key', metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.Integer, sqlalchemy.ForeignKey("user.id")),
    sqlalchemy.Column('service', sqlalchemy.String(40), nullable=False),
    sqlalchemy.Column('key', sqlalchemy.String(255), nullable=False)
)