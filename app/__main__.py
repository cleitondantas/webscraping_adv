"""RUN APP"""
from app import create_app



if __name__ == '__main__':
   print("inicializando")
   app = create_app()
   app.run(host="0.0.0.0",port=8080, debug=True)