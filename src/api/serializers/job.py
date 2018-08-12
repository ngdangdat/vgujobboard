from job.models import Job

from api.serializers.base import ModelSerializer

class JobSerializer(ModelSerializer):

  class Meta:
    model = Job
