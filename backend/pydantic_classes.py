from datetime import datetime, date, time
from typing import Any, List, Optional, Union, Set
from enum import Enum
from pydantic import BaseModel, field_validator


############################################
# Enumerations are defined here
############################################

############################################
# Classes are defined here
############################################
class UserCreate(BaseModel):
    role: str
    appointment: int  # 1:1 Relationship (mandatory)


class AvailabilityCreate(BaseModel):
    date: date
    status: str
    endHour: int
    startHour: int
    blocksOrAllows: Optional[List[int]] = None  # 1:N Relationship


class AppointmentCreate(BaseModel):
    duration: int
    startTime: date
    email: str
    clientName: str
    endTime: date
    availability: int  # N:1 Relationship (mandatory)
    bookedBy: int  # 1:1 Relationship (mandatory)


