####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Classes
Appointment = Class(name="Appointment")
Availability = Class(name="Availability")
User = Class(name="User")

# Appointment class attributes and methods
Appointment_clientName: Property = Property(name="clientName", type=StringType)
Appointment_email: Property = Property(name="email", type=StringType)
Appointment_startTime: Property = Property(name="startTime", type=DateType)
Appointment_endTime: Property = Property(name="endTime", type=DateType)
Appointment_duration: Property = Property(name="duration", type=IntegerType)
Appointment.attributes={Appointment_clientName, Appointment_duration, Appointment_email, Appointment_endTime, Appointment_startTime}

# Availability class attributes and methods
Availability_date: Property = Property(name="date", type=DateType)
Availability_startHour: Property = Property(name="startHour", type=IntegerType)
Availability_endHour: Property = Property(name="endHour", type=IntegerType)
Availability_status: Property = Property(name="status", type=StringType)
Availability.attributes={Availability_date, Availability_endHour, Availability_startHour, Availability_status}

# User class attributes and methods
User_role: Property = Property(name="role", type=StringType)
User.attributes={User_role}

# Relationships
bookedBy: BinaryAssociation = BinaryAssociation(
    name="bookedBy",
    ends={
        Property(name="appointment", type=Appointment, multiplicity=Multiplicity(1, 1)),
        Property(name="bookedBy", type=User, multiplicity=Multiplicity(1, 1))
    }
)
blocksOrAllows: BinaryAssociation = BinaryAssociation(
    name="blocksOrAllows",
    ends={
        Property(name="availability", type=Availability, multiplicity=Multiplicity(1, 1)),
        Property(name="blocksOrAllows", type=Appointment, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Class_Diagram",
    types={Appointment, Availability, User},
    associations={bookedBy, blocksOrAllows},
    generalizations={},
    metadata=None
)
