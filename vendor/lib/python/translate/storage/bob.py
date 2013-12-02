from translate.storage import po

pofile = po.pofile.parsefile("quot_escape_wrapping.dtd.po")
pofile.savefile("quot_escape_wrapping2.dtd.po")
