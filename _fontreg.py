from matplotlib import font_manager as fm
import glob
for f in glob.glob('/usr/share/fonts/opentype/urw-base35/NimbusSans-*.otf'):
    fm.fontManager.addfont(f)
