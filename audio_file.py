__author__ = 'james'


import mutagen
from mutagen.id3 import ID3
from mutagen.mp4 import MP4


class AudioFile:

    file_path = None
    artist = None
    album = None
    track_name = None

    def __init__(self, file_path):
        self.file_path = file_path
        try:
            audio_file = ID3(file_path)
            if 'TPE1' in audio_file:
                self.artist = audio_file['TPE1'].text[0]
            if 'TIT2' in audio_file:
                self.track_name = audio_file['TIT2'].text[0]
            if 'TALB' in audio_file:
                self.album = audio_file['TALB'].text[0]

        except mutagen.id3.ID3NoHeaderError, e:
            audio_file = MP4(file_path)
            if '\xa9ART' in audio_file:
                self.artist = audio_file['\xa9ART'][0]
            if '\xa9nam' in audio_file:
                self.track_name = audio_file['\xa9nam'][0]
            if '\xa9alb' in audio_file:
                self.album = audio_file['\xa9alb'][0]
