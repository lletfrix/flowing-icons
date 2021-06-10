import fontforge
import glob
import os
import json

SVG_DICT = 'compiled-icons/'
FIRST_GLYPH = 57344

def main():
    config = {}
    font = fontforge.font()

    svgs = sorted([ (fname, os.path.split(fname)[-1]) for fname in glob.glob(f'{SVG_DICT}*.svg') ], key=lambda name: '-'.join(name[1].split('-')[:-1]))
    for i, svg in enumerate(svgs):
        path = svg[0]
        name = svg[1].split('.')[0]
        glyph = font.createChar(FIRST_GLYPH+i, name)
        glyph.importOutlines(path)
        # glyph.transform([1.00,0.00,0.00,1.00,-500,0])
        glyph.width=1000
        # glyph.vwidth=1000
        config[name] = FIRST_GLYPH+i

    font.familyname = 'Flowing-Icons'
    font.fullname = 'Flowing-Icons'
    font.fontname = 'Flowing-Icons'
    font.correctDirection()
    font.generate('Flowing-Icons.ttf')
    
    with open('Flowing-Icons.json', 'w') as f:
        json.dump(config, f)

    with open('Flowing-Icons.css', 'w') as f:
        f.write('@font-face{\n')
        f.write('\tfont-family: \'Flowing-Icons\';\n')
        f.write('\tsrc: url(\'Flowing-Icons.ttf\') format(\'truetype\');\n')
        f.write('\tfont-weight: normal;\n')
        f.write('\tfont-style: normal;\n')
        f.write('}\n\n')

        f.write('.icon {\n')
        f.write('\tfont-family: \'Flowing-Icons\';\n')
        f.write('\tfont-weight: normal;\n')
        f.write('\tfont-style: normal;\n')
        f.write('\tfont-variant: normal;\n')
        f.write('\ttext-transform: none;\n')
        f.write('\tline-height: 1;\n')
        f.write('\t-webkit-for-smoothing: antialiased;\n')
        f.write('\tposition: relative;\n')
        f.write('}\n')

        for k in config:
            f.write("."+k+":before\t\t\t\t{ content:'\\"+hex(config[k])[2:]+"'; }\n")


if __name__ == '__main__' :
    main()
