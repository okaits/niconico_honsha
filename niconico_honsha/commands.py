#!/usr/bin/env python3

import niconico_honsha
import argparse

def show() -> None:
    niconico_honsha.tools.show()

def remove_file() -> None:
    parser = argparse.ArgumentParser(description="Remove file")
    parser.add_argument('filename', help="destination file/directory name")
    args = parser.parse_args()
    niconico_honsha.tools.remove_file(args.filename)