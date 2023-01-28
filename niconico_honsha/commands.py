#!/usr/bin/env python3

import niconico_honsha
import argparse
import time

def show() -> None:
    parser = argparse.ArgumentParser(description="Explode Honsha")
    parser.add_argument('--loop', action='store_true', default=False, help="Explode Honsha forever")
    parser.add_argument('--speed', help="Speed to generate Honsha", default="0.01")
    args = parser.parse_args()
    if args.loop is True:
        while True:
            niconico_honsha.tools.show(float(args.speed))
            time.sleep(1)
    else:
        niconico_honsha.tools.show()

def remove_file() -> None:
    parser = argparse.ArgumentParser(description="Remove file")
    parser.add_argument('filename', help="destination file/directory name")
    args = parser.parse_args()
    niconico_honsha.tools.remove_file(args.filename)