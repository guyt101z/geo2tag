import threading
from job import Job

OPEN_DATA_URL = 'openDataUrl'


class GeocodingJob(Job):

    def internalStart(self):
        thread = threading.Thread(
            target=self.backgroundFunction,
            args=(
                self,
                self.channelName,
                self.serviceName
            )
        )
        self.thread = thread
        thread.start()

    def internalStop(self):
        self.thread.join()

    def describe(self):
        ancestorResult = Job.describe(self)
        ancestorResult.pop(OPEN_DATA_URL)
        return ancestorResult
