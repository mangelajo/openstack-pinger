# openstack-pinger


Use as:
```bash

source ~/overcloudrc
./ping_routers_and_fips.sh | tee pinger.log

./checkpings.py pinger.log

```


or:

```bash
source ~/overcloudrc
./ping_routers_and_fips.sh | ./checkpings.py
```

on the other hand, pinger.sh takes a list of IP addresses:

```bash
./pinger.sh 10.0.0.10 10.0.0.11 10.0.0.13 | ./checkpings.py
```

