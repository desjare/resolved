# resolved.py

resolved.py convert media film so that they can be imported by DaVinci Resolve easily on Linux.

The cheat cheat I used to write the script:

https://alecaddd.com/davinci-resolve-ffmpeg-cheatsheet-for-linux/

Your input file will be converted to a 1920x1080 [DNxHD](https://en.wikipedia.org/wiki/Avid_DNxHD) mov file.

**Usage:**

python3 resolved.py --input **path** --outputdir **dir**

**Requirements**
* [python3](https://www.python.org/) (tested with python 3.6.9)
* [ffmpeg](https://ffmpeg.org/) in your path

**Trademarks**

DaVinci Resolve is a Registered Trademark of Blackmagic Design Pty Ltd.
