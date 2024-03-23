# import create app 

from website import create_app

app = create_app()

if __name__ == '__main__':              #only if this file is ran
#   run flask application, start up the webserver and reruns webserver 
    app.run(debug=True)   

    
