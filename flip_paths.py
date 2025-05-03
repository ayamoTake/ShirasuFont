from copy import deepcopy

def flip_paths_vertically(paths, height=1024):
    flipped = []
    for path in paths:
        new_path = deepcopy(path)
        for seg in new_path:
            seg.start = complex(seg.start.real, height - seg.start.imag)
            seg.end = complex(seg.end.real, height - seg.end.imag)
            if hasattr(seg, 'control1'):
                seg.control1 = complex(seg.control1.real, height - seg.control1.imag)
            if hasattr(seg, 'control2'):
                seg.control2 = complex(seg.control2.real, height - seg.control2.imag)
        flipped.append(new_path)

    diff=5000j
    return [p.translated(diff) for p in flipped]
