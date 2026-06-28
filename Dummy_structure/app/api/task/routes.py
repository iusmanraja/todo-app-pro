import os
import requests
from fastapi import APIRouter, HTTPException
from .schemas import TaskCreate, TaskUpdate

from .schemas import TaskCreate, TaskUpdate

router = APIRouter()

@router.post("/tasks")
def create_task(task_data: TaskCreate):
    token = os.getenv("TODOIST_API_TOKEN")
    if not token:
        raise HTTPException(status_code=500, detail="Todoist API token is not set.")

    url = "https://api.todoist.com/api/v1/tasks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": task_data.content,
        "description": task_data.description
    }
    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code not in [200, 201]:
            try:
                error_detail = response.json()
            except Exception:
                error_detail = response.text
            raise HTTPException(status_code=response.status_code, detail=error_detail)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Todoist: {str(e)}")
    


@router.post("/tasks/{task_id}")
def update_task(task_id: str, task_data: TaskUpdate):
    token = os.getenv("TODOIST_API_TOKEN")
    
    if not token:
        raise HTTPException(status_code=500, detail="Todoist API token is not set.")
        
    url = f"https://api.todoist.com/api/v1/tasks/{task_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    payload = task_data.model_dump(exclude_unset=True)
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail=f"Task with ID {task_id} not found.")
            
        if response.status_code not in [200, 201]:
            try:
                error_detail = response.json()
            except Exception:
                error_detail = response.text
            raise HTTPException(status_code=response.status_code, detail=error_detail)
            
        return response.json()
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Todoist: {str(e)}")
    

    
@router.delete("/tasks/{task_id}")
def Delete_Post(task_id: str):
    token= os.getenv("TODOIST_API_TOKEN")

    if not token:
        raise HTTPException(status_code=500, detail="Todoist API token is not set.")
    
    url = f"https://api.todoist.com/api/v1/tasks/{task_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.delete(url, headers=headers)
        
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Task not found")
        
        if response.status_code == 403:
            raise HTTPException(status_code=403, detail="You do not have permission to delete this task.")
            
        if response.status_code not in [200, 204]:
            try:
                error_detail = response.json()
            except Exception:
                error_detail = response.text
            raise HTTPException(status_code=response.status_code, detail=error_detail)
        
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Todoist: {str(e)}")
    