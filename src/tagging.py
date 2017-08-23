from emails import sendYaleEmail
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "CASA Lunch Tag"
        msg['From'] = "Lifeng Wang<lifeng.wang@yale.edu>"
        msg['To'] = '%s<%s>, %s<%s>' % (pair[0]['name'],
                                        pair[0]['email'],
                                        pair[1]['name'],
                                        pair[1]['email'])

        # msg['CC'] = "bar"
        content = "%s and %s foo bar" % (pair[0]['name'], pair[1]['name'])
        body = MIMEText(content, "html")
        msg.attach(body)
        sendYaleEmail("lifeng.wang@yale.edu", [pair[1]['email'], "lifengawang@gmail.com"], msg.as_string(), getCreds())

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
