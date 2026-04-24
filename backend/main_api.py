import uvicorn
import os, json
import time as time_module
import logging
from fastapi import Depends, FastAPI, HTTPException, Request, status, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from pydantic_classes import *
from sql_alchemy import *

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

############################################
#
#   Initialize the database
#
############################################

def init_db():
    SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/Class_Diagram.db")
    # Ensure local SQLite directory exists (safe no-op for other DBs)
    os.makedirs("data", exist_ok=True)
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        echo=False
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    return SessionLocal

app = FastAPI(
    title="Class_Diagram API",
    description="Auto-generated REST API with full CRUD operations, relationship management, and advanced features",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=[
        {"name": "System", "description": "System health and statistics"},
        {"name": "User", "description": "Operations for User entities"},
        {"name": "User Relationships", "description": "Manage User relationships"},
        {"name": "Availability", "description": "Operations for Availability entities"},
        {"name": "Availability Relationships", "description": "Manage Availability relationships"},
        {"name": "Appointment", "description": "Operations for Appointment entities"},
        {"name": "Appointment Relationships", "description": "Manage Appointment relationships"},
    ]
)

# Enable CORS for all origins (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

############################################
#
#   Middleware
#
############################################

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all incoming requests and responses."""
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Add processing time header to all responses."""
    start_time = time_module.time()
    response = await call_next(request)
    process_time = time_module.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

############################################
#
#   Exception Handlers
#
############################################

# Global exception handlers
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    """Handle ValueError exceptions."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Bad Request",
            "message": str(exc),
            "detail": "Invalid input data provided"
        }
    )


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    """Handle database integrity errors."""
    logger.error(f"Database integrity error: {exc}")

    # Extract more detailed error information
    error_detail = str(exc.orig) if hasattr(exc, 'orig') else str(exc)

    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "Conflict",
            "message": "Data conflict occurred",
            "detail": error_detail
        }
    )


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
    """Handle general SQLAlchemy errors."""
    logger.error(f"Database error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "Database operation failed",
            "detail": "An internal database error occurred"
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions with consistent format."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail if isinstance(exc.detail, str) else "HTTP Error",
            "message": exc.detail,
            "detail": f"HTTP {exc.status_code} error occurred"
        }
    )

# Initialize database session
SessionLocal = init_db()
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        logger.error("Database session rollback due to exception")
        raise
    finally:
        db.close()

############################################
#
#   Global API endpoints
#
############################################

@app.get("/", tags=["System"])
def root():
    """Root endpoint - API information"""
    return {
        "name": "Class_Diagram API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health", tags=["System"])
def health_check():
    """Health check endpoint for monitoring"""
    from datetime import datetime
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database": "connected"
    }


@app.get("/statistics", tags=["System"])
def get_statistics(database: Session = Depends(get_db)):
    """Get database statistics for all entities"""
    stats = {}
    stats["user_count"] = database.query(User).count()
    stats["availability_count"] = database.query(Availability).count()
    stats["appointment_count"] = database.query(Appointment).count()
    stats["total_entities"] = sum(stats.values())
    return stats


############################################
#
#   BESSER Action Language standard lib
#
############################################


async def BAL_size(sequence:list) -> int:
    return len(sequence)

async def BAL_is_empty(sequence:list) -> bool:
    return len(sequence) == 0

async def BAL_add(sequence:list, elem) -> None:
    sequence.append(elem)

async def BAL_remove(sequence:list, elem) -> None:
    sequence.remove(elem)

async def BAL_contains(sequence:list, elem) -> bool:
    return elem in sequence

async def BAL_filter(sequence:list, predicate) -> list:
    return [elem for elem in sequence if predicate(elem)]

async def BAL_forall(sequence:list, predicate) -> bool:
    for elem in sequence:
        if not predicate(elem):
            return False
    return True

async def BAL_exists(sequence:list, predicate) -> bool:
    for elem in sequence:
        if predicate(elem):
            return True
    return False

async def BAL_one(sequence:list, predicate) -> bool:
    found = False
    for elem in sequence:
        if predicate(elem):
            if found:
                return False
            found = True
    return found

async def BAL_is_unique(sequence:list, mapping) -> bool:
    mapped = [mapping(elem) for elem in sequence]
    return len(set(mapped)) == len(mapped)

async def BAL_map(sequence:list, mapping) -> list:
    return [mapping(elem) for elem in sequence]

async def BAL_reduce(sequence:list, reduce_fn, aggregator) -> any:
    for elem in sequence:
        aggregator = reduce_fn(aggregator, elem)
    return aggregator


############################################
#
#   User functions
#
############################################

@app.get("/user/", response_model=None, tags=["User"])
def get_all_user(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(User)
        query = query.options(joinedload(User.appointment))
        user_list = query.all()

        # Serialize with relationships included
        result = []
        for user_item in user_list:
            item_dict = user_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if user_item.appointment:
                related_obj = user_item.appointment
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['appointment'] = related_dict
            else:
                item_dict['appointment'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(User).all()


@app.get("/user/count/", response_model=None, tags=["User"])
def get_count_user(database: Session = Depends(get_db)) -> dict:
    """Get the total count of User entities"""
    count = database.query(User).count()
    return {"count": count}


@app.get("/user/paginated/", response_model=None, tags=["User"])
def get_paginated_user(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of User entities"""
    total = database.query(User).count()
    user_list = database.query(User).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": user_list
    }


