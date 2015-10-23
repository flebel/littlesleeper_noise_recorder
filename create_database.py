#!/usr/bin/env python

from recorder import engine
from recorder.models import Base, NoiseEvent, NoiseSource


Base.metadata.create_all(engine)

