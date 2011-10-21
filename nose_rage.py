
import nose.core
from nose.plugins import Plugin
from nose.result import TextTestResult

class NoseRage(Plugin):
    name = 'NoseRage'

    def options(self, parser, env):
        env_opt = 'NOSE_RAGE'
        parser.add_option('--rage', action='store_true',
                          dest='rage', default=env.get(env_opt, False),
                          help="Implements PEP712. Displays FFFFFFFUUUU for errors.")

    def configure(self, options, conf):
        rage = getattr(options, 'rage', False)
        if rage:
            self.enabled = True
            nose.core.TextTestResult = RageTextResult


class RageTextResult(TextTestResult):
    def __init__(self, *args,**kw):
        super(RageTextResult, self).__init__(*args,**kw)
        self.error_count = 0

    def printLabel(self, label, err=None):
        call_orig = True
        stream = getattr(self, 'stream', None)
        if self.stream is not None:
            if self.dots:
                call_orig = False
                if label == 'ERROR':
                    self.error_count += 1
                    if self.error_count > 7:
                        stream.write('U')
                    else:
                        stream.write('F')
                else:
                    stream.write(label[:1])
        if call_orig:
            super(RageTextResult, self).printLabel(label, err)