@app.get("/user/search/", response_model=None, tags=["User"])
def search_user(
    database: Session = Depends(get_db)
) -> list:
    """Search User entities by attributes"""
    query = database.query(User)


    results = query.all()
    return results


@app.get("/user/{user_id}/", response_model=None, tags=["User"])
async def get_user(user_id: int, database: Session = Depends(get_db)) -> User:
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    response_data = {
        "user": db_user,
}
    return response_data



@app.post("/user/", response_model=None, tags=["User"])
async def create_user(user_data: UserCreate, database: Session = Depends(get_db)) -> User:


    db_user = User(
        role=user_data.role        )

    database.add(db_user)
    database.commit()
    database.refresh(db_user)




    return db_user


@app.post("/user/bulk/", response_model=None, tags=["User"])
async def bulk_create_user(items: list[UserCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple User entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_user = User(
                role=item_data.role            )
            database.add(db_user)
            database.flush()  # Get ID without committing
            created_items.append(db_user.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} User entities"
    }


@app.delete("/user/bulk/", response_model=None, tags=["User"])
async def bulk_delete_user(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple User entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_user = database.query(User).filter(User.id == item_id).first()
        if db_user:
            database.delete(db_user)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} User entities"
    }

@app.put("/user/{user_id}/", response_model=None, tags=["User"])
async def update_user(user_id: int, user_data: UserCreate, database: Session = Depends(get_db)) -> User:
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    setattr(db_user, 'role', user_data.role)
    database.commit()
    database.refresh(db_user)

    return db_user


@app.delete("/user/{user_id}/", response_model=None, tags=["User"])
async def delete_user(user_id: int, database: Session = Depends(get_db)):
    db_user = database.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    database.delete(db_user)
    database.commit()
    return db_user






############################################
#
#   Availability functions
#
############################################

@app.get("/availability/", response_model=None, tags=["Availability"])
def get_all_availability(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Availability)
        availability_list = query.all()

        # Serialize with relationships included
        result = []
        for availability_item in availability_list:
            item_dict = availability_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)

            # Add many-to-many and one-to-many relationship objects (full details)
            appointment_list = database.query(Appointment).filter(Appointment.availability_id == availability_item.id).all()
            item_dict['blocksOrAllows'] = []
            for appointment_obj in appointment_list:
                appointment_dict = appointment_obj.__dict__.copy()
                appointment_dict.pop('_sa_instance_state', None)
                item_dict['blocksOrAllows'].append(appointment_dict)

            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Availability).all()


@app.get("/availability/count/", response_model=None, tags=["Availability"])
def get_count_availability(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Availability entities"""
    count = database.query(Availability).count()
    return {"count": count}


@app.get("/availability/paginated/", response_model=None, tags=["Availability"])
def get_paginated_availability(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Availability entities"""
    total = database.query(Availability).count()
    availability_list = database.query(Availability).offset(skip).limit(limit).all()
    # By default, return flat entities (for charts/widgets)
    # Use detailed=true to get entities with relationships
    if not detailed:
        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "data": availability_list
        }

    result = []
    for availability_item in availability_list:
        blocksOrAllows_ids = database.query(Appointment.id).filter(Appointment.availability_id == availability_item.id).all()
        item_data = {
            "availability": availability_item,
            "blocksOrAllows_ids": [x[0] for x in blocksOrAllows_ids]        }
        result.append(item_data)
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": result
    }


