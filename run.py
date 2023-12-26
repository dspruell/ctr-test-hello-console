#!/usr/bin/env python3

import logging
from time import sleep

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s"
)


def main():
    while True:
        message = "Hello, World!"
        logging.info("emitting message on standard output...")
        print(message)
        sleep(60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
