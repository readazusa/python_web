# -*- coding: utf-8 -*-
from flask import  Flask,request;
import logging;
app=Flask(__name__);

@app.route("/hello")
def hello():
    print(request.method);
    logging.debug("接收了一个请求");
    return "你好55555";

@app.route("/word/<value>")
def word(value):
    return "你输入的额内容: "+str(value);

@app.route("/projects/")
def projects():
    return "访问了projects";

@app.route("/")
def index():
    pass;






if __name__ =="__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='d:/myapp.log')
    logging.info("准备开始一个应用");
    print("运行第一个web项目success");
    app.run(host='0.0.0.0');   #任何网络通的地方都可以访问
