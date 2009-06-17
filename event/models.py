from django.db import models

# Create your models here.

class Event(models.Model) :
    day = models.DateField()
    title = models.CharField(max_length=32)

    @models.permalink
    def get_absolute_url() :
        return ('event', None, {'object_id' : self.id})
    
    def __unicode__(self):
        return u"%s" % self.title
    
    class Meta:
        ordering = ['-day']
 