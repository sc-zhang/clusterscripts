#!/usr/bin/env python
import argparse
import os


header = '''#!/bin/bash
#SBATCH -J %s
#SBATCH -p %s
#SBATCH -N 1
#SBATCH -c %d
#SBATCH --comment=no
#SBATCH -o %s.out
#SBATCH -e %s.err
'''


def get_opts():
    group = argparse.ArgumentParser()
    group.add_argument("-c", "--cmd", help="Input cmd list file, each line contain one command for sbatch", required=True)
    group.add_argument("-q", "--queue", help="Submit queue, default=low", type=str, default="low")
    group.add_argument("-b", "--batch", help="Prefix of batch files, auto increasing, default=run", type=str, default="run")
    group.add_argument("-l", "--log", help="Prefix of log files, auto increasing, default=log", type=str, default="log")
    group.add_argument("-t", "--thread", help="threads for sbatch, default=12", type=int, default=12)
    return group.parse_args()


def ssbatch(cmd_file, queue, batch_pre, log_pre, threads):
    cmd_list = []
    print("Loading %s"%cmd_file)
    with open(cmd_file, 'r') as fin:
        for line in fin:
            if line.strip() == "" or line[0] == "#":
                continue
            cmd_list.append(line.strip())
    
    print("Writing batch files")
    batch_list = []
    idx = 1
    for cmd in cmd_list:
        job_name = "%s%d"%(batch_pre, idx)
        log_name = "%s%d"%(log_pre, idx)
        idx += 1
        batch_name = "%s.sh"%job_name
        with open(batch_name, 'w') as fout:
            cur_header = header%(job_name, queue, threads, log_name, log_name)
            fout.write("%s\n%s\n"%(cur_header, cmd))
        batch_list.append(batch_name)
    
    print("Submitting jobs")
    for job in batch_list:
        cmd = "sbatch %s"%job
        os.system(cmd)
    
    print("Finished")


if __name__ == "__main__":
    opts = get_opts()
    cmd_file = opts.cmd
    queue = opts.queue
    batch_pre = opts.batch
    log_pre = opts.log
    threads = opts.thread
    ssbatch(cmd_file, queue, batch_pre, log_pre, threads)
    
