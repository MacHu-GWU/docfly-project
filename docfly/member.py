#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import OrderedDict
import site
import os

_root_dir = site.getsitepackages()[1]

class Package():
	"""Python中包的抽象类。
	"""
	def __init__(self, name, parent=None):	
		self.name = name
		self.parent = parent
		self.subpackage = OrderedDict()
		self.module = OrderedDict()
		
		if self.parent:
			package_dir = os.path.join(
				*([_root_dir,] + self.parent.split(".") + [self.name,])
				)
		else:
			package_dir = os.path.join(
				*[_root_dir, self.name]
				)

		for basename in os.listdir(package_dir):
			abspath = os.path.join(package_dir, basename)
			# 如果是一个目录, 检查是否有__init__.py文件
			if os.path.isdir(abspath):
				# 若是一个包, 则在该目录下生成一个子包对象
				if os.path.exists(os.path.join(abspath, "__init__.py")):
					self.subpackage[basename] = Package(basename, self.fullname)
			# 如果是一个文件, 检查是否是.py文件
			else:
				fname, ext = os.path.splitext(basename)
				# 若是一个模组, 则生成一个模组对象
				if (ext == ".py") and (fname != "__init__"):
					self.module[fname] = Module(fname, self.fullname)
					
	@property
	def fullname(self):
		"""返回包的全名。
		
		全名 = 母包名.包名
		"""
		if self.parent:
			return "%s.%s" % (self.parent, self.name)
		else:
			return self.name
	
	def __str__(self):
		return ("Package(package name = '{0}' subpackage = {1} "
				"module = {2})").format(
					self.fullname, list(self.subpackage), list(self.module)
					)
	
	def __repr__(self):
		return self.name
	
	def __getitem__(self, key):
		try:
			return self.subpackage[key]
		except:
			try:
				return self.module[key]
			except:
				raise Exception("get key error")
	
	def show(self, indent=0):
		"""打印包组织结构的树状图。
		"""
		def pad_text(indent):
			return "    " * indent + "|---"
		
		print("%s%s" % (pad_text(indent), self.fullname))
		print("%s%s" % (pad_text(indent + 1), self.fullname + ".__init__.py"))
		
		indent += 1
		
		for p in self.subpackage.values():
			p.show(indent=indent)
			
		for m in self.module.values():
			print("%s%s" % (pad_text(indent), m.fullname + ".py"))
	
	def walk(self):
		"""一个迭代循环器, 返回:
		
		1. 包对象
		2. 当前包对象的全名
		3. 所有子包
		4. 所有模块
		"""
		yield (self,
			self.fullname, 
			list(self.subpackage.values()), 
			list(self.module.values()),
			)
		for p in self.subpackage.values():
			for current_package, current_fullname, packages, modules in p.walk():
				yield (current_package, current_fullname, packages, modules)
			
class Module():
	"""Python中模块的抽象类。
	"""
	def __init__(self, name, parent=None):
		self.name = name
		self.parent = parent

	@property
	def fullname(self):
		"""返回模组的全名。
		
		全名 = 母包名.模组名
		"""
		if self.parent:
			return "%s.%s" % (self.parent, self.name)
		else:
			return self.name

	def __str__(self):
		return "module name = '%s'" % self.fullname

	def __repr__(self):
		return self.name
	
if __name__ == "__main__":
	from pprint import pprint as ppt
	p = Package("requests")
# 	p.show()
# 	print(p["packages"])
# 	for t in p.walk():
# 		print(t)
