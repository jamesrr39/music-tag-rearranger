#!/usr/bin/python

from audio_file import AudioFile
import argparse
import os


parser = argparse.ArgumentParser(description='Audio file information printer.')
parser.add_argument('filepath', metavar='filepath', type=str, help='prints audio information from file')
args = parser.parse_args()

if os.path.isfile(args.filepath):
    audio_file = AudioFile(args.filepath)
    print "File path: %s" % audio_file.file_path
    print "Artist: %s" % audio_file.artist
    print "Album: %s" % audio_file.album
    print "Track name: %s" % audio_file.track_name

elif os.path.isdir(args.filepath):
    for root, dirs, files in os.walk(args.filepath):
        for file_name in files:
            audio_file = AudioFile(os.path.join(root, file_name))
            print "File path: %s" % audio_file.file_path
            print "Artist: %s" % audio_file.artist
            print "Album: %s" % audio_file.album
            print "Track name: %s" % audio_file.track_name
            print ""


else:
    raise IOError("No file or directory at %s" % args.filepath)