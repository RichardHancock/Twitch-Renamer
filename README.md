Twitch Renamer  
=============================

**Not really intended for anyone else to use, was mostly just a practice project to get python packages built, tested and deployed with GitLab CI.**
  
Was mostly created as I had a bunch of files that youtube-dl download with messed up titles, literally a one time incident. But hey good practice right?

Required Command Line inputs
-----------------------------

- **path** Path to directory of files to rename
  
Optional Command Line inputs
-----------------------------

- **-h, --help** The help for the command line inputs.  
  
- **-v, --version** Show the program's version number and exit.  

- **-d, --dry** Perform the renames as a dry run, meaning the original files are left unchanged and the results are outputted to the console.

- **-s, --skip-warn** Skips all warnings, mostly for the CI builds
