__module_name__ = "Services Notices" 
__module_version__ = "1.1" 
__module_description__ = "Take over handling of notices and send those from *@services.* to active window" 
 
import hexchat
# :bots.phuzion.net NOTICE * :*** Notice -- SETTIME from services.phuzion.net, clock is set 0 seconds backwards
# :ChanServ!ChanServ@services.phuzion.net NOTICE knivey :knivey is gleaming (IRC operator).
def Hnotices(word, word_eol, userdata):

	if word[0] == None or '!' not in word[0]:
		return hexchat.EAT_NONE
	nick,host = word[0].split('!', 1)
	nick = nick[1:]
	message = word_eol[3][1:]
	if "@services." in host.lower() and word[2][0] != '#':
		cur_id = hexchat.get_prefs("id")
		context = hexchat.find_context();
		for chan in hexchat.get_list('channels'):
			if chan.id == cur_id and chan.context == context:
				context.emit_print("Notice",nick,message);
				return hexchat.EAT_ALL
	return hexchat.EAT_NONE

hexchat.hook_server("NOTICE", Hnotices)
