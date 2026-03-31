import sys
from matplotlib import font_manager

if __name__ == '__main__':
    print(sys.path)
    for font in font_manager.fontManager.ttflist:
        print(font.name, '-', font.fname)
