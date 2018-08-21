from distutils.core import setup
setup(
      name = 'tidycmd',
      packages = ['tidycmd'],
      version = '1.1.0',
      description = 'TidyCmd is a class for Python 3.5 to tidy up and simplify the process of piping Unix shell commands together securely, no "shell=True" necessary! Instead of large blocks of Popen text chained together, this class will automatically pipe commands together for you. It stores the exit code, stdOut, and stdErr for processing in your code.',
      author = 'Laurie Odgers',
      author_email = 'laurieodgers83@gmail.com',
      url = 'https://github.com/laurieodgers/tidycmd',
      download_url = 'https://github.com/laurieodgers/tidycmd/archive/1.0.0.tar.gz',
      keywords = ['tidycmd', 'cmd', 'pipe', 'cli'],
      classifiers = [],
)
