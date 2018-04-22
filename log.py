

class Log:

    HIDE_ALL = False
    SHOW_FATAL = True
    SHOW_ERROR = True
    SHOW_WARNING = True
    SHOW_DEBUG = True
    SHOW_COMMENT = True

    @classmethod
    def set_level(cls, lvl):
        """
        lvl is either :
           - 'none'
           - 'fatal',
           - 'error',
           - 'warning',
           - 'debug',
           - or 'comment'.
        """
        if lvl == 'none':
            Log.HIDE_ALL = True
        else:
            Log.HIDE_ALL = True

            Log.SHOW_FATAL = True
            Log.SHOW_ERROR = not(lvl == 'fatal')
            Log.SHOW_WARNING = lvl in ['warning', 'debug', 'comment']
            Log.SHOW_DEBUG = lvl in ['debug', 'comment']
            Log.SHOW_COMMENT = lvl == 'comment'

    @classmethod
    def print(cls, msg):
        display = not Log.HIDE_ALL
        if display:
            print(msg)

    @classmethod
    def get_msg(cls, msg, tag=''):
        return '[{}] {}'.format(tag, msg)

    @classmethod
    def fatal(cls, msg):
        if Log.SHOW_FATAL:
            print(cls.get_msg(msg, 'FATAL'))

    @classmethod
    def error(cls, msg):
        if Log.SHOW_ERROR:
            print(cls.get_msg(msg, 'ERROR'))

    @classmethod
    def warning(cls, msg):
        if Log.SHOW_WARNING:
            print(cls.get_msg(msg, 'WARNING'))

    @classmethod
    def debug(cls, msg):
        if Log.SHOW_DEBUG:
            print(cls.get_msg(msg, 'DEBUG'))

    @classmethod
    def comment(cls, msg):
        if Log.SHOW_COMMENT:
            print(cls.get_msg(msg, 'COMMENT'))

