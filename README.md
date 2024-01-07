# rdbms_tools
rdbms_tools for testing

## Prerequisites

## Quick start

```shell
#check postgresql status
dpkg -l | grep postgresql
sudo service postgresql status
systemctl status postgresql


#purge
sudo apt purge postgresql-*

#rm
sudo rm -rf /etc/postgresql/
sudo rm -rf /etc/postgresql-common/
sudo rm -rf /var/lib/postgresql/
sudo userdel -r postgres
sudo groupdel postgres
```