<%@page import="java.sql.PreparedStatement" %>
<%@page import="java.sql.DriverManager" %>
<%@page import="java.sql.Connection" %>

<%@page import="java.sql.ResultSet" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Dynamic Reg Form</title>
</head>
<body>

<%
     Class.forName("oracle.jdbc.driver.OracleDriver");
     Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","1998");
     PreparedStatement ps=con.prepareStatement("select * from qualification ");
     ResultSet rs=ps.executeQuery();
     
%>
<form action="./reg.jsp">
<pre>
Id      : <input type="text" name="id">
Name    : <input type="text" name="name">
Email   : <input type="text" name="email">
Address : <input type="text" name="address">

Qualification: <select name="qual">
               <% while(rs.next()) { %>
               <option value=" <%=rs.getString(2) %> "> <%=rs.getString(2) %></option>
               <% }%>
               </select>

        <input type="submit" value="submit"/>
</pre>
</form>
<% rs.close();
   con.close();
 %>
</body>
</html>