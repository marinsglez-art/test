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


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: GUI_Module

# Screen: wrapper
wrapper = Screen(name="wrapper", description="Appointment", view_elements=set(), is_main_page=True, route_path="/appointment", screen_size="Medium")
wrapper.component_id = "page-appointment-0"
i303c = Text(
    name="i303c",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="i303c",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "i303c"}
)
iz1np = Link(
    name="iz1np",
    description="Link element",
    label="Appointment",
    url="/appointment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="iz1np",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/appointment", "id": "iz1np"}
)
ir1bw = Link(
    name="ir1bw",
    description="Link element",
    label="Availability",
    url="/availability",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ir1bw",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/availability", "id": "ir1bw"}
)
ivfkg = Link(
    name="ivfkg",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="ivfkg",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/user", "id": "ivfkg"}
)
ippri = ViewContainer(
    name="ippri",
    description=" component",
    view_elements={iz1np, ir1bw, ivfkg},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="ippri",
    display_order=1,
    custom_attributes={"id": "ippri"}
)
ippri_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
ippri.layout = ippri_layout
i4a7i = Text(
    name="i4a7i",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i4a7i",
    display_order=2,
    custom_attributes={"id": "i4a7i"}
)
i43tv = ViewContainer(
    name="i43tv",
    description="nav container",
    view_elements={i303c, ippri, i4a7i},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="i43tv",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "i43tv"}
)
i43tv_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
i43tv.layout = i43tv_layout
ia64y = Text(
    name="ia64y",
    content="Appointment",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="ia64y",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "ia64y"}
)
imnpa = Text(
    name="imnpa",
    content="Manage Appointment data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="imnpa",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "imnpa"}
)
table_appointment_0_col_0 = FieldColumn(label="ClientName", field=Appointment_clientName)
table_appointment_0_col_1 = FieldColumn(label="Email", field=Appointment_email)
table_appointment_0_col_2 = FieldColumn(label="StartTime", field=Appointment_startTime)
table_appointment_0_col_3 = FieldColumn(label="EndTime", field=Appointment_endTime)
table_appointment_0_col_4 = FieldColumn(label="Duration", field=Appointment_duration)
table_appointment_0_col_5_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "bookedBy")
table_appointment_0_col_5 = LookupColumn(label="BookedBy", path=table_appointment_0_col_5_path, field=User_role)
table_appointment_0 = Table(
    name="table_appointment_0",
    title="Appointment List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_appointment_0_col_0, table_appointment_0_col_1, table_appointment_0_col_2, table_appointment_0_col_3, table_appointment_0_col_4, table_appointment_0_col_5],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-appointment-0",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Appointment List", "data-source": "class_h6gns4cio_mocttnmb_y3t", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'clientName', 'label': 'ClientName', 'columnType': 'field', '_expanded': False}, {'field': 'email', 'label': 'Email', 'columnType': 'field', '_expanded': False}, {'field': 'startTime', 'label': 'StartTime', 'columnType': 'field', '_expanded': False}, {'field': 'endTime', 'label': 'EndTime', 'columnType': 'field', '_expanded': False}, {'field': 'duration', 'label': 'Duration', 'columnType': 'field', '_expanded': False}, {'field': 'bookedBy', 'label': 'BookedBy', 'columnType': 'lookup', 'lookupEntity': 'class_q37ig77w0_mocttnmb_r9t', 'lookupField': 'role', '_expanded': False}, {'field': 'Availability', 'label': 'Availability', 'columnType': 'lookup', 'lookupEntity': 'class_pxm5duwij_mocttnmb_xo6', 'lookupField': 'date', '_expanded': False}], "id": "table-appointment-0", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_appointment_0_binding_domain = None
if domain_model_ref is not None:
    table_appointment_0_binding_domain = domain_model_ref.get_class_by_name("Appointment")
if table_appointment_0_binding_domain:
    table_appointment_0_binding = DataBinding(domain_concept=table_appointment_0_binding_domain, name="AppointmentDataBinding")
else:
    # Domain class 'Appointment' not resolved; data binding skipped.
    table_appointment_0_binding = None
if table_appointment_0_binding:
    table_appointment_0.data_binding = table_appointment_0_binding
i4let = ViewContainer(
    name="i4let",
    description="main container",
    view_elements={ia64y, imnpa, table_appointment_0},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i4let",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i4let"}
)
i4let_layout = Layout(flex="1")
i4let.layout = i4let_layout
i2bg8 = ViewContainer(
    name="i2bg8",
    description=" component",
    view_elements={i43tv, i4let},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i2bg8",
    display_order=0,
    custom_attributes={"id": "i2bg8"}
)
i2bg8_layout = Layout(layout_type=LayoutType.FLEX)
i2bg8.layout = i2bg8_layout
wrapper.view_elements = {i2bg8}


