def process_line(line):
    if line[0]=="#":
        return None
    line = line.strip()
    if "#" in line:
        line = line[:line.index("#")]
    line = line.strip()
    line = line.split(" ")
    line = line[0].split("\t") + line[1:]
    if len(line)==1:
        return None
    return line