# TidyCmd

TidyCmd is a class for Python 3.5 to tidy up the process of piping Unix shell commands together. 
Instead of large blocks of Popen text chained together, this class will automatically pipe commands together for you. It stores the exit code, stdOut, and stdErr for processing in your code.

### Version
0.1.0

## License
MIT License

## Contributing
Contributions are always welcome; if you fix a bug or implement some extra functionality please issue a PR back to https://github.com/laurieodgers/pythoncmd

## Features
  - Allows for neater code vs large blocks of Popen statements chained together
  - No need to fiddle with connecting stdout to stdin for each pipe
  - Choose your format to decode stdOut/stdErr to

### Usage

The following shell command will retrieve the MAC address of eth0:
```
ifconfig | grep eth0 | awk '{ print $5 }'
```

To achieve the same thing with TidyCmd:
```
tidyCmd = TidyCmd(['ifconfig'])

tidyCmd.appendPipe(['grep', 'eth0'])

tidyCmd.appendPipe(['awk', '{ print $5 }'])

tidyCmd.run()

print(tidyCmd.getStdOut())
```
