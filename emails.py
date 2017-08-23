import smtplib

smtpObj = smtplib.SMTP('mail.yale.edu', 587)

def sendYaleEmail(smtpObj, sender, receiver, content, creds):
    smtpObj.ehlo()
    smtpObj.startttls()
    smtpObj.login(getattr(creds, 'user'), getattr(creds, 'pass'))
    smtpObj.sendmail(sender, receiver, content)
    print "Successfully sent email to %s" % (receiver)
    smtpObj.close()
