class InvalidMarkError(Exception):
    def __init__(self,message="Mark must be between 0 and 100"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
    
    
def check_marks():
    mark = int(input())
    if mark < 0 or mark > 100:
        raise InvalidMarkError()
    else:
        print("Valid mark:", mark)

try:
    check_marks()
except InvalidMarkError as e:
    print("Caught:", e)
