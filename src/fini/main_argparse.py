import argparse


def app():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print(args)
