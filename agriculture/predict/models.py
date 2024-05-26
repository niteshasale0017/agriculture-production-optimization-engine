from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    password = models.CharField(max_length=20)

    def Email_exits(self):
        if User.objects.filter(email= self.email):
            return True
        return False
    def Mobile_exits(self):
        if User.objects.filter(mobile=self.mobile):
            return True
        return False
    def Is_user_exits(self,email):
        try:
            user = User.objects.get(email=email)
            return user
        except:
            return False
