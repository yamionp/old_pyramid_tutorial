<html>
<body>
%if request.session.peek_flash():
<div>
  <ul>
    %for m in request.session.pop_flash():
    <li>${m}</li>
    %endfor
  </ul>
</div>
%endif
Balance: ${bankaccount.balance}
<form action="${request.route_url('deposit')}" method="post">
  <fieldset>
    <legend>Despsit</legend>
    <input name="amount">
    <input type="submit">
  </fieldset>
</form>
<form action="${request.route_url('withdraw')}" method="post">
  <fieldset>
    <legend>Withdraw</legend>
    <input name="amount">
    <input type="submit">
  </fieldset>
</form>
</body>
</html>