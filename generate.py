import os,re

files: list[str] = []

for f in os.listdir("./methods"):
    if f.endswith(".js"):
        print(f"\x1b[32mSelecting  \x1b[0m{f}")
        files.append(f)
    else:
        print(f"\x1b[31mDiscarding \x1b[0m{f}")

content=""

print("")

def getFunctionArgName(text: str):
    m = re.search(r"function calcPi\((\w+)\) ?\{",text)
    
    return m.group(1)

for fname in files:
    with open("methods/"+fname,'r') as f:
        print(f"\nProcessing \x1b[33m{fname}\x1b[0m...")
        text=f.read()
        name="Error"
        desc="Error"
        url=None
        long_desc=""
        in_long_desc=False
        arg_name = getFunctionArgName(text)
        for line in text.split("\n"):
            if line.startswith("*/"):
                in_long_desc=False
            if in_long_desc:
                long_desc+=f"{line}\n"
            if line.startswith("// name: "):
                name=line[9:]
            if line.startswith("// desc: "):
                desc=line[9:]
            if line.startswith("// url: "):
                url=line[8:]
            if line.startswith("/* longdesc:"):
                in_long_desc=True
        print(f"   \x1b[34m Name \x1b[0m     is \x1b[32m'{name}'\x1b[0m")
        print(f"   \x1b[34m Desc \x1b[0m     is \x1b[32m'{desc}'\x1b[0m")
        print(f"   \x1b[34m URL \x1b[0m      is \x1b[32m'{url}'\x1b[0m")
        print(f"   \x1b[34m Long desc \x1b[0mis \x1b[32m'{long_desc}'\x1b[0m")
        print(f"   \x1b[34m Arg name \x1b[0m is \x1b[32m'{arg_name}'\x1b[0m")
        content+=f"""
<a href="{fname.replace(".js",".html")}" class="card">
    <div class="card">
        <h2>{name}</h2>
        <p class="desc">{desc}</p>
    </div>
</a>
"""
        about=""
        if long_desc:
            about+=f"""
<h2>Long description</h2>
<p>{long_desc}</p>"""
        if url:
            about+=f"<a href=\"{url}\" target=\"_blank\">Wikipedia</a>"
        
        with open(fname.replace(".js",".html"),'w') as wf:
            wf.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Calculating pi in {len(files)} different ways">
    <title>Calculating Pi | {name}</title>
    <link rel="stylesheet" href="public/style.css">
</head>
<body>
    <header>
        <h1><a href="index.html">Calculating Pi</a></h1>
    </header>

    <main>
        <noscript>
            <div style="margin: 10px; border: 1px solid red; border-radius: 5px; background-color: rgba(255,0,0,0.1); padding: 10px">
                <h1>Warning!</h1>
                <p>This website doesn't work without JavaScript!</p>
            </div>
        </noscript>

        <h1>{name}</h1>

        <hr>

        <label for="arg">{arg_name.capitalize()}: </label>
        <input type="number" min="0" step="1" value="10" name="arg" id="arg">

        <br style="margin-bottom: 0.5em">

        <button onclick="run()">Calculate</button>
        
        <pre class="log">Output log:
<span id="log"></span></pre>

        <hr>

        {about}

        <script src="methods/{fname}"></script>
        <script src="public/runner.js"></script>
        
    </main>

    <footer>
        <div>
            <p><a href="https://github.com/CalSch/pi">GitHub Repo</a></p>
			<p>Made by <a href="https://github.com/CalSch">CalSch</a></p>
		</div>
    </footer>

</body>
</html>""")

html=f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Calculating pi in {len(files)} different ways">
    <title>Calculating Pi</title>
    <link rel="stylesheet" href="public/style.css">
</head>
<body>
    <header>
        <h1><a href="index.html">Calculating Pi</a></h1>
    </header>

    <main>
        <noscript>
            <div style="margin: 10px; border: 1px solid red; border-radius: 5px; background-color: rgba(255,0,0,0.1); padding: 10px">
                <h1>Warning!</h1>
                <p>This website doesn't work without JavaScript!</p>
            </div>
        </noscript>

        {content}
        
    </main>

    <footer>
        <div>
            <p><a href="https://github.com/CalSch/pi">GitHub Repo</a></p>
			<p>Made by <a href="https://github.com/CalSch">CalSch</a></p>
		</div>
    </footer>

</body>
</html>"""

with open("index.html",'w') as f:
    f.write(html)