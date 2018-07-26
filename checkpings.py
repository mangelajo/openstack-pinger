#!/usr/bin/python
import sys
import datetime


def difftime(curr, prev):
    prev_dt = datetime.datetime.strptime(prev_ts,"%Y-%m-%d %H:%M:%S.%f")
    curr_dt = datetime.datetime.strptime(ts,"%Y-%m-%d %H:%M:%S.%f")
    diff = str(curr_dt - prev_dt)
    return diff

ip_seq = {}
ip_ts = {}

f = None
if len(sys.argv) < 2:
    f = sys.stdin
else:
    f =  open(sys.argv[1], 'r')

for line in f:
    parts = line.split(' ')

    ts = None
    ip = None
    seq = None
    try:
        ts = ' '.join(parts[0:2])
        ip = parts[7]
        seq = int(parts[8].split('=')[1])
    except:
        continue

    prev_seq = ip_seq.get(ip, seq)
    prev_ts = ip_ts.get(ip, ts)

    if prev_seq < (seq - 1):
        diff = difftime(ts, prev_ts)
        print "Sequence lost for ip %s (%d - %d)  %s to %s. (%s offline)" % (ip, prev_seq, seq, prev_ts, ts, diff)

    ip_seq[ip] = seq
    ip_ts[ip] = ts
    last_seq = seq
    last_ts = ts


for ip, seq in ip_seq.items():
   if (int(last_seq) -  int(seq)) > 10:
        prev_ts = ip_ts[ip]
        diff = difftime(last_ts, prev_ts)
        print "IP %s was down for %s and never recovered since seq %s" % (ip, diff, seq)
