#!/usr/bin/env python
#-.- coding: utf-8 -.-

print 'ä',

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.encoders import encode_base64
from subprocess import Popen, PIPE

from datetime import datetime
from time import strftime

now = datetime.now().strftime('%Y-%m-%d_%H:%M')

msg = MIMEMultipart()
msg.attach(MIMEText('R300 berichtet:'))
msg.attach(MIMEText('\n'))

p = Popen(['/sbin/zpool', 'status'], stdout=PIPE)
msg.attach(MIMEText('zpool status:\n\n' + p.communicate()[0]))
msg.attach(MIMEText('\n'))

configdb = MIMEApplication('application/x-sqlite3')
configdb.set_payload(open('/data/freenas-v1.db', 'rb').read())
configdb.add_header('Content-Disposition', 'attachment', filename='R300-config-' + now + '.db')
encode_base64(configdb)

msg.attach(configdb)
msg.attach(MIMEText('\n'))

msg.attach(MIMEText('-' * 5 + '\nYour Ad here!'))
print 'ö',

msg['To'] = 'spky'
msg['Subject'] = 'R300 Status ' + now

p = Popen(['/usr/sbin/sendmail', '-t'], stdin=PIPE)
p.communicate(msg.as_string())

print 'ü'
