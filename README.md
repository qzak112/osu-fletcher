# osu! Fletcher - Combo Break Punisher (Windows)

Plays an audio clip of Terence Fletcher "Were you rushing or dragging?" from Whiplash every time you break combo in osu! Lazer.

## Why

Because suffering produces excellence.

## Requirements

- osu! Lazer
- tosu (for memory reading) - [Download from tosu.dev](https://tosu.dev)
- Python 3 with websockets
- A desire to be psychologically harassed by a fictional band conductor

## Installation

1. Install tosu:
   - Download from [tosu releases](https://github.com/tosuapp/tosu/releases)
   - Run the installer
   - tosu will start automatically with Windows (or run manually)

2. Install Python dependencies:
```cmd
pip install websockets
```

3. Get Fletcher audio clip (not included for copyright reasons):
   - Download "Were you rushing or dragging?" from Whiplash
   - Trim to 2 seconds
   - Amplify volume: `ffmpeg -i fletcher.wav -filter:a "volume=10.0" fletcher_loud.wav`
   - Place at `C:\Users\YOUR_USERNAME\fletcher_loud.wav`

## Usage

1. Make sure tosu is running (check system tray)

2. Launch osu! Lazer

3. Run the script:
```cmd
python fletcher.py
```

4. Play osu and suffer appropriately when you break combo

## Notes

- No sudo/permissions needed on Windows, tosu handles memory reading automatically
- Audio plays via winsound (built into Python, no extra audio software needed)

## License

MIT (Fletcher audio not included, obtain legally)

## Disclaimer

This will not improve your accuracy. It will make you more anxious. Use responsibly.
