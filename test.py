from tidycmd import TidyCmd
# the following represents the following command being run within the shell:
# ifconfig | grep eth0 | awk '{ print $5 }

# create the object with the first command
tidyCmd = TidyCmd(['ifconfig'])
# first pipe
tidyCmd.appendPipe(['grep', 'eth0'])
# second pipe
tidyCmd.appendPipe(['awk', '{ print $5 }'])

# run the command
tidyCmd.run()

# print stdOut
print(tidyCmd.getStdOut())

# print stdErr
print(tidyCmd.getStdErr())

# print out the command as a string
print(tidyCmd)