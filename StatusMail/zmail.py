#!/usr/bin/env python
#-.- coding: utf-8 -.-

from notify.mail import send_mail
from notify.util import logger, getconf
from subprocess import Popen, PIPE

if __name__ == '__main__':
    logger.info('begin zmail')
    logger.info('-' * 11)

    message = 'R300 berichtet:\n'

    try:
        p = Popen(['/sbin/zpool', 'status'], stdout=PIPE)
        zpoolstatus = p.communicate()[0]
        message += 'zpool status:\n\n' + zpoolstatus
    except Exception as e:
        logger.error('zpool status failed: %s' %(e))
    else:
        logger.info('zpool status: %s' %(zpoolstatus))


    send_mail(['mail@example.com'], message, subject = 'R300 Status', subjectdate = True, files = ['/data/freenas-v1.db'])
    logger.info('end zmail')
    logger.info('-' * 9)