@app.get("/availability/search/", response_model=None, tags=["Availability"])
def search_availability(
    database: Session = Depends(get_db)
) -> list:
    """Search Availability entities by attributes"""
    query = database.query(Availability)


    results = query.all()
    return results


@app.get("/availability/{availability_id}/", response_model=None, tags=["Availability"])
async def get_availability(availability_id: int, database: Session = Depends(get_db)) -> Availability:
    db_availability = database.query(Availability).filter(Availability.id == availability_id).first()
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")

    blocksOrAllows_ids = database.query(Appointment.id).filter(Appointment.availability_id == db_availability.id).all()
    response_data = {
        "availability": db_availability,
        "blocksOrAllows_ids": [x[0] for x in blocksOrAllows_ids]}
    return response_data



@app.post("/availability/", response_model=None, tags=["Availability"])
async def create_availability(availability_data: AvailabilityCreate, database: Session = Depends(get_db)) -> Availability:


    db_availability = Availability(
        date=availability_data.date,        status=availability_data.status,        endHour=availability_data.endHour,        startHour=availability_data.startHour        )

    database.add(db_availability)
    database.commit()
    database.refresh(db_availability)

    if availability_data.blocksOrAllows:
        # Validate that all Appointment IDs exist
        for appointment_id in availability_data.blocksOrAllows:
            db_appointment = database.query(Appointment).filter(Appointment.id == appointment_id).first()
            if not db_appointment:
                raise HTTPException(status_code=400, detail=f"Appointment with id {appointment_id} not found")

        # Update the related entities with the new foreign key
        database.query(Appointment).filter(Appointment.id.in_(availability_data.blocksOrAllows)).update(
            {Appointment.availability_id: db_availability.id}, synchronize_session=False
        )
        database.commit()



    blocksOrAllows_ids = database.query(Appointment.id).filter(Appointment.availability_id == db_availability.id).all()
    response_data = {
        "availability": db_availability,
        "blocksOrAllows_ids": [x[0] for x in blocksOrAllows_ids]    }
    return response_data


