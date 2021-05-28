import fontforge
import glob
import os
import json

SVG_DICT = 'compiled-icons/'
FIRST_GLYPH = 69420

def main():
    config = {}
    font = fontforge.font()

    svgs = sorted([ (fname, os.path.split(fname)[-1]) for fname in glob.glob(f'{SVG_DICT}*.svg') ], key=lambda name: '-'.join(name[1].split('-')[:-1]))
    for i, svg in enumerate(svgs):
        path = svg[0]
        name = svg[1].split('.')[0]
        glyph = font.createChar(FIRST_GLYPH+i, name)
        glyph.importOutlines(path)
        glyph.transform([1.00,0.00,0.00,1.00,-500,0])
        config[name] = FIRST_GLYPH+i

    font.familyname = 'Flowing-Icons'
    font.fullname = 'Flowing-Icons'
    font.fontname = 'Flowing-Icons'
    font.generate('Flowing-Icons.ttf')
    
    with open('Flowing-Icons.json', 'w') as f:
        json.dump(config, f)


if __name__ == '__main__' :
    main()
