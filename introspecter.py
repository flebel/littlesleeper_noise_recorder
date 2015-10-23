#!/usr/bin/env python

import argparse
import sys
import time

from recorder import session
from recorder.models import NoiseEvent


parser = argparse.ArgumentParser(description="Watches over a LittleSleeper noise recorder's database and prints the noise level every `frequency` seconds.")
parser.add_argument('frequency', help='frequency in seconds (supports decimals) at which the database is queried.', type=float)

def run(frequency):
    while True:
        event = session.query(NoiseEvent).order_by(NoiseEvent.id.desc()).first()
        if not event:
            time.sleep(frequency)
            continue
        sys.stdout.write(unicode(event))
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(frequency)

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        run(args.frequency)
    finally:
        session.close()

