import enum
from typing import List as List_, Optional as Optional_
from sqlalchemy import (
    create_engine, Column as Column_, ForeignKey as ForeignKey_, Table as Table_, 
    Text as Text_, Boolean as Boolean_, String as String_, Date as Date_, 
    Time as Time_, DateTime as DateTime_, Float as Float_, Integer as Integer_, Enum
)
from sqlalchemy.orm import (
    column_property, DeclarativeBase, Mapped as Mapped_, mapped_column, relationship
)
from datetime import datetime as dt_datetime, time as dt_time, date as dt_date

class Base(DeclarativeBase):
    pass



# Tables definition for many-to-many relationships

# Tables definition
class User(Base):
    __tablename__ = "user"
    id: Mapped_[int] = mapped_column(primary_key=True)
    role: Mapped_[str] = mapped_column(String_(100))

class Availability(Base):
    __tablename__ = "availability"
    id: Mapped_[int] = mapped_column(primary_key=True)
    date: Mapped_[dt_date] = mapped_column(Date_)
    startHour: Mapped_[int] = mapped_column(Integer_)
    endHour: Mapped_[int] = mapped_column(Integer_)
    status: Mapped_[str] = mapped_column(String_(100))

class Appointment(Base):
    __tablename__ = "appointment"
    id: Mapped_[int] = mapped_column(primary_key=True)
    clientName: Mapped_[str] = mapped_column(String_(100))
    email: Mapped_[str] = mapped_column(String_(100))
    startTime: Mapped_[dt_date] = mapped_column(Date_)
    endTime: Mapped_[dt_date] = mapped_column(Date_)
    duration: Mapped_[int] = mapped_column(Integer_)
    availability_id: Mapped_[int] = mapped_column(ForeignKey_("availability.id"))
    bookedBy_id: Mapped_[int] = mapped_column(ForeignKey_("user.id"), unique=True)


#--- Relationships of the user table
User.appointment: Mapped_["Appointment"] = relationship("Appointment", back_populates="bookedBy", foreign_keys=[Appointment.bookedBy_id])

#--- Relationships of the availability table
Availability.blocksOrAllows: Mapped_[List_["Appointment"]] = relationship("Appointment", back_populates="availability", foreign_keys=[Appointment.availability_id])

#--- Relationships of the appointment table
Appointment.availability: Mapped_["Availability"] = relationship("Availability", back_populates="blocksOrAllows", foreign_keys=[Appointment.availability_id])
Appointment.bookedBy: Mapped_["User"] = relationship("User", back_populates="appointment", foreign_keys=[Appointment.bookedBy_id])

# Database connection
DATABASE_URL = "sqlite:///Class_Diagram.db"  # SQLite connection
engine = create_engine(DATABASE_URL, echo=True)

# Create tables in the database
Base.metadata.create_all(engine, checkfirst=True)