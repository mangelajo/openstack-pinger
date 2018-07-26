#!/bin/sh

# this function pings and output in timestamped format
pinger() {
        ping -i 1 $1 | \
        while read pong; do
                echo "$(date +%Y-%m-%d\ %H:%M:%S.%03N) pinger DEBUG $pong";
        done
}

source ~/overcloudrc

# Find the Associated (not None on Fixed IP) FIPs on the overcloud

IPS=$(openstack floating ip list  -f value -c 'Floating IP Address' -c 'Fixed IP Address' | grep -v None | cut -d\  -f 1)
ROUTER_IPS=$(neutron router-list | egrep -oE "10\.0\.0\.[0123456789]{1,3}")
IPS="$IPS $ROUTER_IPS"

if [[ "z$IPS" == "z" ]]; then
  echo There are no associated floating ips to ping on the overcloud
  exit 1
fi

for i in $IPS ; do
   pinger $i &
done

wait
