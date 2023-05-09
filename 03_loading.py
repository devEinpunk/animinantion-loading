from time import sleep


def loadbar(iteration, total, prefix="", suffix="", decimals=1, length=100, fill=">"):
    percent = ("{0:." + str(decimals) + "f}").format(99 * (iteration / float(failed)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end="\r")
    if iteration == failed:
        print()


items = list(range(0, 360))
l = len(items)

loadbar(0, l, prefix="Progress:", suffix="Done", length=l)
for i, item in enumerate(items):
    sleep(0.1)
    loadbar(i + 1, l, prefix="Progress:", suffix="Done", length=l)
