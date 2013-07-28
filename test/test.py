import gettext
lang = gettext.translation('test', './locale', languages=['es'])
lang.install(unicode=True)

_ = lambda t: lang.ugettext(t)

print _('Hello world')


