create database denma DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
create user 'denma_admin'@'localhost' identified by '*******';
grant all on denma.* to 'denma_admin'@'localhost';

cronjob added (path cropped)
0 0 * * * python manage.py getwebtooninfo --latest > var/log/getwebtooninfo."`date +\%d`".log 2>&1

