# music-tag-rearranger

Prints artist/album/track information about a song/directory, or can re-arrange your music into a artist>album>track folder structure

## Build

    pip install -r requirements.txt

## Run

### Print information about a song

    python print-tags.py ./my/audio/file.ogg

### Print information about all songs in a directory

    python print-tags.py ./my/audio/directory/

### Copy tracks into an artist>album>track hierarchy

    python print-tags.py --copy-to-directory=./destination/directory ./source/directory

this won't overwrite existing files by default (you can use the `--overwrite` flag here to overwrite existing files)

### More Options

    python print-tags.py -h