# TidyCmd

TidyCmd is a class for Python to tidy up and simplify the process of piping Unix shell commands together securely, no "shell=True" necessary!

Instead of large blocks of Popen text chained together, this class will automatically pipe commands together for you. It stores the exit code, stdOut, and stdErr for processing in your code.

## Installation

Python 2.x:
`pip install tidycmd`

Python 3.x:
`pip3 install tidycmd`

## Usage:
```
from tidycmd import TidyCmd
```

The following shell command will retrieve the MAC address of eth0:
```
ifconfig | grep eth0 | awk '{ print $5 }'
```

To achieve the same thing with TidyCmd:
```
tidyCmd = TidyCmd(['ifconfig'])

tidyCmd.appendPipe(['grep', 'eth0'])

tidyCmd.appendPipe(['awk', '{ print $5 }'])

print(tidyCmd.run())

```

stderr, stdout and the exit code are all stored for your later use:
```
# access stdout as a string:
print(tidyCmd.getStdOut())

# access stdout as bytes:
print(tidyCmd.stdOut)

# access stderr as a string:
print(tidyCmd.getStdErr())

# access stderr as bytes:
print(tidyCmd.stdErr)

# get the exit code
print(tidyCmd.returnCode)

```

Modify your environment:
```
tidyCmd = TidyCmd(['env'], {'TIDYCMD_TEST': "TESTING"})
```

### Version
1.0.2

## License
MIT License

## Changelog
### 1.1.0
- Added ability to change environment
- Added "exitCode" which is a more correct name for "returnCode" (now deprecated)

### 1.0.0
- Updated structure for pip submission

### 0.3.0
- Changed getStdOut() to trim the last newline from stdout
- Changed getStdErr() to trim the last newline from stderr
- Changed run() to return stdout from the end of the PIPE chain, with last newline trimmed

### 0.2.0
- Added __str__ function to output a shell compatible command with quoting of blocks which include spaces.

### 0.1.0
- Initial commit

## Contributing
Contributions are always welcome; if you fix a bug or implement some extra functionality please issue a PR back to https://github.com/laurieodgers/tidycmd

## Features
  - Allows for neater code vs large blocks of Popen statements chained together.
  - No need to fiddle with connecting stdout to stdin for each pipe; the plumbing between processes is performed automatically.
  - Choose your format to decode stdOut/stdErr to.
  - str(tidyCmd) will output a string which can be used in a shell for testing. This function will also automatically quote any elements which contain spaces.
