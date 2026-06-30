from pydantic import BaseModel
from typing import Optional, List


class TaskCreate(BaseModel):
    content: str 
    description: Optional[str] = None 



class TaskUpdate(BaseModel):
    content: Optional[str] = None       
    description: Optional[str] = None 
    labels: Optional[List[str]] = None  
    priority: Optional[int] = None     
    
    due_string: Optional[str] = None     
    due_date: Optional[str] = None       
    due_datetime: Optional[str] = None    
    due_lang: Optional[str] = None      
    
    assignee_id: Optional[str] = None    
    child_order: Optional[int] = None     
    is_collapsed: Optional[bool] = None  
    day_order: Optional[int] = None
    
    duration: Optional[int] = None 
    duration_unit: Optional[str] = None  
    deadline_date: Optional[str] = None
    


class TaskMove(BaseModel):
    project_id: Optional[str] = None 
    section_id: Optional[str] = None 
    parent_id: Optional[str] = None 