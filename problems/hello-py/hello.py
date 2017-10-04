#!/usr/bin/env python3

import sys

args=sys.argv

if len(args) < 2:
	print('Usage:', args[0], 'NAME')
	sys.exit(1)
elif len(args) == 2:
        print('Hello to the {} of you: {}!'.format(len(args)-1, args[1]))
elif len(args) == 3:
	print('Hello to the {} of you: {} and {}!'.format(len(args)-1, args[1], args[2]))
elif len(args) > 3:
	print('Hello to the {} of you: {}, and {}!'.format(len(args)-1,', '.join(args[1:-1]), args[-1]))
else:
	sys.exit(1)

