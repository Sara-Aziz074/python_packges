#import Admin_pkg.service
#pkgNam   module   function
#Admin_pkg.service.admin_service()


#import Admin_pkg.product
#pkgNam   module   function
#Admin_pkg.product.admin_product()

#import  Admin_pkg.Common_pkg.header

#Admin_pkg.Common_pkg.header.admin_common_header()

#import Admin_pkg.Common_pkg.footer



#Admin_pkg.Common_pkg.footer.admin_common_footer()

#from Admin_pkg import service

#service.admin_service()# module_name.function_name


#from Admin_pkg import product

#product.admin_product() # module_name.function_name

#from Admin_pkg.Common_pkg import header

#header.admin_common_header()# module_name.function_name

#from Admin_pkg.Common_pkg import footer

#footer.admin_common_footer()# module_name.function_name

#from Tech_pkg import profile

#profile.tech_profile()# module_name.function_name


#from Tech_pkg import work

#work.tech_work()# module_name.function_name

#from User_pkg import profile

#profile.user_profile()# module_name.function_name

#from User_pkg import request

#request.user_request()# module_name.function_name


# direct sorce

# from Package_name.module_name import function_name,vari_name etc

# function_name(), vari, class_name()
#from Admin_pkg.service import admin_service
#admin_service()


#from Admin_pkg.Common_pkg.header import admin_common_header

#admin_common_header()

#  from package_name import * error  if we not put in init__ file __all__ = [" class_name","fun_name",etc]

#from Admin_pkg import *
#product.admin_product()

#service.admin_service()

#from Admin_pkg.Common_pkg import footer, header
#header.admin_common_header()

#footer.admin_common_footer()

# for sibling pakges
# sibling pakges ko get krny ke lea cd.. parent pkg then use flag py -m Tech_pkg.work 

#py -m Tech_pkg.work 
# use hack 

# import sys
#sys.path.append("use url path's of parent_pkg  ")
# import module_name
# in cmd cd module_path py module_name.py
import Admin_pkg.product
Admin_pkg.product.admin_product()
