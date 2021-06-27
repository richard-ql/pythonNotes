# 参考文档：https://www.cnblogs.com/crazyrunning/p/7095014.html
# https://www.cnblogs.com/miyauchi-renge/p/10922092.html
class Minix1:
	"""该混合类为header列表末尾添加data1"""
	def get_header(self):
		print('run Minix1.get_header')
		ctx = super().get_header()
		ctx.append('data1')
		return ctx

class Minix2:
	"""该混合类为header列表头部添加data2"""
	def get_header(self):
		print('run Minix2.get_header')
		ctx = super().get_header()
		ctx.insert(0, 'data2')
		return ctx

class Header:
	header = []
	def get_header(self):
		print('run Headers.get_header')
		return self.header if self.header else []


class Final(Minix1, Minix2, Header):

	def get_header(self):
		return super().get_header()

print(Final.mro())
#[Final, Minix1, Minix2, Header, object]
header = Final().get_header()
#run Minix1.get_header
#run Minix2.get_header
#run Headers.get_header
print(header)
#['data2', 'data1']