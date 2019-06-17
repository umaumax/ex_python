#!/usr/bin/env python3
import glob
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pattern', default='*', help="e.g. '../**/*.py'")
    args, extra_args = parser.parse_known_args()
    files = glob.glob(args.pattern)
    if files:
        print(files)
    else:
        print("Not Found")


if __name__ == '__main__':
    main()
