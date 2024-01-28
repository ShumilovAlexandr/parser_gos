from ftplib import FTP


class FTPConnectionView(FTP):

    def __init__(self):
        self.user = 'free'
        self.passwd = 'free'
        self.url = 'ftp.zakupki.gov.ru'
        super(FTPConnectionView, self).__init__()

    def connect(self):
        super(FTPConnectionView, self).connect(self.url)

    def login(self):
        super(FTPConnectionView, self).login(user=self.user, passwd = self.passwd)

    def quit(self):
        super(FTPConnectionView, self).quit()


