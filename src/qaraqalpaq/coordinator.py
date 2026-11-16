from __future__ import annotations

import threading
import uuid

from .models import TaskBudget, TaskContext


class TaskCancelled(RuntimeError):
    pass


class TaskCoordinator:
    """Small bounded request coordinator; it does not execute external actions."""

    def __init__(self, budget: TaskBudget | None = None) -> None:
        self.budget = budget or TaskBudget()
        self._cancelled: set[str] = set()
        self._lock = threading.Lock()

    def begin(self) -> TaskContext:
        return TaskContext(task_id=str(uuid.uuid4()), budget=self.budget)

    def cancel(self, task_id: str) -> None:
        with self._lock:
            self._cancelled.add(task_id)

    def check(self, context: TaskContext, *, steps: int = 1) -> None:
        if steps > context.budget.max_steps:
            raise ValueError("task step budget exceeded")
        with self._lock:
            if context.task_id in self._cancelled:
                raise TaskCancelled("task was cancelled")
