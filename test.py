try:
    from app import app
    import unittest

except Exception as e:
    print("Some modules are Missing {}".format(e))


class FT(unittest.TestCase):

     #Check if the interface status is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/web")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check information and response inside the api
    def test_index_info(self):
        tester = app.test_client(self)
        response = tester.get("/web")
        self.assertTrue(b'Emotion Detection' in response.data)

    # Checking for anger emotion when a text is inputted
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/emotion_predictor?text_message=anger")
        self.assertEqual(response.status_code, 200)
        print(response)

if __name__ == '__main__':
    unittest.main()
