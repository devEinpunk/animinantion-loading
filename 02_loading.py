import time
import sys

# animation = "|/-\\"

# animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "99%"]

animation = [
    "[■□□□□□□□□□]",
    "[■■□□□□□□□□]",
    "[■■■□□□□□□□]",
    "[■■■■□□□□□□]",
    "[■■■■■□□□□□]",
    "[■■■■■■□□□□]",
    "[■■■■■■■□□□]",
    "[■■■■■■■■□□]",
    "[■■■■■■■■■□]",
    "[■■■■■■■■■■]",
]

for i in range(360):
    time.sleep(0.1)
    sys.stdout.write(
        "\currently debugging and rebasing node bugs.... "
        + animation[i % len(animation)]
    )
    sys.stdout.flush()

print("\nDone!")
