import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";

const Appointment: React.FC = () => {
  return (
    <div id="page-appointment-0">
    <div id="i2bg8" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="i43tv" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="i303c" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="ippri" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="iz1np" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/appointment">{"Appointment"}</a>
          <a id="ir1bw" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/availability">{"Availability"}</a>
          <a id="ivfkg" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/user">{"User"}</a>
        </div>
        <p id="i4a7i" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="i4let" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="ia64y" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"Appointment"}</h1>
        <p id="imnpa" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage Appointment data"}</p>
        <TableBlock id="table-appointment-0" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Appointment List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "ClientName", "column_type": "field", "field": "clientName", "type": "str", "required": true}, {"label": "Email", "column_type": "field", "field": "email", "type": "str", "required": true}, {"label": "StartTime", "column_type": "field", "field": "startTime", "type": "date", "required": true}, {"label": "EndTime", "column_type": "field", "field": "endTime", "type": "date", "required": true}, {"label": "Duration", "column_type": "field", "field": "duration", "type": "int", "required": true}, {"label": "BookedBy", "column_type": "lookup", "path": "bookedBy", "entity": "User", "field": "role", "type": "str", "required": true}], "formColumns": [{"column_type": "field", "field": "clientName", "label": "clientName", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "email", "label": "email", "type": "str", "required": true, "defaultValue": null}, {"column_type": "field", "field": "startTime", "label": "startTime", "type": "date", "required": true, "defaultValue": null}, {"column_type": "field", "field": "endTime", "label": "endTime", "type": "date", "required": true, "defaultValue": null}, {"column_type": "field", "field": "duration", "label": "duration", "type": "int", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "bookedBy", "field": "bookedBy", "lookup_field": "role", "entity": "User", "type": "str", "required": true}, {"column_type": "lookup", "path": "availability", "field": "availability", "lookup_field": "date", "entity": "Availability", "type": "str", "required": true}]}} dataBinding={{"entity": "Appointment", "endpoint": "/appointment/"}} />
      </main>
    </div>    </div>
  );
};

export default Appointment;
