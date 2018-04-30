class TreeNode:
	def __init__(self,n):
		self.val=n
		self.left=None
		self.right=None
class bin_tree():
	def __init__(self):
		self.root=None
	
	def ins_bin(self,n):
		#n = TreeNode(n)		
		if (self.root is None ):
			self.root=TreeNode(n)
			return
			
		l=[]
		l.append(self.root)
		while(True):
			self.temp=l.pop(0)
			if(self.temp.left is None):
				self.temp.left=TreeNode(n)
				return
			else :
				l.append(self.temp.left)
			if(self.temp.right is None):
				self.temp.right=TreeNode(n)
				return
			else:	
				l.append(self.temp.right)	

	def _inshow(self,n):
		if(n is not None):
			self._inshow(n.left)
			print(n.val,end=' ')
			self._inshow(n.right)
	
	def inshow(self):
		self._inshow(self.root)
		print()
	

	def _ispath(self,nod,n):
			if(n-nod.val == 0 and nod.left is None and nod.right is None):
				return True
						
			b=False			
			if(nod.left is not None):
				b=b or self._ispath(nod.left,n-nod.val)
			if(nod.right is not None):				
				b=b or self._ispath(nod.right,n-nod.val)
			return b 

	def ispath(self, n):
		if (self.root is None):
			return False		
		return False or self._ispath(self.root,n)	
					
b=bin_tree()
b.ins_bin(1)
b.ins_bin(2)
b.ins_bin(3)
b.ins_bin(4)
b.ins_bin(5)
b.ins_bin(6)
b.inshow()
print(b.ispath(10))
