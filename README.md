# Blog-Post-Agentic_AI-Writer

This project demonstrates how to use **CrewAI** in conjunction with **SerperDevTool** to automate content creation workflows. The project is structured to research a topic from the web, create a detailed blog post based on the research, and summarize the findings for a LinkedIn post. This process is powered by **Agents**, **Tasks**, and the **Gemini** model for natural language processing.

## Introduction

This project automates the process of gathering relevant resources from the web and generating content in multiple formats (a blog post and a LinkedIn post). It utilizes **CrewAI**, a framework designed to facilitate collaborative workflows across multiple intelligent agents. Each agent performs a specific task, with the entire process orchestrated through **Tasks** and **Crew**.

The flow of the process starts with the **Topic Researcher** agent searching for the most relevant resource related to a given topic. The **Blog Writer** agent then uses this resource to create a blog post, and finally, the **LinkedIn Post Creator** agent summarizes the content into a concise LinkedIn post.

## Dependencies

Before running the project, ensure that the following dependencies are installed:

- `crewai`: Framework for building and managing intelligent agents
- `crewai_tools`: A collection of pre-built tools for interacting with APIs
- `python-dotenv`: Loads environment variables from `.env` files
- `SerperDevTool`: A tool for internet searching using Serper API

Install the necessary dependencies using `pip`:

```bash
pip install crewai crewai_tools python-dotenv requests

```

# How It Works

## CrewAI

**CrewAI** is a framework that allows the creation and orchestration of intelligent agents that can work in tandem on different tasks. It defines agents, tools, tasks, and processes in a modular fashion, enabling automated workflows.

### Agents:
- Each agent is assigned a specific role and goal.
- They use tools (such as search engines or data processors) and LLMs (language models) to perform tasks.

### Tasks:
- A task describes the specific work an agent must complete.
- It includes inputs, expected outputs, and tools required for execution.

### Tools:
- Tools are utilities or APIs that agents can use to perform tasks.
- For instance, a tool could be an API to search the web, analyze text, or format a document.

### Process:
- This defines the sequence in which tasks are executed.
- It can be set as **sequential** or **parallel**.

## Agents

In this project, we define three agents, each with specific roles and goals:

### Topic Researcher:

- **Role**: Search for relevant content on the web about a specific topic.
- **Goal**: Find 1 relevant resource that matches the given topic.
- **Tools**: Uses the `SerperDevTool` to search the web for articles.
- **LLM**: The LLM model is used to process and interpret the information from the web search.

### Blog Writer:

- **Role**: Write a comprehensive blog post based on the resource provided by the Topic Researcher.
- **Goal**: Create a detailed blog post with an introduction, step-by-step guide, and conclusion.
- **Tools**: Uses the `SerperDevTool` for research and article analysis, if needed.
- **LLM**: The LLM is used to generate coherent, readable content.

### LinkedIn Post Creator:

- **Role**: Create a LinkedIn post summarizing key insights from the article provided by the Topic Researcher.
- **Goal**: Condense the article into a concise summary, including hashtags for visibility.
- **Tools**: Similar to the Blog Writer, this agent uses the `SerperDevTool` to gather insights.
- **LLM**: The LLM is employed to generate the post content, ensuring it is clear and engaging.

## Tools

### SerperDevTool:
- A tool designed for web searching, utilizing the Serper API. It allows agents to perform web searches to find relevant content.
- **Usage**: This tool is used by agents to gather resources related to the specified topic.

## LLM Model

The language model used in this project is **Gemini-1.5-Flash** by Google. It is used to:

- Process and summarize text.
- Generate human-like content, including blog posts and social media posts.
- Analyze the content found by the Topic Researcher agent to extract key information and rephrase it into readable formats for the blog and LinkedIn post.

### Key Features of the LLM:
- **Model**: `gemini/gemini-1.5-flash`
- **Temperature**: 0.7 (controls the creativity of the generated text)

This model is integrated into each agent and provides the power to create high-quality content from simple inputs.

# Setting Up

## Set up environment variables:
Create a `.env` file in the project directory and define your API keys:

```plaintext
SERPER_API_KEY=your_serper_api_key
GEMINI_API_KEY=your_gemini_api_key
```

# Usage

## Defining the Topic
The `topic_of_interest` variable is used to define the subject you want to explore. For example, if the topic is **"Gemini 2.0 Multimodel"**, you would set:

```python
topic_of_interest = 'gemini 2.0 multimodel'
```

# Kicking off the Crew
The ```python my_crew.kickoff()```  function is used to start the entire process. This initiates the tasks for all agents, triggering the sequence of actions from the Topic Researcher, Blog Writer, and LinkedIn Post Creator agents. The function will output the result, which can include a blog post or LinkedIn summary, depending on the tasks you have configured.

# Viewing the Results

Once the agents have completed their tasks, the generated content will be saved as markdown files:

- `./artifacts/blog-post.md`: Contains the blog post created by the **Blog Writer** agent.
- `./artifacts/linkedin-post.md`: Contains the LinkedIn post summary created by the **LinkedIn Post Creator** agent.

You can open these markdown files for further editing or directly publish them on your desired platform.

# Conclusion
This project demonstrates how CrewAI can be utilized to build an intelligent, collaborative process between different agents for content generation. By integrating SerperDevTool for web research and Gemini LLM for content creation, the project automates and streamlines the process of researching and writing content, making it both more efficient and scalable.



