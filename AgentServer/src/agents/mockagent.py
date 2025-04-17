from datetime import date 


class MockAgent():
  """_summary_
  
  Class for mocking any agent to be used in tests.
  """

  def __init__(self):
    pass

  def mock_task1(self, message: str):
    return {'User Message': f'Task 1 print the user message: {message}'}
  
  def mock_task2(self):
    return date.today()
