import glob
import shutil

RAWICONS_DICT = 'raw-icons/'
COMPILED_DICT = 'compiled-icons/'
def kebab_case(sentence):
    return '-'.join([ w.lower() for w in sentence.split(' ') ])


def icon_props(pathname):
    splitted = pathname.split('=')
    return {'name': kebab_case(splitted[1].split(',')[0]), 'style': kebab_case(splitted[-1].split('.')[0])}


def main():
    svgs = [ (fname, icon_props(fname)) for fname in glob.glob(f'{RAWICONS_DICT}*.svg') ]
    for svg in svgs:
        path = svg[0]
        name = svg[1]['name']
        style = svg[1]['style']
        shutil.copy(path, f'{COMPILED_DICT}{name}-{style}.svg')

if __name__ == '__main__' :
    main()