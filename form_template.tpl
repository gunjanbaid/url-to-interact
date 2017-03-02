<!DOCTYPE html>
<head>
<title>URL to Interact</title>
</head>

<body>
<form action="/" method="post" class="form-style-9">
<ul>
<li><textarea name="url" class="field-style" placeholder="Paste the GitHub URL for your file or folder here. Make sure you're on the desired branch! 

Example:
https://github.com/data-8/connector-instructors/blob/gh-pages/examples/create_interact_link.ipynb"></textarea></li>
<li><center><input type="submit" value="Convert to interact link!"/></center></li>
<li><textarea class="field-style" placeholder="Your interact link URL will appear here.

Example:
http://datahub.berkeley.edu/user-redirect/interact?repo=connector-instructors&branch=gh-pages&path=examples/create_interact_link.ipynb
">
%if show_url:
{{interact}}
%end
</textarea></li>
</ul>
</form>
</body>

<style type="text/css">
.form-style-9{
    max-width: 800px;
    background: #FAFAFA;
    padding: 30px;
    margin: 50px auto;
    border: 6px solid #276f91;
}
.form-style-9 ul{
    padding:0;
    margin:0;
    list-style:none;
}
.form-style-9 ul li{
    display: block;
    margin-bottom: 10px;
    min-height: 35px;
}
.form-style-9 ul li  .field-style{
    box-sizing: border-box; 
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box; 
    padding: 8px;
    outline: none;
    border: 1px solid #B0CFE0;
    -webkit-transition: all 0.30s ease-in-out;
    -moz-transition: all 0.30s ease-in-out;
    -ms-transition: all 0.30s ease-in-out;
    -o-transition: all 0.30s ease-in-out;

}.form-style-9 ul li  .field-style:focus{
    box-shadow: 0 0 5px #B0CFE0;
    border:1px solid #B0CFE0;
}
.form-style-9 ul li .field-split{
    width: 49%;
}
.form-style-9 ul li .field-full{
    width: 100%;
}
.form-style-9 ul li input.align-left{
    float:left;
}
.form-style-9 ul li input.align-right{
    float:right;
}
.form-style-9 ul li textarea{
    width: 100%;
    height: 100px;
}
.form-style-9 ul li input[type="button"], 
.form-style-9 ul li input[type="submit"] {
    background-color: #276f91;
    border: 1px solid #276f91;
    display: inline-block;
    cursor: pointer;
    color: #FFFFFF;
    padding: 8px 18px;
    text-decoration: none;
    font: 12px Arial, Helvetica, sans-serif;
}
.form-style-9 ul li input[type="button"]:hover, 
.form-style-9 ul li input[type="submit"]:hover {
    background: linear-gradient(to bottom, #2D77A2 5%, #337DA8 100%);
    background-color: #276f91;
}
</style>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-92901816-1', 'auto');
  ga('send', 'pageview');

</script>