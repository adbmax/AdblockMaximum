#!/usr/bin/env python3

import os
import json
import re
import sys

if len(sys.argv) == 1 or not sys.argv[1]:
    raise SystemExit('Build dir missing.')

proj_dir = os.path.join(os.path.split(os.path.abspath(__file__))[0], '..')
build_dir = os.path.abspath(sys.argv[1])

version = ''
key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApmN39/tzRLNJwEo/+MIOXTdGR8GkxOLrFEUFyiVIcsJXCHmNB1Akhl5vJsdZ6/Z0KPthayB3FXEutp+X0ShHz6dpRqLRbFk/1LzdiYxvIy71A7cyl2J+8Ed4iIuRSRUeublROypZbtjXuyib8I/Ouiz3Q5BEZ9/wamHGz7Rah6HfeJL4KYx4KZ2mVPxzPd2gPEhv3gGWXe6RqI0ZSiTTrmWGqt1+qNvvuGMeOKDMwtShKiT5O4tP5pzJiVWuuxpqsIf3tWqTOkrePMrYNdJwv/pP00AnawcX/Bj5pnZRz052VsWn1wLZ6xV+5axR1t+bgFfZ+iJQbmn2WmGHfiWiUQIDAQAB'

with open(os.path.join(proj_dir, 'dist', 'version')) as f:
    version = f.read().strip()

manifest_out = {}
manifest_out_file = os.path.join(build_dir, 'manifest.json')
with open(manifest_out_file) as f:
    manifest_out = json.load(f)

manifest_out['version'] = version
manifest_out['key'] = key

with open(manifest_out_file, 'w') as f:
    json.dump(manifest_out, f, indent=2, separators=(',', ': '), sort_keys=True)
    f.write('\n')
