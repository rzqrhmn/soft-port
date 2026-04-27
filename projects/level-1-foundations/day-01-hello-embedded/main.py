"""
Day 01 — Hello, embedded world.

Goal: print the names of the 3 sensors we'll use throughout this portfolio.
"""


def main() -> None:
    # TODO: replace this with a list of sensor names + a for-loop that prints each.
    # Sensors we'll work with: temp_motor, vibration, current
    sensors = ["temp_motor", "vibration", "current"]  # <-- fill this in

    for sensor in sensors:
        print(sensor)


if __name__ == "__main__":
    main()
