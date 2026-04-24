import React from "react";
import { TableBlock } from "../components/runtime/TableBlock";

const Availability: React.FC = () => {
  return (
    <div id="page-availability-1">
    <div id="i0egq" style={{"height": "100vh", "fontFamily": "Arial, sans-serif", "display": "flex", "--chart-color-palette": "default"}}>
      <nav id="i3bag" style={{"width": "250px", "padding": "20px", "display": "flex", "overflowY": "auto", "background": "linear-gradient(135deg, #4b3c82 0%, #5a3d91 100%)", "color": "white", "--chart-color-palette": "default", "flexDirection": "column"}}>
        <h2 id="ii6mg" style={{"fontSize": "24px", "fontWeight": "bold", "marginTop": "0", "marginBottom": "30px", "--chart-color-palette": "default"}}>{"BESSER"}</h2>
        <div id="iolxq" style={{"display": "flex", "--chart-color-palette": "default", "flexDirection": "column", "flex": "1"}}>
          <a id="i6izd" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/appointment">{"Appointment"}</a>
          <a id="i3dju" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "rgba(255,255,255,0.2)", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/availability">{"Availability"}</a>
          <a id="irkwd" style={{"padding": "10px 15px", "textDecoration": "none", "marginBottom": "5px", "display": "block", "background": "transparent", "color": "white", "borderRadius": "4px", "--chart-color-palette": "default"}} href="/user">{"User"}</a>
        </div>
        <p id="i8bti" style={{"fontSize": "11px", "paddingTop": "20px", "marginTop": "auto", "textAlign": "center", "opacity": "0.8", "borderTop": "1px solid rgba(255,255,255,0.2)", "--chart-color-palette": "default"}}>{"© 2026 BESSER. All rights reserved."}</p>
      </nav>
      <main id="i39yr" style={{"padding": "40px", "overflowY": "auto", "background": "#f5f5f5", "--chart-color-palette": "default", "flex": "1"}}>
        <h1 id="imwre" style={{"fontSize": "32px", "marginTop": "0", "marginBottom": "10px", "color": "#333", "--chart-color-palette": "default"}}>{"Availability"}</h1>
        <p id="iq82m" style={{"marginBottom": "30px", "color": "#666", "--chart-color-palette": "default"}}>{"Manage Availability data"}</p>
        <TableBlock id="table-availability-1" styles={{"width": "100%", "minHeight": "400px", "--chart-color-palette": "default"}} title="Availability List" options={{"showHeader": true, "stripedRows": false, "showPagination": true, "rowsPerPage": 5, "actionButtons": true, "columns": [{"label": "Date", "column_type": "field", "field": "date", "type": "date", "required": true}, {"label": "StartHour", "column_type": "field", "field": "startHour", "type": "int", "required": true}, {"label": "EndHour", "column_type": "field", "field": "endHour", "type": "int", "required": true}, {"label": "Status", "column_type": "field", "field": "status", "type": "str", "required": true}, {"label": "BlocksOrAllows", "column_type": "lookup", "path": "blocksOrAllows", "entity": "Appointment", "field": "clientName", "type": "list", "required": false}], "formColumns": [{"column_type": "field", "field": "date", "label": "date", "type": "date", "required": true, "defaultValue": null}, {"column_type": "field", "field": "startHour", "label": "startHour", "type": "int", "required": true, "defaultValue": null}, {"column_type": "field", "field": "endHour", "label": "endHour", "type": "int", "required": true, "defaultValue": null}, {"column_type": "field", "field": "status", "label": "status", "type": "str", "required": true, "defaultValue": null}, {"column_type": "lookup", "path": "blocksOrAllows", "field": "blocksOrAllows", "lookup_field": "clientName", "entity": "Appointment", "type": "list", "required": false}]}} dataBinding={{"entity": "Availability", "endpoint": "/availability/"}} />
      </main>
    </div>    </div>
  );
};

export default Availability;
