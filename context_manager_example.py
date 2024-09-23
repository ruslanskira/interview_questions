# # Example 1.

# import unittest

# class MyContextManager:
#     def __enter__(self):
#         print("Entering the context")
#         # Any initialization code can be added here
#         return self

#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting the context")
#         # Any cleanup code can be added here

# class TestContextManager(unittest.TestCase):
#     def test_context_manager(self):
#         with MyContextManager() as e:
#             self.assertIsInstance(e, MyContextManager)
#             print("Inside the context")
        
#         # After exiting the context
#         print("Outside the context")

# if __name__ == "__main__":
#     unittest.main()
    
# Example 2.
import unittest
from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        yield file
    finally:
        file.close()

class TestContextManager(unittest.TestCase):
    def test_context_manager(self):
        with open_file("test.txt", "w") as file:
            file.write("Hello, World!")

        with open_file("test.txt", "r") as file:
            content = file.read()
            self.assertEqual(content, "Hello, World!")

if __name__ == "__main__":
    unittest.main()