import base64
import hashlib

class Read(object):
    # 请求body加密
    def base64_code(self,date):
        self.b =base64.b64encode(date.encode('utf-8')).decode('utf-8')
        return self.b

    # 请求体摘要
    def sha256_code(self,date,appid):
        self.h=hashlib.sha256((date+appid).encode('utf-8')).hexdigest()
        return self.h



if __name__ == '__main__':
    er = Read()
    d = "{'queryCond':[{'tranDate':'2019-07-24','srcNo':'10501543817831589019'}]}"
    dd =er.base64_code(d)
    print(dd)
    appid ="N100703-L00801"
    ddd = er.sha256_code(d,appid)
    print(ddd)