# AI book Writer

A Python-based system that uses AutoGen to generate complete books through collaborative AI agents. The system employs multiple specialized agents working together to create coherent, structured narratives from initial prompts.

## Features

- Multi-agent collaborative writing system
- Structured chapter generation with consistent formatting
- Maintains story continuity and character development
- Automated world-building and setting management
- Support for complex, multi-chapter narratives
- Built-in validation and error handling
- Export story as a pdf file
- Generation of story book covers

## Architecture

The system uses several specialized agents:

- **Story Planner**: Creates high-level story arcs and plot points
- **World Builder**: Establishes and maintains consistent settings
- **Memory Keeper**: Tracks continuity and context
- **Writer**: Generates the actual prose
- **Editor**: Reviews and improves content
- **Outline Creator**: Creates detailed chapter outlines
- **pdf generator**: Converts generated story into pdf

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/autogen-book-generator.git
cd autogen-book-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Basic usage:
```python
from main import main

if __name__ == "__main__":
    main()
```

2. Custom initial prompt:
```python
from config import get_config
from agents import BookAgents
from book_generator import BookGenerator
from outline_generator import OutlineGenerator

# Get configuration
agent_config = get_config()

# Create agents
outline_agents = BookAgents(agent_config)
agents = outline_agents.create_agents()

# Generate outline
outline_gen = OutlineGenerator(agents, agent_config)
outline = outline_gen.generate_outline(your_prompt, num_chapters=25)

# Initialize book generator
book_agents = BookAgents(agent_config, outline)
agents_with_context = book_agents.create_agents()
book_gen = BookGenerator(agents_with_context, agent_config, outline)

# Generate book
book_gen.generate_book(outline)
```

## Configuration

The system can be configured through `config.py`. Key configurations include:

- LLM endpoint URL
- Number of chapters
- Agent parameters
- Output directory settings

## Output Structure

Generated content is saved in the `book_output` directory:
```
book_output/
├── outline.txt
├── chapter_01.txt
├── chapter_02.txt
└── ...
```

## Requirements

- Python 3.8+
- AutoGen 0.2.0+
- Other dependencies listed in requirements.txt

## Development

To contribute to the project:

1. Fork the repository
2. Create a new branch for your feature
3. Install development dependencies:
```bash
pip install -r requirements.txt
```
4. Make your changes
5. Run tests:
```bash
pytest
```
6. Submit a pull request

## Error Handling

The system includes robust error handling:
- Validates chapter completeness
- Ensures proper formatting
- Maintains backup copies of generated content
- Implements retry logic for failed generations

## Limitations

- Requires significant computational resources
- Generation time increases with chapter count
- Quality depends on the underlying LLM model
- May require manual review for final polish

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built using the [AutoGen](https://github.com/microsoft/autogen) framework
- Inspired by collaborative writing systems
