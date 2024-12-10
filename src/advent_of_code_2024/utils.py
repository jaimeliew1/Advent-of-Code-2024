def print_complex_map(map: dict[complex, int]):
    """
    Print a dictionary containing complex map in 2D.
    """
    Nx = int(max(x.real for x in map.keys()))
    Ny = int(max(x.imag for x in map.keys()))

    out = []
    for i in range(Ny + 1):
        line = ""
        for j in range(Nx + 1):
            if (v := map.get(complex(j, i))) is not None:
                line += str(v)
            else:
                line += "."
        out.append(line)

    print("\n".join(out))
    print()
