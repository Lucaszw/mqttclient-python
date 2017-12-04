import re

def add_subscription(self, channel, method):
    route = self.router.addRoute(channel, method)
    # print route:
    subscription = re.sub(r"\{(.+?)\}", "+", channel)
    

    if (not this.connected):
        print f'{this.name} :: Cannot add subscription. Client is not connected'
    