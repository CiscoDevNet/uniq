"""
Copyright 2016 Cisco Systems

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

try:
    from uniq.common import logger
except:
    import logging
    logger = logging.getLogger("uniq")


class Services(object):
    """ Services base class"""

    TASK_DEFAULT_TIMEOUT = 60  # seconds

    def __init__(self, base, *args, **kwargs):
        """ Initializer makes available the nb_api client and logger to objects of this class. """

        super(Services, self).__init__(*args, **kwargs)

        self.log = logger.log

    def serialize(self, model):
        """ Serializes any service's model object into dictionary.

        Args:
            model (swagger model object): object of swagger model class

        Returns:
            a serialized dict of the swagger model object
        """

        self.log.info("Serializing swagger model: {0}".format(model.__class__.__name__))
        return self.nb_api.serialize(model)

    def handle_task(self, task, task_status=None, timeout=TASK_DEFAULT_TIMEOUT):
        """ Returns the task response for a task on completion

        By default it will only wait for the task to complete, it can be made to wait for a
        particular state (Success/Failre), depending on the argument value of task_status.

        Args:
            task (task model object): an object of the task response
            task_status (str): task status to  wait for (Success/Failure). Default is None
            timeout (int): timeout in seconds.
        """

        if task_status:
            if task_status.lower() == "success":
                return self.nb_api.task_util.wait_for_task_success(task, timeout)
            elif task_status.lower() == "failure":
                return self.nb_api.task_util.wait_for_task_failure(task, timeout)

        return self.nb_api.task_util.wait_for_task_complete(task, timeout)
