# osu! Fletcher - Combo Break Punisher
Plays an audio clip of Terence Fletcher "Were you rushing or dragging?" from Whiplash every time you break combo in osu! Lazer.
## Why

Because suffering produces excellence.

## Requirements

- osu! Lazer
- tosu (for memory reading)
- Python 3 with websockets
- paplay (PulseAudio)
- A desire to be psychologically harassed by a fictional band conductor

## Installation

1. Install tosu:
```bash
yay -S tosu
```

2. Give tosu memory reading permissions:
```bash
sudo setcap cap_sys_ptrace=eip /opt/tosu/tosu
```

3. Install Python dependencies:
```bash
pip install websockets --break-system-packages
```

4. Get Fletcher audio clip (not included for copyright reasons):
   - Download "Were you rushing or dragging?" from Whiplash
   - Trim to 2 seconds
   - Amplify volume: `ffmpeg -i fletcher.wav -filter:a "volume=10.0" fletcher_loud.wav`
   - Place at `~/fletcher_loud.wav` (your home directory)

5. Update the script path in `fletcher.py`

## Usage

1. Start tosu:
```bash
sudo tosu
```

2. Launch osu! Lazer

3. Run the script:
```bash
python fletcher.py
```

4. Play osu and suffer appropriately when you break combo

## Future Plans

- Arduino microcontroller version with physical speaker
- More Fletcher quotes for different fail states
- Configurable combo threshold
- Support for osu! stable (maybe)
- Support for windows(only tested in linux)

## License

MIT (Fletcher audio not included, obtain legally)

## Disclaimer

This will not improve your accuracy. It will make you more anxious. Use responsibly.
