# import smtplib

# gmail_user = 'zahrapoorsoltani7@gmail.com'
# password = 'zahraP00@@$$'
# password = 'teduqtaincopvbct'
# TO ='sarvaritoktam57@gmail.com'


# SUBJECT = "Testing sending using gmail"
# TEXT = "Testing sending mail using gmail servers"

# BODY = '\r\n'.join(['To: %s' % TO,
#         'From: %s' % gmail_user,
#         'Subject: %s' % SUBJECT,
#         '', TEXT])

# server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
# server.login(gmail_user, password)
# server.sendmail(gmail_user, TO, BODY)


import smtplib, ssl

EMAIL_HOST_USER = 'zahrapoorsoltani7@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'zahraP00@@$$'
EMAIL_HOST_PASSWORD = 'teduqtaincopvbct'
EMAIL_PORT_SSL = 465

with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(EMAIL_HOST_USER, 'sarvaritoktam57@gmail.com', 'your message')