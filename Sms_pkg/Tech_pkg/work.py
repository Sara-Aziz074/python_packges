def tech_work():
    print("Tech Package --> Work Module")
    print("tech_work Function")
    print()

    
from User_pkg import request
request.user_request()
# directly fun call
from User_pkg.request import user_request
user_request()

