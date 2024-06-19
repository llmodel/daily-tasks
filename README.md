# daily-tasks
Docker project for executing daily tasks

~/projects/docker/daily_tasks folder is the root project folder and is version controled via git/github.

Source code is in the ./code directory, which is mounted on the container as /code.
Any changes in the source code, either from the host side, or the container side will be reflected on the other side.


Building the image:
```
cd ~/projects/docker/daily-tasks
docker build -t daily-tasks .
```

Running the container:
```
docker run -it -v /home/user_name/projects/docker/daily-tasks/code:/code daily-tasks bash
```
