#!/usr/bin/python

from audio_file import AudioFile
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Audio file information printer.')
parser.add_argument('filepath', metavar='filepath', type=str, help='prints audio information from file')
parser.add_argument('--overwrite', action="store_true", default=False, help='Overwrite existing files?')
parser.add_argument('--copy-to-directory', action="store", dest='copy_to_directory', default=None, help='If supplied, copies the files into an Artist>Album>Track name folder structure')
args = parser.parse_args()

def get_new_file_path(root_directory, artist, album, track):
    return os.path.join(root_directory, artist or "Unknown", album or "Unknown", track or "Untitled")

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


file_paths = []
if os.path.isfile(args.filepath):
    file_paths.append(args.filepath)
elif os.path.isdir(args.filepath):
    for root, dirs, files in os.walk(args.filepath):
        for file_name in files:
            file_paths.append(os.path.join(root, file_name))
else:
    raise IOError("No file or directory at %s" % args.filepath)


for file_path in file_paths:
    audio_file = AudioFile(file_path)
    print "File path: %s" % audio_file.file_path
    print "Artist: %s" % (audio_file.artist or "Unknown")
    print "Album: %s" % (audio_file.album or "Unknown")
    print "Track name: %s" % (audio_file.track_name or "Unknown")
    if args.copy_to_directory is not None:
        extension = "." + file_path.split(".")[-1]
        new_file_path = get_new_file_path(args.copy_to_directory, audio_file.artist, audio_file.album, audio_file.track_name or "Untitled" + extension)
        if args.overwrite is False and os.path.exists(new_file_path):
            print "%s already exists, will not overwrite" % (new_file_path)
        else:
            ensure_directory_exists(os.path.join(args.copy_to_directory, audio_file.artist or "Unknown", audio_file.album or "Unknown"))
            print "copying from %s to %s" % (file_path, new_file_path)
            shutil.copyfile(file_path, new_file_path)
    print ""
