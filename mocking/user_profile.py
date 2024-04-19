class UserProfile:
    def __init__(self, data_service):
        self.data_service = data_service

    def fetch_user_data(self):
        return self.data_service.get_user_data()
