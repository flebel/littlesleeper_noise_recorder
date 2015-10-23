from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import DateTime, Float, Integer, String

Base = declarative_base()


class NoiseSource(Base):
    __tablename__ = 'noise_source'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class NoiseEvent(Base):
    __tablename__ = 'noise_event'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, index=True, nullable=False, unique=True)
    intensity = Column(Float, nullable=False)
    source_id = Column(Integer, ForeignKey('noise_source.id'), nullable=False)
    source = relationship('NoiseSource', backref='events')

    __mapper_args__ = {
        'version_id_col': timestamp,
        'version_id_generator': lambda _: datetime.now(),
    }

    def __repr__(self):
        return '%s: %f @ %s' % (self.source.name, self.intensity, self.timestamp.strftime('%y-%m-%d %H:%M:%S.%f'),)

