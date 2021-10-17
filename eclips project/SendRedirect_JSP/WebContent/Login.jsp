<%
String uname=request.getParameter("uname");
String pwd=request.getParameter("pwd");
if(uname.equals("admin")&&pwd.equals("admin")){
	//request.setAttribute("msg","login success");
	session.setAttribute("msg","login success");
	response.sendRedirect("./success.jsp");
}
else
{
	//request.setAttribute("msg","login success");
    session.setAttribute("msg","login fail");
	response.sendRedirect("./fail.jsp");
}
%>