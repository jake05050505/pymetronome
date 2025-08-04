from argparse import ArgumentParser
from pathlib import Path
from sys import argv
from time import sleep
import winsound

def main():
    # region inputs
    # if the program was run via running metronome.py from explorer or bpm value is missing
    if len(argv) == 1:
        value = int(input("Please enter BPM:"))
        delay_sec = 60 / value
        bpm = 60 / delay_sec
    else:
        parser = ArgumentParser(description="Simple metronome")
        parser.add_argument(
            "value",
            type=float,
            help="Beats per minute (BPM), or milliseconds delay if -d is given"
            )
        parser.add_argument("-d", "--delay",
            action="store_true",
            help="Treat value as delay in milliseconds instead of BPM"
            )
        args = parser.parse_args()

        delay_sec = args.value / 1000.0 if args.delay else 60.0 / args.value
        bpm = 60.0 / delay_sec
    # endregion

    print(f"Metronome: {bpm:.2f} BPM ({delay_sec*1000:.1f} ms interval).")

    try:
        while True:
            winsound.PlaySound(f"{Path(__file__).parent}/sounds/stick.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            sleep(delay_sec)
    except KeyboardInterrupt:
        print("\nStopped.")

    return 0

if __name__ == "__main__":
    main()