"""Register URW Nimbus Sans with matplotlib.

Nimbus Sans is metric-compatible with Helvetica and is the family the
manuscript's figures are set in. It ships with Ghostscript (Debian and
Ubuntu: the fonts-urw-base35 package) but is not always visible to
matplotlib's own font cache, so it is registered explicitly here.

If it cannot be found, the figures still draw, but in matplotlib's default
family and at slightly different text widths. A warning is printed so that
the substitution is never silent.
"""
import glob
import sys
from matplotlib import font_manager as fm

_PATTERNS = (
    '/usr/share/fonts/**/NimbusSans-*.otf',
    '/usr/local/share/fonts/**/NimbusSans-*.otf',
    '/opt/homebrew/share/fonts/**/NimbusSans-*.otf',
    '/Library/Fonts/NimbusSans-*.otf',
)

_found = []
for _pat in _PATTERNS:
    for _f in glob.glob(_pat, recursive=True):
        try:
            fm.fontManager.addfont(_f)
        except Exception:      # a file matplotlib's FreeType cannot read
            continue
        _found.append(_f)

if not _found:
    print(
        'WARNING: Nimbus Sans was not found, so the figures will be drawn in '
        'matplotlib\'s default family instead of the manuscript\'s.\n'
        '         Install it (Debian/Ubuntu: apt-get install fonts-urw-base35) '
        'or set FONT at the head of each script to a local Helvetica-metric family.',
        file=sys.stderr,
    )
