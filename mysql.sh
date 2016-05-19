mysql -uroot -e "CREATE DATABASE djbase;"
mysql -uroot -e "CREATE USER 'django@localhost' IDENTIFIED BY 'pass123';"
mysql -uroot -e "GRANT ALL ON djbase.* TO 'django@localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
