
class KeyNotExistingException:
    def __init__(self, msg=None, form=None):
        if form is not None:
            msg = u''
            for k in form.errors.keys():
                for e in form.errors[k]:
                    msg += u' ' + e
            self.msg = e
        else:
            self.msg = u'%s' % msg