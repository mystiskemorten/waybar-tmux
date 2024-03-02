# waybar-tmux

This script was an experiment to see if it was possible to have a tmux status line
as a custom module in Waybar. Simply just to reduce the amount of status lines on
screen.

The tmux status line is refreshed upon events by using hooks in tmux.

## Setup

- Download and move tmux.py file to preferred location
- Add your new tmux custom module to your Waybar config as shown in the code below
- Remember to include path for file in the exec field

```json
....
  },
  "custom/tmux": {
    "format": "{}",
    "interval": "once",
    "exec": "{PATH_TO_FILE}/tmux.py",
    "signal": 13
  }
.....

```

- Add hooks to tmux config which signals our Waybar module to rerender

```tmux
set-hook -g session-window-changed 'run-shell "pkill -RTMIN+13 waybar"'
set-hook -g client-session-changed 'run-shell "pkill -RTMIN+13 waybar"'
set-hook -g window-renamed 'run-shell "pkill -RTMIN+13 waybar"'
set-hook -g session-closed 'run-shell "pkill -RTMIN+13 waybar"'
```
