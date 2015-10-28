import imaplib

imap_host = 'imap.gmail.com'
imap_user = 'username@gmail.com'
imap_pass = 'password@gmail.com'

## open a connection
imap = imaplib.IMAP4_SSL(imap_host)

## login
imap.login(imap_user, imap_pass)

## get status for the mailbox (folder) INBOX
folderStatus, UnseenInfo = imap.status('INBOX', "(UNSEEN)")

print folderStatus

NotReadCounter = int(UnseenInfo[0].split()[2].strip(').,]'))
print NotReadCounter

## folders list
status, folder_list = imap.list()

## select a specific folder
status, data = imap.select('INBOX')

## fetching message header by  using message( ID)
status, msg_header = imap.fetch('1', '(BODY.PEEK[HEADER])')
