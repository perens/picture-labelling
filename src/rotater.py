#!/usr/bin/python3

""" Rotater
Usage:
    rotater.py [-o <folder>] <input>
    rotater.py -h | --help

Options:
    -h --help           Request help
    -o <folder>         Specify output folder [default: out]

Arguments:
    <input>             Input folder with images

"""
# rotater.py -o /labelled/facade /labelled/facade
import schema
from docopt import docopt
from PIL import Image
import os


def main():
    ARGS = docopt(__doc__, version='Rotater 1.0')
    SCHEMA = schema.Schema({
        '--help': schema.Or(False),
        '-o': schema.Or(str),
        '<input>': schema.Or(None, str, error='Input missing'),
    })
    try:
        ARGS = SCHEMA.validate(ARGS)
    except schema.SchemaError as err:
        exit(err)

    # TODO _0, _90, _180, _270
    if not os.path.exists('out') and ARGS['-o'] == "out":
        os.makedirs('out')

    directory = ARGS['<input>']
    for entry in os.scandir(directory):
        if entry.path.endswith(".jpg") and entry.is_file():
            img = Image.open(entry.path)

            filename = img.filename.split('/')[-1]
            #filename_parts = filename.split('-')
            #f_name = ARGS['-o'] + "/{part0}-{degrees}deg-{part2}"
            img_title, img_extension = os.path.splitext(filename)
            
            # TODO erinevatesse folderitesse salvestada
            # 0 ka? hoiaks moditud andmed kõigest eraldi??
            
            degrees = [0, 90, 180, 270]
            for d in degrees:
                rotate_img = img.rotate(d)
                #rot_name = f_name.format(part0=filename_parts[0], degrees=d, part2=filename_parts[2])
                rot_name = img_title + "_" + str(d) + img_extension
                print(rot_name)
                rotate_img.save(rot_name)


if __name__ == "__main__":
    main()
