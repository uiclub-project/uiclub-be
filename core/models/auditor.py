from django.db import models



class Auditor(models.Model):
  """
  Abstract class to generate audit fields.
  """

  date_created = models.DateTimeField(
    auto_now_add=True, help_text="date created"
  )
  date_updated = models.DateTimeField(
    null=True, auto_now=True, help_text="date updated"
  )
  date_deleted = models.DateTimeField(
    help_text="date deleted", null=True, blank=True
  )
  state = models.BooleanField(default=True, help_text="status")


  class Meta:
    abstract = True
    ordering = ["-date_created"]


  def __str__(self):
    return "{}".format(self.pk)
