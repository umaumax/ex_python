#!/usr/bin/env python3

import unittest

import contextlib
import io


class TestContextlib(unittest.TestCase):
    def test_contextlib_redirect_stdout(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            print('stdout-output')
        self.assertEqual(buf.getvalue(), 'stdout-output\n')


def main():
    pass


if __name__ == '__main__':
    main()
