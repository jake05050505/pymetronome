import argparse
import sys
import time
import winsound

def main():
    # if value argument is missing
    if len(sys.argv) == 1:
        value = int(input("Please enter BPM:"))
        delay_sec = 60 / value
        bpm = 60 / delay_sec
    else:
        parser = argparse.ArgumentParser(description="Simple metronome")
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

    print(f"Metronome: {bpm:.2f} BPM ({delay_sec*1000:.1f} ms interval). Ctrl+C to stop.")

    try:
        while True:
            winsound.PlaySound(f"{__file__}\\..\\sounds\\stick.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            time.sleep(delay_sec)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
