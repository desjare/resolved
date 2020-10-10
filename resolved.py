#!/usr/bin/python3

# This was took from
# https://alecaddd.com/davinci-resolve-ffmpeg-cheatsheet-for-linux/
# 

import argparse
import os
import sys

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

def run_command(cmd):
    status = os.system(cmd)
    if(status != 0):
        print("Command %s return status %d" % (cmd, status))
        sys.exit(1)


def transcode_for_resolve(input_file, output_dir):

    _, ext = os.path.splitext(input_file)
    output_file = os.path.join(output_dir, os.path.basename(input_file.replace(ext,".mov")))

    if os.path.exists(output_file):
        print("Skipping existing %s" % (output_file))
        sys.exit(1)

    cmd = "ffmpeg -i \"%s\" -vcodec dnxhd -acodec pcm_s16le -s 1920x1080 -r 30000/1001 -b:v 36M -pix_fmt yuv422p -f mov \"%s\"" % (input_file, output_file)
    print("Executing: %s" % (cmd))

    run_command(cmd)

parser = argparse.ArgumentParser(description="resolved.py convert media film so that they can be imported by DaVinci Resolve easily (Registered Trademark of Blackmagic Design Pty Ltd)")
parser.add_argument("--input", type=str, default=None, dest="input", help="input file", required=True)
parser.add_argument("--outputdir", type=str, default=None, dest="output_dir", help="output dir", required=True)
args = parser.parse_args()


transcode_for_resolve(args.input, args.output_dir)
