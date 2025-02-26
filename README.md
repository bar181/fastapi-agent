# FastAPI Agent System

A FastAPI-based dynamic agent system that leverages the ReACT methodology for building autonomous and human-in-the-loop agents.

## Features
- Dynamic agent loading and execution
- Multiple agent support with dedicated endpoints
- Agent listing and discovery endpoint
- Health check endpoint
- Error handling
- Comprehensive test suite
- Token-based authorization (for math agent)
- Advanced text processing (classifier and summarizer agents)

## Project Structure
```
fastapi-agent-system/
├─ app/
│   ├─ main.py          # FastAPI application entrypoint
│   └─ models.py        # (For future use: data models)
├─ agents/
│   ├─ __init__.py      # Package initializer
│   ├─ hello_world.py   # Hello World agent
│   ├─ goodbye.py       # Goodbye agent
│   ├─ math.py          # Math agent with token verification
│   ├─ classifier.py    # Text classification agent
│   ├─ summarizer.py    # Text summarization agent
│   ├─ echo.py          # Echo message agent
│   ├─ time.py          # Current time agent
│   ├─ joke.py          # Random joke agent
│   └─ quote.py         # Inspirational quote agent
├─ docs/                # Documentation
├─ tests/               # Test suite
├─ requirements.txt     # Dependencies
└─ LICENSE             # MIT License
```

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn app.main:app --reload
```

3. Test the endpoints:

Core Endpoints:
- Welcome message: GET /
- Health check: GET /health
- List all agents: GET /agents

Simple Agents (No Parameters):
- Hello World: GET /agent/hello_world
- Goodbye: GET /agent/goodbye
- Echo: GET /agent/echo
- Time: GET /agent/time
- Joke: GET /agent/joke
- Quote: GET /agent/quote

Advanced Agents (With Parameters):
- Math: GET /agent/math?token=MATH_SECRET&expression=3*(4%2B2)
- Classifier: GET /agent/classifier?INPUT_TEXT=Hello,%20how%20are%20you?
- Summarizer: GET /agent/summarizer?TEXT_TO_SUMMARIZE=FastAPI%20is%20efficient.

Example Usage:
```bash
# Start the server
uvicorn app.main:app --reload

# Test an endpoint (replace SERVER_URL with your server address)
curl SERVER_URL/agent/hello_world

# Test with parameters
curl "SERVER_URL/agent/math?token=MATH_SECRET&expression=3*(4%2B2)"
```

## Running Tests
```bash
pytest tests/
```

## Documentation
- [Implementation Guide](docs/Implementation_Guide.md)
- [Testing Documentation](docs/Testing_and_Validation.md)
- [Technical Specifications](docs/Technical_Specifications.md)


## This repository was created using Documentation First Coding Methodologies

Our development process followed a rigorous Documentation First approach:

1. **Brainstorm and Design:**  
   Initial ideas and designs were discussed and documented to establish project goals.

2. **Required Documentation:**  
   All technical and implementation documents were created and saved in the `/docs` directory.

3. **Phase Plans:**  
   Detailed plans for each development phase were created and are available in the `/plans` folder.

4. **Step-by-Step Execution:**  
   Development followed the step-by-step outlines provided in each phase, including comprehensive tests.

5. **Tracking and Logging:**  
   Every step of the process was tracked and logged in the `/logs` directory for transparency.

6. **Testing and Updates:**  
   Appropriate tests were implemented and documentation was continuously updated to reflect the current state of the project.



## Original Gist
https://gist.github.com/bar181/7fc0286841a38c72848ed037d0e561fd
### Author: Bradley Ross (bar181 on gists and github)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
