from django.db import models
from django.utils.text import slugify
from accounts.models import CustomUser
import uuid

class Ticket(models.Model):
    """
    Defines a ticket model
    """
    STATUS = (
        ('open', 'open'),
        ('pending', 'pending'),
        ('closed', 'closed'),
    )
    ticket_id = models.UUIDField(default=uuid.uuid4)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS, default='open')
    attachments = models.ImageField(null=True, upload_to='attachments/')
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_by')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_to')
    accepted_on = models.DateTimeField(null=True, blank=True)
    closed_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        """
        This method makes the title of the ticket the slug
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representaion for the ticket class on the admin pannel
        """
        # TODO: add the name of the client as well
        return self.title
    