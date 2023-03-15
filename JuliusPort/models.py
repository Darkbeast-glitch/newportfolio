from django.db import models

# Create your models here.


class Blog(models.Model):
    blog_head = models.CharField(max_length=900, blank=True, null=True)
    like_number = models.IntegerField()
    message_number = models.IntegerField()
    blog_post = models.CharField(max_length=40000, blank=True, null=True)
    blog_image = models.ImageField(upload_to="images/")
    admin_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.admin_name

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    # class Meta:


class ContactMe(models.Model):
    fullname = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self) -> str:
        return self.fullname

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
