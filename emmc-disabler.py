#!/usr/bin/python

import os
import glob
import syslog

if os.path.exists("/sys/block/mmcblk0boot0"):
    syslog.openlog("dsctl-emmc-disabler")
    devname = glob.glob("/sys/block/mmcblk0boot0/device/device/driver/mmc0*")[0].rsplit('/', 1)[1]
    try:
        outf = open("/sys/block/mmcblk0boot0/device/device/driver/unbind", 'w')
        outf.write(devname)
        outf.close()
    except:
        syslog.syslog(syslog.LOG_WARNING, "Failed to disable internal eMMC card!")
    else:
        syslog.syslog(syslog.LOG_DEBUG, "Successfully disabled internal eMMC card")
    syslog.closelog()
