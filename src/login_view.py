from user_profile import UserProfile

class LoginView:
    def registerUser(self, userProfile: UserProfile, password: str):
        pass

    def displayError(self, message: str):
        pass

    def transitionToHomeView(self, userProfile: UserProfile):
        pass

    # UI readers:
    def readUsernameTextbox(self):
        pass

    def readPasswordTextbox(self):
        pass

    def readEmailTextbox(self):
        pass

    def readNotificationPreferences(self):
        pass