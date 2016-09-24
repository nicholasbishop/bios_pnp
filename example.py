#! /usr/bin/env python

# pylint: disable=missing-docstring

from __future__ import print_function
from bios_pnp import pnp


def main():
    print('PNP devices on this system:')
    for device in pnp.get_all_pnp_devices_from_sysfs():
        print(device)


if __name__ == '__main__':
    main()
