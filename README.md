# moshup
Simple CLI wrapper for mosh connections.

`moshup` wraps the Mosh command and inject some arguments that makes it more useful for me. This includes setting up a particular session and optionally invoking `tmux`.

## Installation

```
pip install .
```

## Usage

```
Usage: moshup [OPTIONS] HOSTNAME

Options:
  --username TEXT  Username for host.
  --no_tmux        Do not invoke tmux on connection.
  --help           Show this message and exit.
```

Note: having hostnames configured in ~/.ssh/config is a nice way to have aliases for hostnames and usernames.
