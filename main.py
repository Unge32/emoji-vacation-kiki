#!/usr/bin/env python3
"""KIKI -- one palm tree for the dream vacation she keeps picturing.

Kiki works at a desk where the inbox never empties. Every morning
she opens her laptop to a hundred unread messages, and every evening
she closes it the same way, a little further behind than she was.
Her dream vacation is not a resort brochure or a checklist of
sights; it is the opposite of all that noise -- one palm tree on a
quiet beach, somewhere far enough away that no notification can
find her.

That is why a single palm tree says everything she cannot put
into words. No words, no itinerary,
no flight number: just the tree, the sand it stands on, and the sea
behind it, everything Kiki is saving her daydreams for in one small
picture. A stranger sees it and is already there, barefoot, phone
off, shade overhead, nowhere to be until the sun goes down.

The brief asks for exactly one emoji and nothing else, standing in
for the trip of your dreams, and this is Kiki's answer: the palm
tree is her whole holiday, condensed to a single character. It fits
the gate exactly -- one character, one code point, one dream -- and
it leaves the rest to the imagination, which is where every great
vacation begins anyway.
"""

import os

LINE = "🌴"


def main():
    assert len(LINE) == 1, "line must be exactly one emoji character"
    assert ord(LINE) == 0x1F334, "line must be U+1F334 PALM TREE"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d character" % (path, len(LINE)))


if __name__ == "__main__":
    main()
