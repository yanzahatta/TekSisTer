
# coding: utf-8

# In[4]:


from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(('localhost',8888), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile='cert.pem', keyfile='key.pem')
httpd.serve_forever()

