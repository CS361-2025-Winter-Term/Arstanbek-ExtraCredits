from notification_preferences import NotificationPreferences


class UserProfile:
    def __init__(self, username: str, email: str, notificationPreferences: NotificationPreferences):
        self.username = username    # public
        self.email = email      # public
        self.notificationPreferences = notificationPreferences  # public