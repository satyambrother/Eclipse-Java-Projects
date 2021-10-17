<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<%@page import="java.sql.PreparedStatement" %>
<%@page import="java.sql.DriverManager" %>
<%@page import="java.sql.Connection" %>
<%
int id=Integer.parseInt(request.getParameter("id"));
String name=request.getParameter("name");
String email=request.getParameter("email");
String address=request.getParameter("address");
String qual=request.getParameter("qual");

Class.forName("oracle.jdbc.driver.OracleDriver");
Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","1998");
PreparedStatement ps=con.prepareStatement("insert into student values(?,?,?,?,?) ");
ps.setInt(1,id);
ps.setString(2,name);
ps.setString(3,email);
ps.setString(4,address);
ps.setString(5,qual);
int i =ps.executeUpdate();
con.close();
ps.close();

if(i!=0)
	out.println("<h1>Registration Successful <h2>");
else
	out.println("<h1>Registration Un Successful <h2>");
	

%>
</body>
</html>