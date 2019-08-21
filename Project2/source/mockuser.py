import mock
class MockUser:

    def __init__(self) -> None:
        super().__init__()
        print("creating Mock User")

    def mockuser(self):
        print("used mock")



handle = MockUser()
handle.mockuser()


