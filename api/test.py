try:
    from app import app
    import unittest
    
except Exception as e:
    print(e)
    
class apptest(unittest.TestCase):
    
    #Check for response 200
    def test(self):
        tester = app.test_client(self)
        response = tester.post("http://127.0.0.1:5000/post_numbers",json={ "num1": "23", "num2": "3"})
        self.assertEqual(response.status_code,200)
        
    def test1(self):
        tester = app.test_client(self)
        response = tester.post("http://127.0.0.1:5000/post_numbers",json={ "num": "3", "num2": "9"})
        self.assertNotEqual(response.status_code,)
        
        
    def test_content(self):
        tester = app.test_client(self)
        response = tester.post("http://127.0.0.1:5000/post_numbers",json={ "num1": "2", "num2": "0"})

        self.assertEqual(response.content_type, "application/json")

if __name__ == "__main__":
    unittest.main()
