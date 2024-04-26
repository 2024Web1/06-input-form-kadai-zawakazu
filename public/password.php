<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>パスワードの練習(送信後)</title>
</head>

<body>

    <!--
    * H4タグに自分の`出席番号 氏名`を入れる
    * フォームとして受け取った`user`,`pass`の値をそれぞれPHPの命令で出力する
        * それぞれを**pタグでくくる**こと
        * 「入力されたユーザーIDは、XXXX(`user`の値)です」
        * 「入力されたパスワードは、XXXX(`pass`の値)です」
-->

    <h4><!-- 出席番号 氏名 --></h4>
    <p>入力されたユーザーIDは、<?php echo $_POST['user']; ?>です</p>
    <p>入力されたパスワードは、<?php echo $_POST['pass']; ?>です</p>
</body>

</html>
