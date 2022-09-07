"""Utilities for accessing the testing database"""

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine  # type: ignore

Base = declarative_base()

engine = create_engine(url="sqlite://")
make_session = sessionmaker(engine)
