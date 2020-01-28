#Argparser practise program
#Takes few arguments and calculates the volume of a cube

import argparse

parser = argparse.ArgumentParser(description='Takes width, height and depth of a cube and calculates the volume.')
parser.add_argument('-w', '--width', type=int, required=True, metavar='', help='Width of the cube')
parser.add_argument('-H', '--height', type=int, required=True, metavar='', help='Height of the cube')
parser.add_argument('-d', '--depth', type=int, required=True, metavar='', help='Depth of the cube')
group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='print quiet = only answer')
group.add_argument('-v', '--verbose', action='store_true', help='print verbose = print more')
args = parser.parse_args()

def calculate_cube(width, height, depth):
    volume = width * height * depth
    return volume

if __name__ == '__main__':
    vol = calculate_cube(args.width, args.height, args.depth)
    if args.quiet:
        print(vol)
    elif args.verbose:
        print('The volume of the cube with width {}, height {} and depth {} is {}.'.format(args.width, args.height, args.depth, vol))
    else:
        print('The volume of the cube is: {}'.format(vol))
