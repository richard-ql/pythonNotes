import time
import hmac
import hashlib

def jiami_md5(src):
    m = hashlib.md5()
    m.update(src.encode("utf-8"))
    return m.hexdigest()

timestamp = int(time.time())

# hmac_sha256加密
appkey = "需要申请"
strToSign = "根据文档规则生成"
signature = hmac.new(bytes(appkey, encoding="utf-8"), bytes(strToSign, encoding="utf-8"), digestmod=hashlib.sha256).hexdigest()
low_sig = signature.lower()


