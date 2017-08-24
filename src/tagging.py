from emails import sendYaleEmail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# needs to be set
fbLink = "fb.com"
meEmail = "lifeng.wang@yale.edu"

def getCreds():
    file = open('../creds.txt', 'r')
    # instead of a creds file - ask for credentials
    # for testing purposes
    credLst = file.read().split()
    creds = {}
    creds['user'] = credLst[0]
    creds['pass'] = credLst[1]
    return creds


def matchAndSend():
    # list of names of the matched people in file
    one = userParser('../one.txt')
    two = userParser('../two.txt')
    matchedPairs = zip(one, two)

    for matchedPair in matchedPairs:
        pair = list(matchedPair)
        pairSend(pair)

def pairSend(pair):
    body = open('../emailBody.txt', 'r')
    strBody = str(body.read())
    for i in range(len(pair)):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "CASA Lunch Tag"
        msg['From'] = "Lifeng Wang<lifeng.wang@yale.edu>"
        msg['To'] = '%s<%s>' % (pair[i]['name'], pair[i]['email'])
        content = strBody % (pair[(i+1) % 2]['name'], pair[(i+1) % 2]['email'], fbLink)
        body = MIMEText('<br>'.join(content.split('\n')), "html")
        msg.attach(body)
        sendYaleEmail(meEmail, pair[i]['email'], msg.as_string(), getCreds())

def userParser(fileName):
    peeps = []
    txt = open(fileName, 'r')
    info = txt.read().split('\n')
    for person in info:
        if person != "":
            details = {}
            personal = person.split()
            lastIndex = len(personal) - 1
            details['email'] = personal[lastIndex]
            details['name'] = ' '.join(personal[:lastIndex:])
            peeps.append(details)
    return peeps
#
# for pair in matchedPairs:
#     matchedPair = list(pair)
#     message = """From: Alex<lifeng.wang@yale.edu>\nTo: Boo\nSubject: test\nthis is a test %s""" % ("testtttt")
#     message = message + "hello"
def final():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "CASA Lunch Tag"
    msg['From'] = "Alex Wang<lifeng.wang@yale.edu>"
    for matchedPair in matchedPairs:
        pair = list(matchedPair)
        msg['To'] = 'lifeng, alex'
        print msg['To']

        # msg['CC'] = "bar"
        content = "%s and %s" % (pair[0], pair[1])
        body = MIMEText(content, "html")
        msg.attach(body)
        sendYaleEmail("lifeng.wang@yale.edu", ','.join(pair), msg.as_string(), creds)

if __name__ == '__main__':
    print matchAndSend()
