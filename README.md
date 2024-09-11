# Cluster Scripts
A set of scripts for cluster users

# Installation
```bash
git clone https://github.com/sc-zhang/clusterscripts.git
cd clusterscripts
chmod +x bin/*.*
```

# Usage

- **zsub:** A script for SLURM/SGE/TORQUE users, it will automatically generate batch files with a command list file 
and submit them to the job scheduler.
```bash
usage: zsub [-h] -c CMD [-q QUEUE] [-b BATCH] [-g {slurm,sge,torque}] [-l LOG] [-t THREAD]

options:
  -h, --help            show this help message and exit
  -c CMD, --cmd CMD     Input cmd list file, each line contain one command for sbatch
  -q QUEUE, --queue QUEUE
                        Submit queue, default=low
  -b BATCH, --batch BATCH
                        Prefix of batch files, auto increasing, default=run
  -g {slurm,sge,torque}, --grid {slurm,sge,torque}
                        Grid engine, could be slurm, sge, torque, default=slurm
  -l LOG, --log LOG     Prefix of log files, auto increasing, default same with batch
  -t THREAD, --thread THREAD
                        threads for sbatch, default=12
```
> Notice: cmd list file can contain empty lines, and every line start with "#" will be dropped, 
> commands for each job must be written in one line.