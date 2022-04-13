#!/bin/bash
# This script checks if there is a need to reboot due to the kernel being updated or one or more services. Requires 'reboot-required', which is supplied with yum-utils.

/usr/bin/needs-restarting -r  >/dev/null 2>&1
KERNEL=$?

SERVICE="$(/usr/bin/needs-restarting -s | /usr/bin/wc -l)"

if [ ! -e /var/run/yum.pid ]; then
  if [ $KERNEL -eq 1 ] || [ $SERVICE -gt 0 ]; then
   /usr/sbin/reboot
  fi
fi