# Screen: wrapper_2
wrapper_2 = Screen(name="wrapper_2", description="Availability", view_elements=set(), route_path="/availability", screen_size="Medium")
wrapper_2.component_id = "page-availability-1"
ii6mg = Text(
    name="ii6mg",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ii6mg",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ii6mg"}
)
i6izd = Link(
    name="i6izd",
    description="Link element",
    label="Appointment",
    url="/appointment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i6izd",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/appointment", "id": "i6izd"}
)
i3dju = Link(
    name="i3dju",
    description="Link element",
    label="Availability",
    url="/availability",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i3dju",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/availability", "id": "i3dju"}
)
irkwd = Link(
    name="irkwd",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="irkwd",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/user", "id": "irkwd"}
)
iolxq = ViewContainer(
    name="iolxq",
    description=" component",
    view_elements={i6izd, i3dju, irkwd},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iolxq",
    display_order=1,
    custom_attributes={"id": "iolxq"}
)
iolxq_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iolxq.layout = iolxq_layout
i8bti = Text(
    name="i8bti",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="i8bti",
    display_order=2,
    custom_attributes={"id": "i8bti"}
)
i3bag = ViewContainer(
    name="i3bag",
    description="nav container",
    view_elements={ii6mg, iolxq, i8bti},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="i3bag",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "i3bag"}
)
i3bag_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
i3bag.layout = i3bag_layout
imwre = Text(
    name="imwre",
    content="Availability",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="imwre",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "imwre"}
)
iq82m = Text(
    name="iq82m",
    content="Manage Availability data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="iq82m",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "iq82m"}
)
table_availability_1_col_0 = FieldColumn(label="Date", field=Availability_date)
table_availability_1_col_1 = FieldColumn(label="StartHour", field=Availability_startHour)
table_availability_1_col_2 = FieldColumn(label="EndHour", field=Availability_endHour)
table_availability_1_col_3 = FieldColumn(label="Status", field=Availability_status)
table_availability_1_col_4_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "blocksOrAllows")
table_availability_1_col_4 = LookupColumn(label="BlocksOrAllows", path=table_availability_1_col_4_path, field=Appointment_clientName)
table_availability_1 = Table(
    name="table_availability_1",
    title="Availability List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_availability_1_col_0, table_availability_1_col_1, table_availability_1_col_2, table_availability_1_col_3, table_availability_1_col_4],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-availability-1",
    display_order=2,
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "Availability List", "data-source": "class_pxm5duwij_mocttnmb_xo6", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'date', 'label': 'Date', 'columnType': 'field', '_expanded': False}, {'field': 'startHour', 'label': 'StartHour', 'columnType': 'field', '_expanded': False}, {'field': 'endHour', 'label': 'EndHour', 'columnType': 'field', '_expanded': False}, {'field': 'status', 'label': 'Status', 'columnType': 'field', '_expanded': False}, {'field': 'blocksOrAllows', 'label': 'BlocksOrAllows', 'columnType': 'lookup', 'lookupEntity': 'class_h6gns4cio_mocttnmb_y3t', 'lookupField': 'clientName', '_expanded': False}], "id": "table-availability-1", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_availability_1_binding_domain = None
if domain_model_ref is not None:
    table_availability_1_binding_domain = domain_model_ref.get_class_by_name("Availability")
