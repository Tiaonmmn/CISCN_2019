#!/bin/sh
service apache2 start
service mysql start
mysql < /var/www/html/admin448bfdcd-c968-4d05-b9aa-7563a9e9cd19/flag.sql
rm -rfv /var/www/html/admin448bfdcd-c968-4d05-b9aa-7563a9e9cd19/flag.sql
su ciscn -l -c "nohup python main.py >/dev/null 2>&1 &"

