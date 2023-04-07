from pathlib import Path

filename = Path(__file__).parent / "hblog"
print(filename)
with open(filename, mode="w") as f:
    lines = f.readline()
    lines.replace("\\n", "\n")
    f.write(lines)
