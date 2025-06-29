D3 FPS (Frames Per Second) Analysis

SCM Repo: https://github.com/rhocevar/d3fps

Goal: process a directory of "FPS performance log" files which are collections of performance samples and metadata represented as JSON objects.

Requirements:
- It should accept the following arguments: "act", "calc_type", "data_dir"
- It should process JSON files from the supplied "data_dir"
- It should be able to calculate and report back the minimum/maximum FPS values or the computed average FPS for the desired Act

Notes:
- Please cite any references you used in making this tool
https://www.jenkins.io/doc/tutorials/#pipeline


- Please specify the type of pipeline script created
The Jenkins pipeline job was configured using 'pipeline script from SCM'. The SCM repo is available at https://github.com/rhocevar/d3fps.


- Provide a list of tools/programs/libraries/frameworks used in it's creation
The python script was implemented and tested using PyCharm IDE.
Jenkins version 2.504.3
Python version 3.9.6

