import pickle

d = {
    "name": "tools",
    "role": "police",
    "blood": 76,
    "weapon": "AK47"
}

d_dump = pickle.dumps(d) # 序列化
print(d_dump)
print(pickle.loads(d_dump)) # 反序列化

with open("pic.pkl", "wb") as f:
    pickle.dump(d, f)

with open("pic.pkl", "rb") as f:
    print(pickle.load(f))

# pickle vs json
# pickle 只支持python
# 支持 python里的所有数据类型
# class->object
# function
# datetime
# json 所有语言都支持
# 只支持常规数据类型 str, int, dict, set, tuple, list
