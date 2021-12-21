### Sukodu Solver project Requirement
  - Docker
  - Docker Compose
  - Python 3

### Docker
  - docker-compose --build
  - docker-compose up --remove-orphans
  - docker-compose stop (stops the cointainer)
  - docker-compose down (destroys the cointainer)
  - navigate to http://0.0.0.0:5555/ to check a Flower Dashboard

### API usage
  - Argument should be in a specific format: 
      {
        "grid": [[2,5,0,0,3,0,9,0,1],[0,1,0,0,0,4,0,0,0],[4,0,7,0,0,0,2,0,8],[0,0,5,2,0,0,0,0,0],[0,0,0,0,9,8,1,0,0],
        [0,4,0,0,0,3,0,0,0],[0,0,0,3,6,0,0,7,2],[0,7,0,0,0,0,0,0,3],[9,0,3,0,0,0,0,0,4]]
      } 
  - Each array represents exactly one row of a sudoku grid by order
  - Argument Exmaple for "/status/<task_id>" - endpoint (supports only GET method):
    type a task id to check the reseult (http://0.0.0.0:5000/status/def76ecf-74a2-4241-891d-5fafdeb6778f)

### URLS
  - "/" (Takes a nested arrays of sudoku puzzle numbers and returns a task id)
  - "/status/<task_id>" (returns the result of a specific task)