import smtplib

def sendYaleEmail(sender, receiver, message, creds):
    try:
        smtpObj = smtplib.SMTP('mail.yale.edu', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(creds['user'], creds['pass'])
        smtpObj.sendmail(sender, receiver, message)
        print "Successfully sent email to %s" % (receiver)
        smtpObj.close()
    except:
        print "please check your credentials"