if table_availability_1_binding_domain:
    table_availability_1_binding = DataBinding(domain_concept=table_availability_1_binding_domain, name="AvailabilityDataBinding")
else:
    # Domain class 'Availability' not resolved; data binding skipped.
    table_availability_1_binding = None
if table_availability_1_binding:
    table_availability_1.data_binding = table_availability_1_binding
i39yr = ViewContainer(
    name="i39yr",
    description="main container",
    view_elements={imwre, iq82m, table_availability_1},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="i39yr",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "i39yr"}
)
i39yr_layout = Layout(flex="1")
i39yr.layout = i39yr_layout
i0egq = ViewContainer(
    name="i0egq",
    description=" component",
    view_elements={i3bag, i39yr},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="i0egq",
    display_order=0,
    custom_attributes={"id": "i0egq"}
)
i0egq_layout = Layout(layout_type=LayoutType.FLEX)
i0egq.layout = i0egq_layout
wrapper_2.view_elements = {i0egq}


# Screen: wrapper_3
wrapper_3 = Screen(name="wrapper_3", description="User", view_elements=set(), route_path="/user", screen_size="Medium")
wrapper_3.component_id = "page-user-2"
ix3r3 = Text(
    name="ix3r3",
    content="BESSER",
    description="Text element",
    styling=Styling(size=Size(font_size="24px", font_weight="bold", margin_top="0", margin_bottom="30px"), color=Color(color_palette="default")),
    component_id="ix3r3",
    tag_name="h2",
    display_order=0,
    custom_attributes={"id": "ix3r3"}
)
i2ili = Link(
    name="i2ili",
    description="Link element",
    label="Appointment",
    url="/appointment",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i2ili",
    tag_name="a",
    display_order=0,
    custom_attributes={"href": "/appointment", "id": "i2ili"}
)
in8vb = Link(
    name="in8vb",
    description="Link element",
    label="Availability",
    url="/availability",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="transparent", text_color="white", color_palette="default", border_radius="4px")),
    component_id="in8vb",
    tag_name="a",
    display_order=1,
    custom_attributes={"href": "/availability", "id": "in8vb"}
)
i3d8v = Link(
    name="i3d8v",
    description="Link element",
    label="User",
    url="/user",
    styling=Styling(size=Size(padding="10px 15px", text_decoration="none", margin_bottom="5px"), position=Position(display="block"), color=Color(background_color="rgba(255,255,255,0.2)", text_color="white", color_palette="default", border_radius="4px")),
    component_id="i3d8v",
    tag_name="a",
    display_order=2,
    custom_attributes={"href": "/user", "id": "i3d8v"}
)
iitxe = ViewContainer(
    name="iitxe",
    description=" component",
    view_elements={i2ili, in8vb, i3d8v},
    styling=Styling(position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")),
    component_id="iitxe",
    display_order=1,
    custom_attributes={"id": "iitxe"}
)
iitxe_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column", flex="1")
iitxe.layout = iitxe_layout
izzy9 = Text(
    name="izzy9",
    content="© 2026 BESSER. All rights reserved.",
    description="Text element",
    styling=Styling(size=Size(font_size="11px", padding_top="20px", margin_top="auto"), position=Position(alignment=Alignment.CENTER), color=Color(opacity="0.8", color_palette="default", border_top="1px solid rgba(255,255,255,0.2)")),
    component_id="izzy9",
    display_order=2,
    custom_attributes={"id": "izzy9"}
)
iwjt9 = ViewContainer(
    name="iwjt9",
    description="nav container",
    view_elements={ix3r3, iitxe, izzy9},
    styling=Styling(size=Size(width="250px", padding="20px", unit_size=UnitSize.PIXELS), position=Position(display="flex", overflow_y="auto"), color=Color(background_color="linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", text_color="white", color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX, flex_direction="column")),
    component_id="iwjt9",
    tag_name="nav",
    display_order=0,
    custom_attributes={"id": "iwjt9"}
)
iwjt9_layout = Layout(layout_type=LayoutType.FLEX, flex_direction="column")
iwjt9.layout = iwjt9_layout
iqfwf = Text(
    name="iqfwf",
    content="User",
    description="Text element",
    styling=Styling(size=Size(font_size="32px", margin_top="0", margin_bottom="10px"), color=Color(text_color="#333", color_palette="default")),
    component_id="iqfwf",
    tag_name="h1",
    display_order=0,
    custom_attributes={"id": "iqfwf"}
)
iugt6 = Text(
    name="iugt6",
    content="Manage User data",
    description="Text element",
    styling=Styling(size=Size(margin_bottom="30px"), color=Color(text_color="#666", color_palette="default")),
    component_id="iugt6",
    tag_name="p",
    display_order=1,
    custom_attributes={"id": "iugt6"}
)
table_user_2_col_0 = FieldColumn(label="Role", field=User_role)
table_user_2 = Table(
    name="table_user_2",
    title="User List",
    primary_color="#2c3e50",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=5,
    action_buttons=True,
    columns=[table_user_2_col_0],
    styling=Styling(size=Size(width="100%", min_height="400px", unit_size=UnitSize.PERCENTAGE), color=Color(color_palette="default", primary_color="#2c3e50")),
    component_id="table-user-2",
    display_order=2,
    css_classes=["has-data-binding"],
    custom_attributes={"chart-color": "#2c3e50", "chart-title": "User List", "data-source": "class_q37ig77w0_mocttnmb_r9t", "show-header": "true", "striped-rows": "false", "show-pagination": "true", "rows-per-page": "5", "action-buttons": "true", "columns": [{'field': 'role', 'label': 'Role', 'columnType': 'field', '_expanded': False}, {'field': 'Appointment', 'label': 'Appointment', 'columnType': 'lookup', 'lookupEntity': 'class_h6gns4cio_mocttnmb_y3t', 'lookupField': 'clientName', '_expanded': False}], "id": "table-user-2", "filter": ""}
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table_user_2_binding_domain = None
if domain_model_ref is not None:
    table_user_2_binding_domain = domain_model_ref.get_class_by_name("User")
if table_user_2_binding_domain:
    table_user_2_binding = DataBinding(domain_concept=table_user_2_binding_domain, name="UserDataBinding")
else:
    # Domain class 'User' not resolved; data binding skipped.
    table_user_2_binding = None
if table_user_2_binding:
    table_user_2.data_binding = table_user_2_binding
ijv7g = ViewContainer(
    name="ijv7g",
    description="main container",
    view_elements={iqfwf, iugt6, table_user_2},
    styling=Styling(size=Size(padding="40px"), position=Position(overflow_y="auto"), color=Color(background_color="#f5f5f5", color_palette="default"), layout=Layout(flex="1")),
    component_id="ijv7g",
    tag_name="main",
    display_order=1,
    custom_attributes={"id": "ijv7g"}
)
ijv7g_layout = Layout(flex="1")
ijv7g.layout = ijv7g_layout
ifdkg = ViewContainer(
    name="ifdkg",
    description=" component",
    view_elements={iwjt9, ijv7g},
    styling=Styling(size=Size(height="100vh", font_family="Arial, sans-serif"), position=Position(display="flex"), color=Color(color_palette="default"), layout=Layout(layout_type=LayoutType.FLEX)),
    component_id="ifdkg",
    display_order=0,
    custom_attributes={"id": "ifdkg"}
)
ifdkg_layout = Layout(layout_type=LayoutType.FLEX)
ifdkg.layout = ifdkg_layout
wrapper_3.view_elements = {ifdkg}

gui_module = Module(
    name="GUI_Module",
    screens={wrapper, wrapper_2, wrapper_3}
)

# GUI Model
gui_model = GUIModel(
    name="GUI",
    package="",
    versionCode="1.0",
    versionName="1.0",
    modules={gui_module},
    description="GUI"
)
