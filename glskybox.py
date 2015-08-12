#!/usr/bin/env python

# author: ChiChou <chichou@ujs.edu.cn>

import argparse

from render import Projector


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert skydome texture to skybox')
    parser.add_argument('input', metavar='FILE', nargs='+', help='source file name')
    parser.add_argument('-o', '--output', dest='output', default='output', help='destination path')
    parser.add_argument('-s', '--size', dest='size', type=int, default=1024, help='output image size')
    parser.add_argument('-f', '--overwrite', dest='overwrite', action='store_true', default=False,
        help='overwrite existing output')

    args = parser.parse_args()
    projector = Projector(args.size, args.output, True, args.overwrite)
    (projector.run(source) for source in args.input)