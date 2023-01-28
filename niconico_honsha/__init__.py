#!/usr/bin/env python3

from __future__ import annotations
import time
import os
import shutil

class honsha():
    class asciiarts():
        def __init__(self) -> None:
            with open(f"{os.path.dirname(os.path.abspath(__file__))}/honsha_aa/honsha.txt", encoding="UTF-8") as honsha:
                self.honsha = honsha.read()
            with open(f"{os.path.dirname(os.path.abspath(__file__))}/honsha_aa/explode.txt", encoding="UTF-8") as explode:
                self.explode = explode.read()
    def show_honsha(aa: honsha.asciiarts) -> None: #pylint: disable=E0213 C0103
        print("\x1B[H\x1B[2J\x1B[3J") #強引にclearコマンドの実行結果をコピペしたもの(制御文字)を出力する。catコマンドが誤作動してしまう可能性あり
        print(aa.honsha)
    def explode(aa: honsha.asciiarts) -> None: #pylint: disable=E0213 C0103
        print("\x1B[H\x1B[2J\x1B[3J")
        print(aa.explode)
    def show(aa: honsha.asciiarts) -> None: #pylint: disable=E0213 C0103
        honsha.show_honsha(aa)
        time.sleep(1)
        honsha.explode(aa)

class tools():
    def show() -> None: #pylint: disable=E0213 E0211
        honsha.show(honsha.asciiarts())
    def remove_file(filename: str) -> None: #pylint: disable=E0213
        aa = honsha.asciiarts()
        honsha.show_honsha(aa)
        shutil.rmtree(filename)
        honsha.explode(aa)

if __name__ == "__main__":
    tools.show()