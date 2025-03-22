class EmailService:
    def _connect(self):
        print("connecting to the email server....")

    def _authenticating(self):
        print("authenticating the user....")

    def send_email(self):
        self._connect()
        self._authenticating()
        print("sending email....")
        self._disconnect()

    def _disconnect(self):
        print("disconnecting from the email server....")


email_service = EmailService()

email_service.send_email()

