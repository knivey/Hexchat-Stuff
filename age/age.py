__module_name__ = "age"
__module_version__ = "1.0"
__module_description__ = "Display your age in the active channel" 
 
import xchat, datetime
''' Set these variables to your birthday '''
YEAR  = 1970
MONTH = 1
DAY   = 1

def cmd_age(word, wordl, ud):
    woot = (datetime.datetime.today() - datetime.datetime(year=YEAR, month=MONTH, day=DAY)).days / 365.24
    xchat.command("MSG %s Age: %s" % (xchat.get_info("channel"), woot))
    return xchat.EAT_ALL

xchat.hook_command("age", cmd_age, help="Display your age in the active channel")