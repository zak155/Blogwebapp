from django.db import models

# Create your models here.
class About(models.Model):
    about_heading=models.CharField(max_length=25)
    about_description=models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        
        verbose_name_plural = "About"

    def _str_(self):
        return self.about_heading
class Social_Link(models.Model):
      platform=models.CharField(max_length=25)
      link=models.URLField(max_length=255)
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)

      def _str_(self):
            return self.platform
      