**Requirements**: - Docker compose

- Run config file:

  ```bash
  docker compose -f docker-compose.local.yaml up -d
  ```

- Go inside container:

  ```bash
    docker compose -f docker-compose.local.yaml exec network_analysis bash
  ```

  We are located in the directory /app

- Run script:

  ```bash
      Ex:

      python -m task_1.task1

      or

      python -m task_2.task2
  ```
