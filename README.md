pygettext_template
==================

Sample of using python gettext module for i18n


1. Creating a messages template 
==================

Let's say we are want to add i18n for our 'test' module.
To retrieve all the messages marked by _() call from module we should run 'pygettext test'. 
As result we'll have a messages.pot https://github.com/alrusdi/pygettext_template/blob/master/test/locale/messages.pot -
it is an untranslated dictionary containing pairs of untranslated strings (msgid) and
placeholder for future translation of this string (msgstr)



2. Making translation
==================

For each languages we want to support we should create in any place in filesystem reachable 
by our application (test/locale in my case) a set of folders containing translated .po files.
.po files created by just renaming messages.pot to <somewhat>.po and translating all msgids.

For example in our test application we want to support a Spanish translation. So we are created in test/locale directory
a folder es/LC_MESSAGES which is contains test.po file https://github.com/alrusdi/pygettext_template/blob/master/test/locale/es/LC_MESSAGES/test.po



3. Compilling messages
==================

At last stage we are compiling our .po files to internal gettext format by msgfmt command
msgfmt test.po -o test.mo
After this translation is ready to use in application as shown in https://github.com/alrusdi/pygettext_template/blob/master/test/test.py
