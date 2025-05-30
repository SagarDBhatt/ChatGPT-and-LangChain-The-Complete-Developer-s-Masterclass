# ChatGPT-and-LangChain-The-Complete-Developer-s-Masterclass
Udemy course on "Intensive masterclass on ChatGPT, LangChain, and Python. Make production-ready apps focused on real-world AI integration"

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
My notes on lectures and topics in simple words. 

May 27th, 2025

4) Install openai package: $pip install openai
    - Note: $pip show openai command will show openai version which is 0.27. This is older version and does not have AzureOpenAI classes. (Only available over 1.0.0 version)
    - $pip install --upgrade "openai>=1.0.0" command to update the openai to newer version.
3) Start the virtual env : $pipenv shell


May 25th, 2025

1) PDF.ai is a web application which takes the PDF and then user can ask any question from the PDF. 
=> There are 2 approaches. a) Send the entire PDF and question to chatGPT. But this will fail because of token error. 

=> b) We can OCR the PDF, chunk the OCR text and then send users question with most relevant chunk of OCR text and then answer users question. (We will develop this approach)
--> Chunk size usually 1000 characters long. But can be configured. 
--> chatGPT model use raw essence of each chunk of text by embeddings (Using Embedding Creation Algorithm). Embeddings is nothing but the array of numbers with the size of 1536 elements/ digits. Each digits represents what could be the essense of the text.
--> So in other words, the E2E flow is : Upload PDF <-> Parse Text from PDF <-> Break text into chunks <-> Embeddings to find essence of each chunk <-> Find most relevant chunk using embeddings and store in vector DB <-> Format question + chunk into prompt <-> get answer from chatGPT

2) What is LangChain?
=> LangChain is the tool to automate all the above steps of E2E flow. Like to read PDF, chunking, embeddings, Prompting and more stages can be automate using LangChain.




++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

What you'll learn
Integrate ChatGPT into production-style apps with LangChain
Use LangChain components to build complex text generation pipelines
Enhance ChatGPT's output by automatically integrating user feedback
Teach ChatGPT new facts through Retrieval Augmented Generation
Extend LangChain to implement server-to-browser text streaming
Use OpenAI Plugins to add new capabilities to ChatGPT, such as database access and code execution
Understand every line of code we write so you can use these exact same techniques on your own projects
Build your own chat-with-a-PDF web application, complete with document upload and authentication
See how users interact with your chat features using observability and tracing
Description
You've found the most advanced, most complete, and most intensive masterclass online for learning how to integrate LangChain and ChatGPT into production-ready applications!

Thousands of engineers have learned how to build amazing applications using ChatGPT, and you can too. This course uses a time-tested, battle-proven method to make sure you understand exactly how ChatGPT works, and is the perfect pathway to help you get a new job as a software engineer working on AI-enabled apps.

The difference between this course and all the others: you will go far beyond the basics of simple ChatGPT prompts, and understand how companies are integrating text generation into their apps today.

___________

ChatGPT is being used across industries to enhance applications with text generation. But with this new feature comes many challenges:

Building complex text generation pipelines that incorporate outside information

Creating reusable configuration components that can be reassembled in different ways

Applying user feedback (like upvotes/downvotes) to enhance ChatGPT's output

Wiring in observability and tracing to see how users are interacting with your AI

Generate text performantly using distributed processing

This course will walk you through production-ready, repeatable techniques for addressing each of these challenges and many more.



What will you build?

This course focuses on creating a series of different projects of increasing complexity. You'll start from the very basics, understanding how to access ChatGPT 4 programatically.  From there, we will quickly increase in complexity, building more complex projects with many more features. By the end, you will make a fully-featured web app that implements a "Chat-with-a-PDF" feature. Note: no previous web development experience is required.

Here's a partial list of some of the topics you'll cover:

Understand how complex text-generation pipelines work

Write reusable code using chains provided by LangChain

Connect chains together in different ways to dramatically change your apps behavior with ease

Store, retrieve, and summarize chat messages using conversational memory

Implement semantic search for Retrieval-Augmented Generation using embeddings

Generate and store embeddings in vector databases like ChromaDB and Pinecone

Use retrievers to refine, reduce, and rank context documents, teaching ChatGPT new information

Create agents to automatically accomplish tasks for you using goals you define

Write tools and plugins to allow ChatGPT to access the outside world

Maintain a consistent focus on performance through distributed processing using Celery and Redis

Extend LangChain to implement server-to-browser text streaming

Improve ChatGPT's output quality through user-generated feedback mechanisms

Get visibility into how users interact with your text generation features by using tracing

There are a ton of courses that show how to use ChatGPT at a very basic level. This is one of the very few courses online that goes far beyond the basics to teach you advanced techniques that top companies are using today. I have a passion for teaching topics the right way - the way that you'll actually use technology in the real world. Sign up today and join me!

Who this course is for:
Software engineers looking to add AI into their apps
Instructor
Stephen Grider
Engineering Architect
Stephen Grider has been building complex Javascript front ends for top corporations in the San Francisco Bay Area.  With an innate ability to simplify complex topics, Stephen has been mentoring engineers beginning their careers in software development for years, and has now expanded that experience onto Udemy, authoring the highest rated React course. He teaches on Udemy to share the knowledge he has gained with other software engineers.  Invest in yourself by learning from Stephen's published courses.

Requirements
Basic programming experience with Python
