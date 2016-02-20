__module_name__ = "testy" 
__module_version__ = "1.0" 
__module_description__ = "Benchmark the gigglehertz of your hexchat" 
 
import xchat, time

def testy(word, wordl, ud):
    count=0
    t = time.time() + 1
    while time.time() <= t:
        count += 1
    xchat.command("MSG %s My silly computer can inc a variable %s times in %s ms ;(" % (xchat.get_info("channel"), count, 1000 * (1 - 
time.time() + t)))
    return xchat.EAT_ALL

xchat.hook_command("testy", testy, help="lol")