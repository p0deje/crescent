from ConfigParser import RawConfigParser

class System:
    """Parses system.conf and gets server information.
    Provides tests with sut, base_url and http_auth_url properties."""
    def __init__(self):
        # parse settings file
        self._settings = RawConfigParser()
        file = open('framework/system/system.cfg')
        self._settings.readfp(file)
        # get system under test information
        self._sut = self._settings.get('System', 'Name')
        # get Selenium RC configuration
        self._selenium_conf = {}
        for conf in self._settings.options('Selenium'):
            self._selenium_conf[conf] = self._settings.get('Selenium', conf) 
        # get server information
        self._protocol = self._settings.get('Server', 'Protocol')
        self._hostname = self._settings.get('Server', 'Hostname')
        self._port = self._settings.get('Server', 'Port')
        # get HTTP authorization information
        self._http_auth = {}
        self._http_auth['username'] = self._settings.get('HTTP-Auth', 'Username')
        self._http_auth['password'] = self._settings.get('HTTP-Auth', 'password')

    @property
    def sut(self):
        """Returns the name of system under test"""
        return self._sut

    @property
    def base_url(self):
        """Returns base URL of system under test.
        Note, that HTTP authorization is not included.
        Use http_auth_url instead."""
        # prepare protocol
        if self._protocol: protocol = self._protocol
        else: protocol = 'http'
        # prepare hostname
        if self._hostname: hostname = self._hostname
        else: raise (RuntimeError, 'Hostname is not definied.')
        # prepare port
        if self._port: port = int(self._port) # it's returned as a sting
        else: port = 80
        # construct URL
        url = '%s://%s' % (protocol, hostname)
        if port != 80:
            url += ':%s' % port
        return url

    @property
    def http_auth_url(self):
        """Returns URL of system under test with HTTP authorization.
        You generally need this only at first page open as long as browser
        saves HTTP authorization.
        If HTTP-Auth in settings.conf has empty Username and Password,
        returns base URL."""
        # check if HTTP authorization is set
        if self._http_auth['username'] and self._http_auth['password']:
            # prepare protocol
            if self._protocol: protocol = self._protocol
            else: protocol = 'http'
            # prepare HTTP authorization credentials
            username = self._http_auth['username']
            password = self._http_auth['password']
            # prepare hostname
            if self._hostname: hostname = self._hostname
            else: raise (RuntimeError, 'Hostname is not definied.')
            # prepare port
            if self._port: port = int(self._port) # it's returned as a sting
            else: port = 80
            # construct URL
            url = '%s://%s:%s@%s' % (protocol, username, password, hostname)
            if port != 80:
                url += ':%s' % port
            return url
        # otherwise return base URL
        else:
            return self.base_url

    @property
    def selenium_conf(self):
        """Returns the configuration of Selenium RC."""
        return self._selenium_conf
