import ftplib

# log in
ftp = ftplib.FTP('ftp.sec.gov','anonymous','@anonymous')

# list contents
ftp.retrlines('LIST')

#change directory
ftp.cwd('edgar')

#retrieve README file from edgar
ftp.retrbinary('RETR README.txt', open('README.txt', 'wb').write)

# quit
ftp.quit()