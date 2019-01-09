<%@ include file="/commons/taglib.jsp"%>
<%@page language="java" contentType="application/json"  pageEncoding="UTF-8"
    import="org.apache.wink.json4j.*"
    import="com.fasterxml.jackson.databind.ObjectMapper"
    import="com.intumit.citi.backend.*"
    import="com.intumit.citi.frontend.*"
    import="com.intumit.citi.*"
    import="com.intumit.solr.robot.*"
    import="org.apache.wink.json4j.*"    
%><%!
%><%

Menu menu;
ObjectMapper mapper;
Result result;

menu = new Menu();
mapper = new ObjectMapper();
result = new Result();
result.setCode(0);
result.setMessage("");
menu.setResult(result);

String qaId = request.getParameter("id");
//QAContext qaCtx = QAContextManager.lookup(qaId);
CardInfo cardinfo = CitiUtil.getSmartMenu(qaId, Result.Postfix.STMTDETAIL.toString()) ; //= ((CardInfo)qaCtx.getCtxAttr("cardinfo"));
Info info = cardinfo.getAdditionalProperties(request.getParameter("carno"));
BoxGrid box = new BoxGrid();
box.setId(qaId);
box.setType(Box.Type.GRID);
box.setTitle(CitiUtil.currBillTranDetail);
box.addHeader(new Header("交易日",null));
box.addHeader(new Header("請款日",null));
box.addHeader(new Header("金額","right"));
GridRow row = new GridRow();
row.setTitle(info.getCardno().replaceFirst(".*(\\d{4})", (info.getPrim().equals("true") ? "主" : "副") + "卡$1新增消費"));
row.setIsTitle(true);
box.addRow(row);
int newLineCnt = 0;
for (Txn txn:info.getTxns()) {
    row = new GridRow();
    Field field = new Field();
    field.setText(txn.getTxndate());
    row.addField(field);
    field = new Field();
    field.setText(txn.getDate());
    row.addField(field);
    field = new Field();
    field.setText(txn.getDesc());
    row.addField(field);
    field = new Field();
    field.setText( CitiUtil.formatMoney(txn.getAmount(), CitiUtil.fontColor.BLUE) );
    row.addField(field);
    if (newLineCnt > 0)
        row.setIsAlternatingRow(true);
    newLineCnt++;
    box.addRow(row);
}
menu.setBox(box);

String jsonInString = mapper/*.writerWithDefaultPrettyPrinter()*/.writeValueAsString(menu);
JSONObject json=null;
try {
    json = new JSONObject(jsonInString);
} catch (JSONException e) {
	  // TODO Auto-generated catch block
	  e.printStackTrace();
}

%><%= json.toString(4) %>
