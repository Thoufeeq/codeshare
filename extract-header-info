import imaplib
import email

imap_host = 'imap.gmail.com'
imap_user = 'email address'
imap_pass = 'password'

## open a connection
imap = imaplib.IMAP4_SSL(imap_host)

## login
imap.login(imap_user, imap_pass)

try:
    imap.select('INBOX', readonly=True)

    typ, msg_data = imap.fetch('1', '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1])
            for header in [ 'subject', 'to', 'from' ]:
                print '%-8s: %s' % (header.upper(), msg[header])

finally:
    try:
        imap.close()
    except:
        pass
    imap.logout()
