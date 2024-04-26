<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>テキストエリア練習問題(結果)</title>
</head>
<body>
<!--
* H4タグに自分の`出席番号 氏名`を入れる
* フォームとして受け取った`input_text`の値を出力する
    * 出力するテキストはpタグでくくる

-->
<h4>出席番号 氏名</h4>
<p>入力されたテキストは以下の通りです。
<p><?php echo $_POST['input_text']; ?></p>
</body>
</html>
