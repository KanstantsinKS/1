from bs4 import BeautifulSoup
html_string = '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Index</title>

</head>
<body>
    <div id="header">
        <h1>My web site</h1>
    </div>

    <div id="menubar">
        <a href="index.html">HOME</a>
        <a href="py/index.html">Python</a>
        <a href="html5/index.html">HTML5</a>
        <a href="css3/index.html">CSS3</a>
        <a href="js/index.html">JavaScript</a>
        <a href="sql/index.html">SQL</a>
        <a href="git/index.html">Git</a>
    </div>

    <div id="content">
        <h2>What is this site about?</h2>
        <p>
            On this site, I will share with you my successes in learning various programming languages.
        </p>

        
        <p>
            На этом веб-сайте Я буду размещать то, что узнаю о разных языках программирования, программировании в целом и связанные с ним вещи. 
        </p>

        <p>
            Сейчас я изучаю такие языки как: 
            <ul>
                <li>Python и различные фреймворки к нему, например Django, Flask, Docker;</li>
                <li>HTML5, CSS3, JavaScript;</li>
                <li>MySql</li>
                <li>Git</li>
            </ul>
        </p>
    </div>

    <div id="footer">
        <p id='footer'>2021 KanstantsinKS<br>
        All rights reserved<p>
    </div>
</body>
</html>

'''

parsed_html = BeautifulSoup(html_string, 'html.parser')
# print(parsed_html)
# print(type(parsed_html))

print(parsed_html.body.ul.li)
print(parsed_html.find('li'))
print(parsed_html.find_all('li'))
print(parsed_html.select('li'))