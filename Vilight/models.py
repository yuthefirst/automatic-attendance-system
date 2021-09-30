from django.db import models

# Create your models here.

class Attendant(models.Model):
    confirm = (
        ('Đã xử lý','Đã xử lý'),
        ('Chưa hợp lệ', 'Chưa hợp lệ'),
    )
    date = models.CharField(max_length=255, null=True)
    month = models.CharField(max_length= 255, null = True)
    staff_id = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255, null=True)
    checkin = models.CharField(max_length=255, null=True)
    checkmid = models.CharField(max_length=255, null=True)
    checkout = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255, null=True)
    admin_comment = models.CharField(max_length=255, null=True, choices=confirm)

    def __str__(self):
        return self.staff_id + " - " + self.date

class Axxxx(models.Model): #Model này sau khi add vào database admin sẽ được chỉnh sửa
    date = models.CharField(max_length=255, null=True)
    staff_id = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.staff_id