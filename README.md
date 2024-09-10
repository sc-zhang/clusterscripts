# Cluster Scripts
A set of scripts for cluster users

# Installation
```bash
git clone https://github.com/sc-zhang/clusterscripts.git
cd clusterscripts
chmod +x bin/*.*
```

# Usage

- **ssbatch.py:** A script for SLURM users, it will automatically generate batch files and submit them to the job manager.
```bash
usage: ssbatch.py [-h] -c CMD [-q QUEUE] [-b BATCH] [-l LOG] [-t THREAD]

options:
  -h, --help            show this help message and exit
  -c CMD, --cmd CMD     Input cmd list file, each line contain one command for sbatch
  -q QUEUE, --queue QUEUE
                        Submit queue, default=low
  -b BATCH, --batch BATCH
                        Prefix of batch files, auto increasing, default=run
  -l LOG, --log LOG     Prefix of log files, auto increasing, default=log
  -t THREAD, --thread THREAD
                        threads for sbatch, default=12
```
> Notice: cmd list file can contain empty lines, and every line start with "#" will be dropped, commands for each job must within one line.