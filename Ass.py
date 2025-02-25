Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
Ans:By default, Django signals execute synchronously, meaning they run in the same execution flow as the caller.

code:
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a delay
    print("Signal handler finished")

# Simulating a User save operation
user = User(username="test_user")
user.save()
print("User save operation completed")





Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
Ans:Yes, by default, Django signals run in the same thread as the caller.

code:
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal is running in thread: {threading.current_thread().name}")

# Simulating a User save operation
print(f"Caller is in thread: {threading.current_thread().name}")
user = User(username="test_user")
user.save()





Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
Ans:By default, Django signals run in the same database transaction as the caller. However, post_save runs after the transaction is committed, while pre_save runs within the transaction.

code:
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Inside signal: Transaction active? {transaction.get_autocommit()}")

# Simulating a User save operation inside a transaction
with transaction.atomic():
    user = User(username="test_user")
    user.save()
    print(f"Inside transaction block: Transaction active? {transaction.get_autocommit()}")






Description: You are tasked with creating a Rectangle class with the following requirements:

1.An instance of the Rectangle class requires length:int and width:int to be initialized.
2.We can iterate over an instance of the Rectangle class 
3.When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

code:
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}

# Usage Example:
rect = Rectangle(10, 5)

for item in rect:
    print(item)


