#!/usr/bin/env python3

from __future__ import annotations
import time
import os
import shutil

class honsha():
    class asciiarts():
        def __init__(self) -> None:
            with open(f"{os.path.dirname(os.path.abspath(__file__))}/honsha_aa/honsha.txt", encoding="UTF-8") as honshaaa:
                self.honsha = honshaaa.read()
            with open(f"{os.path.dirname(os.path.abspath(__file__))}/honsha_aa/explode.txt", encoding="UTF-8") as explode:
                self.explode = explode.read()
            with open(f"{os.path.dirname(os.path.abspath(__file__))}/honsha_aa/after-explode.txt", encoding="UTF-8") as exploded:
                self.exploded = exploded.read()
    def show_honsha(aa: honsha.asciiarts, speed: float = 0.01) -> None: #pylint: disable=E0213 C0103
        print("\x1B[H\x1B[2J\x1B[3J") #強引にclearの制御文字を出力し、OSに依存しないようにする
        for line in aa.honsha.split("\n"):
            time.sleep(speed)
            print(line)
    def explode(aa: honsha.asciiarts) -> None: #pylint: disable=E0213 C0103
        print("\x1B[H\x1B[2J\x1B[3J")
        print(aa.explode)
    def show_honsha_exploded(aa: honsha.asciiarts()) -> None: #pylint: disable=E0213 C0103
        print("\x1B[H\x1B[2J\x1B[3J")
        print(aa.exploded) #pylint: disable=E1101
    def show(aa: honsha.asciiarts, speed: float = 0.01) -> None: #pylint: disable=E0213 C0103
        honsha.show_honsha(aa, speed=speed)
        time.sleep(1)
        honsha.explode(aa)
        time.sleep(0.6)
        honsha.show_honsha_exploded(aa)

class tools():
    def show(speed: float = 0.01) -> None: #pylint: disable=E0213 E0211
        honsha.show(honsha.asciiarts(), speed=speed)
    def remove_file(filename: str) -> None: #pylint: disable=E0213
        aa = honsha.asciiarts()
        honsha.show_honsha(aa)
        shutil.rmtree(filename)
        honsha.explode(aa)
        time.sleep(0.3)
        honsha.show_honsha_exploded(aa)

if __name__ == "__main__":
    tools.show()