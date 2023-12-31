from datetime import datetime
from django.utils.text import slugify

posts = [
    {
        "id": 1,
        "title": "An introduction to the Django Python web app framework",
        "banner": "bg-django",
        "pub_date": datetime.strptime("2023-04-12", "%Y-%m-%d").strftime("%B %d, %Y"),
        "author": "Nicholas Hunt-Walker",
        "content": """<h1>About Django</h1>
            <p>Django styles itself as "a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel." And they really mean it! This massive web framework comes with so many batteries included that oftentimes during development it can be a mystery as to how everything manages to work together.</p>
            In addition to the framework itself being large, the Django community is absolutely massive. In fact, it's so big and active that there's a whole website devoted to the third-party packages people have designed to plug into Django to do a whole host of things. This includes everything from authentication and authorization, to full-on Django-powered content management systems, to e-commerce add-ons, to integrations with Stripe. Talk about not re-inventing the wheel; chances are if you want something done with Django, someone has already done it and you can just pull it into your project.
            For this purpose, we want to build a REST API with Django, so we'll leverage the always popular Django REST framework. Its job is to turn the Django framework, which was made to serve fully rendered HTML pages built with Django's own templating engine, into a system specifically geared toward effectively handling REST interactions. Let's get going with that.
            """
    },
    {
        "id": 2,
        "title": "What is Python? Powerful, intuitive programming",
        "banner": "bg-python",
        "pub_date": datetime.strptime("2023-01-07", "%Y-%m-%d").strftime("%B %d, %Y"),
        "author": "Serdar Yegulalp",
        "content": """<h1>Python is easy to learn and use</h1>
            <p>Python encompasses a relatively modest number of features, so it requires a fairly minimal investment of time and effort to produce your first programs. Python's syntax is designed to be readable and straightforward. This simplicity makes it an ideal teaching language, which newcomers can pick up quickly. As a result, developers can spend more time thinking about the problem they’re trying to solve, rather than worrying about syntactic complexities or deciphering legacy code.</p>
            <h2>Python is broadly adopted and supported</h2>
            <p>Python is both popular and widely used, as the high rankings in surveys like the Tiobe Index and the large number of GitHub projects using Python attest. Python runs on every major operating system and platform, and most minor ones, too. Many major libraries and API-powered services have Python bindings or wrappers, so Python interfaces freely with them. </p>
            """
    },
    {
        "id": 3,
        "title": "17 Great Articles About JavaScript",
        "banner": "bg-js",
        "pub_date": datetime.strptime("2021-03-26", "%Y-%m-%d").strftime("%B %d, %Y"),
        "author": "John Mwakalinga",
        "content": """<h1>About JavaScript</h1>
                    <p>Penumbra is a new tab replacement for chrome in the form of an extension. It overrides the existing new tab to give some very minimal add-ons or features.
                    </p>

                    <p>The main problem that I have with default new tab is that it is little too simple. It limits users to only eight shortcuts and it uses favicons of those websites for the preview. The favicons are usually very small (16×16px) and when they are used anywhere other than the tab they look blurry. This pet peeve forced me to create my own Chrome extension with subtle traits that I like.</p>

                    <p>There’s plethora of new tab replacements out there. But they either try to have prolific features that it becomes nuisance to use or so little that I start wondering what’s the point.</p>
                    """
    },
    {
        "id": 4,
        "title": "Why is Rust Language Becoming Popular and Should You Learn it?",
        "banner": "bg-rust",
        "pub_date": datetime.strptime("2023-01-27", "%Y-%m-%d").strftime("%B %d, %Y"),
        "author": "Rounak Sharma",
        "content": """<h1>What is the Rust Programming Language Used For?</h1>
                    <p>Rust is a modern computer programming language developed by Mozilla in 2010. It was initially developed to build high-programming applications without the issue of invalid memory access that developers were facing while using C and C++. This system programming language facilitates designing and writing computer programs that allow smooth integration of computer hardware and software. </p>

                    <p>The main purpose of using Rust is enhanced safety, speed, and concurrency, or the ability to run multiple computations parallelly. In simple words, Rust is used for three essential purposes in programming; performance, safety, and memory management. Hence, Rust is used to develop advanced applications like gaming engines, operating systems, and browsers that demand scalability.</p>

                    <h2>Why Should You Learn Rust Programming Language?</h2>
                    <p>Rust is an advanced programming language that is beneficial to build tech applications that align with modern Information Technology (IT) architecture requirements. Here are the top four reasons why you should learn Rust:</p>
                    
                    <ol>
                        <li>Rust facilitates easy scalability and concurrency and is suitable for building heavy applications to meet the increasing tech demands in the modern world.</li>
                        <li>It uses a logical and functional syntax that allows developers to handle low-level programming for IoT (Internet of Things) applications.</li>
                        <li>The old codes in Rust are compatible with the newer versions of the language.</li>
                        <li>Rust has an asynchronous processing model that allows developers to create and run independent functions, which can be collaborated later.</li>
                    </ol>
                    """
    }
]

for post in posts:
    post["slug"] = slugify(post["title"])
