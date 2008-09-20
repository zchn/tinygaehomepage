import  wsgiref.handlers 
 
import  Pyblosxom.pyblosxom 
from  google.appengine.ext  import  webapp 

def  main(): 
    application  =  Pyblosxom.pyblosxom.PyBlosxomWSGIApp()
    wsgiref.handlers.CGIHandler().run(application)
 
if  __name__  ==  '__main__': 
     main()
