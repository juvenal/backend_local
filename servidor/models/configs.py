from . import Base
from sqlalchemy import Column, Integer, String, Boolean, Text

class Configuration(Base):
    __tablename__ = 'configs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(100), nullable=False, unique=True)
    value = Column(Text, nullable=False)
    enabled = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Configuration(key='{self.key}', value='{self.value}', enabled={self.enabled})>"
