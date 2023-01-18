#!/bin/bash
cd /home/jam/pvcV1.3/pvcCode
# FTP LOGIN
HOST='ftp.endeardistribution.com'
LHOST='jam@hidden12.lan'
USER='jmcnary@sojournerlogistics.com'
PASSWORD='22simplestartup'

# DISTANT DIRECTORY
REMOTE_DIR='/siteData'

#LOCAL DIRECTORY
LOCAL_DIR='/home/jam/pvcV1.4/siteData'

# RUNTIME!
echo

echo "Starting only missing download from $LHOST $LOCAL_DIR to $HOST $REMOTE_DIR"

date

lftp -u "$USER","$PASSWORD" $HOST <<EOF
# the next 3 lines put you in ftpes mode. Uncomment if you are having trouble connecting.

set ssl:check-hostname no

set ftp:ssl-force true

set ftp:ssl-protect-data true

set ssl:verify-certificate no

# transfer starts now...

set sftp:auto-confirm yes

mirror -R --only-missing $LOCAL_DIR $REMOTE_DIR;

exit

EOF

echo

echo "Transfer finished"

date

#ddlftp jam@hidden12.lan , PLASTIC321352mug13321 << EOF

#mirror --only-missing --file=test.txt
