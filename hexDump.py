#!/usr/bin/env python3
"""
    PROGRAM :   Python Based HEX Dump Utility
    AUTHOR  :   lc

    VERSION HISTORY :

        2017-08-11      lc      Created from scratch

    INTRODUCTION :
        Takes a file and does a HEX/ASCII dump on it
"""
import sys
from optparse import OptionParser
"""
    useful constants
"""
version = '0.0.1'

TAB_STR   = '\t'
SPACE_STR = '    '

EXIT_OK = 0
EXIT_IO_ERROR = 10

BLOCK = 4

def hexDump( fh, output_width ) :
    """hexDump takes in a file stream and outputs an ASCII and hex
        dump. The output is in the format:

        <Hex Address> : <Hex values>... | <ASCII values>

    The output is variable in width based on the 'output_width' value.
    In the programs outter code this is 8, 16, 32 or 64 bytes but the
    function can, in theory, handle any width.
    """

    p = 0
    q = 0
    hex = ''
    ascii = ''

    for buf in fh.read() :

        c = buf

        hex = hex + ' {0:02X}'.format(c)
        if c >= 32 and c < 128 :
            ascii = ascii + '{0:s}'.format(chr(c))
        else :
            ascii = ascii + '.'
        p = p + 1
        q = q + 1

        if (p % BLOCK ) == 0 :
            hex = hex + ' :'
        if (p % output_width) == 0 :
            print( '{0:06x} :{1} {2}'.format( p-q, hex, ascii ) )
            q = 0
            hex = ''
            ascii = ''

    hex = hex + ' ' * (4*output_width)
    hex = hex[0:int((3*output_width)+(2*(output_width/BLOCK)))]

    print( '{0:06x} :{1} {2}'.format( p-q, hex, ascii ) )


if __name__ == '__main__' :
    parse = OptionParser( 'usage: -f <file>', version='%prog version ID: {0}'.format( version ) )
    parse.add_option( '-f', '--file',       dest='file',    default=None,  type='string',                   help='File to be dumped' )
    parse.add_option( '-n', '--narrow',     dest='narrow',  default=False,  action='store_true',    help='Narrow format (8-byte wide)' )
    parse.add_option( '-m', '--medium',     dest='medium',  default=True,   action='store_true',    help='Normal format (16-byte wide)' )
    parse.add_option( '-w', '--wide',       dest='wide',    default=False,  action='store_true',    help='Wide format (32-byte wide)' )
    parse.add_option( '-u', '--ultra',      dest='ultra',   default=False,  action='store_true',    help='Ultra-wide format (64-byte wide)' )

    ( opt, agrs ) = parse.parse_args()

    width = 16
    if opt.file is None  :
        parse.error( 'Invalid file name: "-f" option is required' )
    if opt.narrow :
        width = 8
    if opt.wide :
        width = 32
    if opt.ultra :
        width = 64

    try :
        print('Reading {0}...'.format(opt.file))
        fh = open(opt.file, 'rb')
        hexDump(fh, width)
        fh.close()

    except Exception as e :
        print( 'IO Error occured when reading {0}: {1}'.format( opt.file, e ) )
        sys.exit( EXIT_IO_ERROR )

    sys.exit( EXIT_OK )