@app.post("/availability/bulk/", response_model=None, tags=["Availability"])
async def bulk_create_availability(items: list[AvailabilityCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Availability entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item

            db_availability = Availability(
                date=item_data.date,                status=item_data.status,                endHour=item_data.endHour,                startHour=item_data.startHour            )
            database.add(db_availability)
            database.flush()  # Get ID without committing
            created_items.append(db_availability.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Availability entities"
    }


@app.delete("/availability/bulk/", response_model=None, tags=["Availability"])
async def bulk_delete_availability(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Availability entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_availability = database.query(Availability).filter(Availability.id == item_id).first()
        if db_availability:
            database.delete(db_availability)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Availability entities"
    }

@app.put("/availability/{availability_id}/", response_model=None, tags=["Availability"])
async def update_availability(availability_id: int, availability_data: AvailabilityCreate, database: Session = Depends(get_db)) -> Availability:
    db_availability = database.query(Availability).filter(Availability.id == availability_id).first()
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")

    setattr(db_availability, 'date', availability_data.date)
    setattr(db_availability, 'status', availability_data.status)
    setattr(db_availability, 'endHour', availability_data.endHour)
    setattr(db_availability, 'startHour', availability_data.startHour)
    if availability_data.blocksOrAllows is not None:
        # Clear all existing relationships (set foreign key to NULL)
        database.query(Appointment).filter(Appointment.availability_id == db_availability.id).update(
            {Appointment.availability_id: None}, synchronize_session=False
        )

        # Set new relationships if list is not empty
        if availability_data.blocksOrAllows:
            # Validate that all IDs exist
            for appointment_id in availability_data.blocksOrAllows:
                db_appointment = database.query(Appointment).filter(Appointment.id == appointment_id).first()
                if not db_appointment:
                    raise HTTPException(status_code=400, detail=f"Appointment with id {appointment_id} not found")

            # Update the related entities with the new foreign key
            database.query(Appointment).filter(Appointment.id.in_(availability_data.blocksOrAllows)).update(
                {Appointment.availability_id: db_availability.id}, synchronize_session=False
            )
    database.commit()
    database.refresh(db_availability)

    blocksOrAllows_ids = database.query(Appointment.id).filter(Appointment.availability_id == db_availability.id).all()
    response_data = {
        "availability": db_availability,
        "blocksOrAllows_ids": [x[0] for x in blocksOrAllows_ids]    }
    return response_data


@app.delete("/availability/{availability_id}/", response_model=None, tags=["Availability"])
async def delete_availability(availability_id: int, database: Session = Depends(get_db)):
    db_availability = database.query(Availability).filter(Availability.id == availability_id).first()
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    database.delete(db_availability)
    database.commit()
    return db_availability


@app.get("/availability/{availability_id}/blocksOrAllows/", response_model=None, tags=["Availability Relationships"])
async def get_blocksOrAllows_of_availability(availability_id: int, database: Session = Depends(get_db)):
    """Get all Appointment entities related to this Availability through blocksOrAllows"""
    db_availability = database.query(Availability).filter(Availability.id == availability_id).first()
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")

    blocksOrAllows_list = database.query(Appointment).filter(Appointment.availability_id == availability_id).all()

    return {
        "availability_id": availability_id,
        "blocksOrAllows_count": len(blocksOrAllows_list),
        "blocksOrAllows": blocksOrAllows_list
    }





############################################
#
#   Appointment functions
#
############################################

@app.get("/appointment/", response_model=None, tags=["Appointment"])
def get_all_appointment(detailed: bool = False, database: Session = Depends(get_db)) -> list:
    from sqlalchemy.orm import joinedload

    # Use detailed=true to get entities with eagerly loaded relationships (for tables with lookup columns)
    if detailed:
        # Eagerly load all relationships to avoid N+1 queries
        query = database.query(Appointment)
        query = query.options(joinedload(Appointment.availability))
        query = query.options(joinedload(Appointment.bookedBy))
        appointment_list = query.all()

        # Serialize with relationships included
        result = []
        for appointment_item in appointment_list:
            item_dict = appointment_item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)

            # Add many-to-one relationships (foreign keys for lookup columns)
            if appointment_item.availability:
                related_obj = appointment_item.availability
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['availability'] = related_dict
            else:
                item_dict['availability'] = None
            if appointment_item.bookedBy:
                related_obj = appointment_item.bookedBy
                related_dict = related_obj.__dict__.copy()
                related_dict.pop('_sa_instance_state', None)
                item_dict['bookedBy'] = related_dict
            else:
                item_dict['bookedBy'] = None


            result.append(item_dict)
        return result
    else:
        # Default: return flat entities (faster for charts/widgets without lookup columns)
        return database.query(Appointment).all()


@app.get("/appointment/count/", response_model=None, tags=["Appointment"])
def get_count_appointment(database: Session = Depends(get_db)) -> dict:
    """Get the total count of Appointment entities"""
    count = database.query(Appointment).count()
    return {"count": count}


@app.get("/appointment/paginated/", response_model=None, tags=["Appointment"])
def get_paginated_appointment(skip: int = 0, limit: int = 100, detailed: bool = False, database: Session = Depends(get_db)) -> dict:
    """Get paginated list of Appointment entities"""
    total = database.query(Appointment).count()
    appointment_list = database.query(Appointment).offset(skip).limit(limit).all()
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "data": appointment_list
    }


@app.get("/appointment/search/", response_model=None, tags=["Appointment"])
def search_appointment(
    database: Session = Depends(get_db)
) -> list:
    """Search Appointment entities by attributes"""
    query = database.query(Appointment)


    results = query.all()
    return results


@app.get("/appointment/{appointment_id}/", response_model=None, tags=["Appointment"])
async def get_appointment(appointment_id: int, database: Session = Depends(get_db)) -> Appointment:
    db_appointment = database.query(Appointment).filter(Appointment.id == appointment_id).first()
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")

    response_data = {
        "appointment": db_appointment,
}
    return response_data



