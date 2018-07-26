#!/bin/sh

# this function pings and output in timestamped format
pinger() {
        ping -i 0.25 $1 | \
        while read pong; do
                echo "$(date +%Y-%m-%d\ %H:%M:%S.%03N) pinger DEBUG $pong";
        done
}


for i in $* ; do
   pinger $i &
done

wait
