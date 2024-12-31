import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool
import os
from crewai import LLM
load_dotenv()

# Set the API key for the SerperDevTool
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7
)

# Define Agents
topic_researcher = Agent(
    role='Topic Researcher',
    goal='Search for only 1 relevant resources on the topic {topic} from the web',
    verbose=True,
    memory=True,
    backstory='Expert in finding and analyzing relevant content from Web, specializing in AI, Data Science, Machine Learning, and Generative AI topics.',
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

blog_writer = Agent(
    role='Blog Writer',
    goal='Write a comprehensive blog post from the only 1 article  provided by the Topic Researcher, covering all necessary sections',
    verbose=True,
    memory=True,
    backstory='Experienced in creating in-depth, well-structured blog posts that explain technical concepts clearly and engage readers from introduction to conclusion.',
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

linkedin_post_agent = Agent(
    role='LinkedIn Post Creator',
    goal='Create a concise LinkedIn post summary from the transcription provided by the Topic Researcher.',
    verbose=True,
    memory=True,
    backstory='Expert in crafting engaging LinkedIn posts that summarize complex topics and include trending hashtags for maximum visibility.',
    tools=[tool],
    llm=llm,
    allow_delegation=True

)
# Define Tasks
research_task = Task(
    description="Identify and analyze only 1 content or  article on the {topic} from the web.",
    expected_output="A complete word-by-word report on the most relevant post or article found on the topic {topic}.",
    agent=topic_researcher,
    tools=[tool]
)

blog_writing_task = Task(
    description="""Write a comprehensive blog post based on the 1 article  provided by the Topic Researcher.
                   The article must include an introduction, step-by-step guides, and conclusion.
                   The overall content must be about 400 words long.""",
    expected_output="A markdown-formatted blog post",
    agent=blog_writer,
    tools=[tool],
    output_file='./artifects/blog-post.md'
)

linkedin_post_task = Task(
    description="Create a LinkedIn post summarizing the key points from the transcription provided by the Topic Researcher, including relevant hashtags.",
    expected_output="A markdown-formatted LinkedIn post",
    agent=linkedin_post_agent,
    tools=[tool],
    output_file='./artifects/linkedin-post.md'
)

# Create Crew
my_crew = Crew(
    agents=[topic_researcher, linkedin_post_agent, blog_writer],
    tasks=[research_task, linkedin_post_task, blog_writing_task],
    verbose=True,
    process=Process.sequential
    
)

# Input Topic
topic_of_interest = 'gemini 2.0 multimodel'
result = my_crew.kickoff(inputs={'topic': topic_of_interest})

print(result)