@app.post("/appointment/", response_model=None, tags=["Appointment"])
async def create_appointment(appointment_data: AppointmentCreate, database: Session = Depends(get_db)) -> Appointment:

    if appointment_data.availability is not None:
        db_availability = database.query(Availability).filter(Availability.id == appointment_data.availability).first()
        if not db_availability:
            raise HTTPException(status_code=400, detail="Availability not found")
    else:
        raise HTTPException(status_code=400, detail="Availability ID is required")
    if appointment_data.bookedBy is not None:
        db_bookedBy = database.query(User).filter(User.id == appointment_data.bookedBy).first()
        if not db_bookedBy:
            raise HTTPException(status_code=400, detail="User not found")
    else:
        raise HTTPException(status_code=400, detail="User ID is required")

    db_appointment = Appointment(
        duration=appointment_data.duration,        startTime=appointment_data.startTime,        email=appointment_data.email,        clientName=appointment_data.clientName,        endTime=appointment_data.endTime,        availability_id=appointment_data.availability,        bookedBy_id=appointment_data.bookedBy        )

    database.add(db_appointment)
    database.commit()
    database.refresh(db_appointment)




    return db_appointment


@app.post("/appointment/bulk/", response_model=None, tags=["Appointment"])
async def bulk_create_appointment(items: list[AppointmentCreate], database: Session = Depends(get_db)) -> dict:
    """Create multiple Appointment entities at once"""
    created_items = []
    errors = []

    for idx, item_data in enumerate(items):
        try:
            # Basic validation for each item
            if not item_data.availability:
                raise ValueError("Availability ID is required")
            if not item_data.bookedBy:
                raise ValueError("User ID is required")

            db_appointment = Appointment(
                duration=item_data.duration,                startTime=item_data.startTime,                email=item_data.email,                clientName=item_data.clientName,                endTime=item_data.endTime,                availability_id=item_data.availability,                bookedBy_id=item_data.bookedBy            )
            database.add(db_appointment)
            database.flush()  # Get ID without committing
            created_items.append(db_appointment.id)
        except Exception as e:
            errors.append({"index": idx, "error": str(e)})

    if errors:
        database.rollback()
        raise HTTPException(status_code=400, detail={"message": "Bulk creation failed", "errors": errors})

    database.commit()
    return {
        "created_count": len(created_items),
        "created_ids": created_items,
        "message": f"Successfully created {len(created_items)} Appointment entities"
    }


@app.delete("/appointment/bulk/", response_model=None, tags=["Appointment"])
async def bulk_delete_appointment(ids: list[int], database: Session = Depends(get_db)) -> dict:
    """Delete multiple Appointment entities at once"""
    deleted_count = 0
    not_found = []

    for item_id in ids:
        db_appointment = database.query(Appointment).filter(Appointment.id == item_id).first()
        if db_appointment:
            database.delete(db_appointment)
            deleted_count += 1
        else:
            not_found.append(item_id)

    database.commit()

    return {
        "deleted_count": deleted_count,
        "not_found": not_found,
        "message": f"Successfully deleted {deleted_count} Appointment entities"
    }

@app.put("/appointment/{appointment_id}/", response_model=None, tags=["Appointment"])
async def update_appointment(appointment_id: int, appointment_data: AppointmentCreate, database: Session = Depends(get_db)) -> Appointment:
    db_appointment = database.query(Appointment).filter(Appointment.id == appointment_id).first()
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")

    setattr(db_appointment, 'duration', appointment_data.duration)
    setattr(db_appointment, 'startTime', appointment_data.startTime)
    setattr(db_appointment, 'email', appointment_data.email)
    setattr(db_appointment, 'clientName', appointment_data.clientName)
    setattr(db_appointment, 'endTime', appointment_data.endTime)
    if appointment_data.availability is not None:
        db_availability = database.query(Availability).filter(Availability.id == appointment_data.availability).first()
        if not db_availability:
            raise HTTPException(status_code=400, detail="Availability not found")
        setattr(db_appointment, 'availability_id', appointment_data.availability)
    if appointment_data.bookedBy is not None:
        db_bookedBy = database.query(User).filter(User.id == appointment_data.bookedBy).first()
        if not db_bookedBy:
            raise HTTPException(status_code=400, detail="User not found")
        setattr(db_appointment, 'bookedBy_id', appointment_data.bookedBy)
    database.commit()
    database.refresh(db_appointment)

    return db_appointment


@app.delete("/appointment/{appointment_id}/", response_model=None, tags=["Appointment"])
async def delete_appointment(appointment_id: int, database: Session = Depends(get_db)):
    db_appointment = database.query(Appointment).filter(Appointment.id == appointment_id).first()
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    database.delete(db_appointment)
    database.commit()
    return db_appointment








############################################
# Maintaining the server
############################################
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



