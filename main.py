"""Main script for running the book generation system"""
from config import get_config
from agents import BookAgents
from book_generator import BookGenerator
from outline_generator import OutlineGenerator

def main():
    # Get configuration
    agent_config = get_config()

    
    # Initial prompt for the book
    initial_prompt = """
    Create a Ghanaian folklore story that embodies traditional storytelling elements with local flavor and wisdom. The story should feature well-known folklore characters like Kweku Ananse, the cunning trickster, alongside figures such as Tortoise (akyekyedeɛ), Owl (patuo), and the wise Ohene Amasa, set in a vibrant Ghanaian village.

The story should incorporate proverbs, riddles, and cultural values such as community unity, patience, honesty, and wit, weaving lessons into the narrative. The setting should reflect a typical Ghanaian village, complete with bustling market scenes, evening storytelling under the baobab tree, and traditional ceremonies featuring kente, adowa dance, and the sounds of the talking drum.

Story Structure:

Setup: Ananse hears of a magical talking drum hidden deep in the forest, said to grant great wisdom and fortune to whoever possesses it.
Initial Conflict: The village elders announce a challenge—whoever brings the drum back will earn the title of "The Wisest of All." Ananse, akyekyedeɛ, and patuo each set off on the quest.
Rising Action: Ananse uses his trickery to outwit his competitors but faces unexpected trials from spirits of the forest (Mmoatia).
Climax: Upon finding the drum, Ananse must solve a riddle posed by the ancestors to claim it.
Resolution: Ananse learns that true wisdom comes not from trickery but from humility and teamwork.
Characters:

Kweku Ananse: Cunning and always seeking an easy way out, yet lovable and relatable.
akyekyedeɛ (Tortoise): Slow but wise and persistent.
patuo (Owl): Keeper of ancient wisdom, mysterious and observant.
Ohene Amasa: The respected leader, fair and just.
Mmoatia (Forest Spirits): Mischievous and wise beings who test the challengers.

Themes:
The value of wisdom over cunning.
The importance of community and collaboration.
Respect for tradition and elders.
Cultural Elements:
Include descriptions of Ghanaian foods like fufu and light soup, the beauty of kente cloth, the significance of adinkra symbols, and interactions in Twi phrases such as:

"Ananse, wo ho te sɛn?" (Ananse, how are you?)
"Ɛyɛ, me da ase." (I’m fine, thank you.)
"""

    num_chapters = 5
    # Create agents
    outline_agents = BookAgents(agent_config)
    agents = outline_agents.create_agents(initial_prompt, num_chapters)
    
    # Generate the outline
    outline_gen = OutlineGenerator(agents, agent_config)
    print("Generating book outline...")
    outline = outline_gen.generate_outline(initial_prompt, num_chapters)
    
    # Create new agents with outline context
    book_agents = BookAgents(agent_config, outline)
    agents_with_context = book_agents.create_agents(initial_prompt, num_chapters)
    
    # Initialize book generator with contextual agents
    book_gen = BookGenerator(agents_with_context, agent_config, outline)
    
    # Print the generated outline
    print("\nGenerated Outline:")
    for chapter in outline:
        print(f"\nChapter {chapter['chapter_number']}: {chapter['title']}")
        print("-" * 50)
        print(chapter['prompt'])
    
    # Save the outline for reference
    print("\nSaving outline to file...")
    with open("book_output/outline.txt", "w", encoding="utf-8") as f:
        for chapter in outline:
            f.write(f"\nChapter {chapter['chapter_number']}: {chapter['title']}\n")
            f.write("-" * 50 + "\n")
            f.write(chapter['prompt'] + "\n")
    
    # Generate the book using the outline
    print("\nGenerating book chapters...")
    if outline:
        book_gen.generate_book(outline)
    else:
        print("Error: No outline was generated.")

if __name__ == "__main__":
    main()