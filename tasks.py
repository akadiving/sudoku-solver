from celery import Celery
from puzzle import Puzzle
import os

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379")

@celery.task
def solve_puzzle(*grid):
    new_puzzle = Puzzle(grid)
    return new_puzzle.final_answer()