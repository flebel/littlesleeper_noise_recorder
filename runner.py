#!/usr/bin/env python

import argparse
import requests
import sys
import time

from recorder import DEBUG, session
from recorder.models import NoiseEvent, NoiseSource
from recorder.utils import get_or_create


parser = argparse.ArgumentParser(description='Watches over a LittleSleeper instance and records the noise level every `frequency` seconds.')
parser.add_argument('url', help="URL at which LittleSleeper's JSON API can be found.", type=str)
parser.add_argument('frequency', help='frequency in seconds (supports decimals) at which LittleSleeper is queried.', type=float)
parser.add_argument('source_name', help='name of the sensor/LittleSleeper instance from which the noise level is recorded.', type=str)

def run(url, frequency, source_name):
    sleep = lambda: time.sleep(frequency)
    while True:
        try:
            data = requests.get(url).json()
            current_value = data['audio_plot'][-1]
        except:
            sleep()
            continue
        event = NoiseEvent()
        event.intensity = current_value
        event.source_id = get_or_create(session, NoiseSource, name=source_name)[0].id
        session.add(event)
        session.commit()
        if DEBUG:
            sys.stdout.write(unicode(event))
            sys.stdout.write('\n')
            sys.stdout.flush()
        sleep()

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        run(args.url, args.frequency, args.source_name)
    finally:
        session.close()

