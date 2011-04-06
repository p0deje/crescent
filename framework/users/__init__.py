from ConfigParser import RawConfigParser

class Users:
    """Parses users.conf file and gets all users' information.
    Provides tests with users property and get_user() method."""
    def __init__(self):
        # initiate empty dictionary of users
        self._users = {}
        # parse users file
        self._settings = RawConfigParser()
        file = open('framework/users/users.cfg')
        self._settings.readfp(file)
        # parse sections of users file
        for section in self._settings.sections():
            # transform section to lower-case for readability
            role = section.lower()
            self._users[role] = {}
            # parse options in sections
            for option in self._settings.options(section):
                # transform option to lower-case for readability
                info = option.lower()
                # write to users dictionary
                self._users[role][info] = self._settings.get(section, option)

    @property
    def users(self):
        """Returns dictionary of users keyed by users.conf section name."""
        return self._users

    def get_user(self, role):
        """Returns dictionary of user's information by user's role."""
        return self._users[role]
