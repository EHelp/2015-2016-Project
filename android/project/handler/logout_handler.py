from handler import base_handler

class LogoutHandler(base_handler.BaseHandler):
    def get(self):
        self.clear_cookie("username")
        self.clear_cookie("id")
        self.clear_cookie("passwordVerify")
        self.redirect("/account/login")

    def post(self):
	    if (self.get_argument("logout", None)):
	        self.clear_cookie("username")
        	self.redirect("/account/login")