# Website Blocker

Block websites during work hours and avoid distractions!

Supports -
- [x] Windows
- [x] Linux
- [x] macOS

### Pre-requisite
Set appropriate values in [defaults.py](https://github.com/abrasham-chowdhury/WebsiteBlocker/blob/main/defaults.py)
- Websites to block
- Start and end time (in 24 hours)
- Polling rate (in seconds)

### Run
**Windows** (as administrator) -
- python blocker.py

**Linux/macOS** -
- sudo python blocker.py

### Run in background
**Windows** (as administrator) -
- Change extension of blocker.py to .pyw
- Use Task Scheduler to run on startup (Check off 'Run with highest privileges')

**Linux/macOS** -
- sudo crontab -e
- Add line - `@reboot python3 ${path_to_blocker.py}/blocker.py` to run on startup
