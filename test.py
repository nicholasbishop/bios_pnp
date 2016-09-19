#! /usr/bin/env python

# pylint: disable=missing-docstring

from StringIO import StringIO
from unittest import TestCase, main

from bios_pnp import pnp


class TestSplitN(TestCase):
    def test_too_small(self):
        with self.assertRaises(ValueError):
            pnp.split_n('abc', 4)

    def test_valid(self):
        self.assertEqual(pnp.split_n('abc', 2), ('ab', 'c'))


class TestPnpDevice(TestCase):
    def test_vendor_case(self):
        self.assertEqual(pnp.DeviceId('ifx', 0, 0).vendor, 'IFX')


class TestParse(TestCase):
    def test_parse_hex(self):
        self.assertEqual(pnp.parse_hex('10'), 16)

    def test_invalid_device_id(self):
        with self.assertRaises(ValueError):
            pnp.parse_device_id('ifx000')

    def test_valid_device_id(self):
        self.assertEqual(pnp.parse_device_id('IFX0101'),
                         pnp.DeviceId('ifx', 16, 1))

    def test_parse_id_file(self):
        id_file = StringIO('INT3f0d\nPNP0c02\n')
        self.assertEqual(pnp.parse_sysfs_pnp_id_file(id_file),
                         pnp.Device(ids=[pnp.DeviceId('INT', 0x3f0, 0xd),
                                         pnp.DeviceId('PNP', 0x0c0, 0x2)]))


if __name__ == '__main__':
    main()
