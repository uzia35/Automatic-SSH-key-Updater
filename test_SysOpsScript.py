import unittest,sys,SysOpsScript,os

class TestSysOpsMethods(unittest.TestCase):

	def test_valid_ip4_addrp(self):
		counter = 0 
		for line in sys.stdin:
			ip = re.sub('/s+','',line.strip('\n\r'))
			if counter == 1 or counter == 4 or counter == 0:
				self.assertFalse(SysOpsScript.valid_ip4_addr(ip))
			else:
				self.assertTrue(valid_ip4_addr(ip))

	def test_valid_permission(self):
		key = "bad_permissions.pub"
		keyPathLocal = os.path.abspath(key)
		self.assertFalse(SysOpsScript.valid_permission(key,keyPathLocal))
		key = "authorized_key_exercise.pub"
		keyPathLocal = os.path.abspath(key)
		self.assertTrue(SysOpsScript.valid_permission(key,keyPathLocal))

if __name__ == '__main__':
    unittest.main()