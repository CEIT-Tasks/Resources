class Error:
  def __init__(self, message):
    self.message = message

  def handle(self, *args, **kwargs):
    print(f"Error: {self.message}")

class FileError(Error):
  def handle(self, filename=None):
    if filename:
      print(f"FileError: {self.message} (File: {filename})")
    else:
      print(f"FileError: {self.message}")


class NetworkError(Error):
  def __init__(self, message, code=None):
    super().__init__(message)
    self.code = code

  def handle(self, url=None):
    if url and self.code:
      print(f"NetworkError: {self.message} (URL: {url}, Code: {self.code})")
    elif self.code:
      print(f"NetworkError: {self.message} (Code: {self.code})")
    else:
      print(f"NetworkError: {self.message}")