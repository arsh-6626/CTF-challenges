# app.py
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Sample blog posts
POSTS = [
    {
        'title': 'My Flight to Past',
        'id':1,
        'date': datetime(2025, 1, 22),
        'category': 'chess',
        'content': """
            On Flight VJH643, at 1:18 AM, I found myself lost in thought, staring out at the dark expanse below. My mind drifted back to a historic chess match from 1981, played somewhere beneath these very skies. The contenders? A Grandmaster world champion and his tenacious rival, battling in a game that has since become the stuff of legend.
            Inspired by the Grandmaster’s brilliance, I set up my miniature chessboard and played the opening he was renowned for. Each move resonated with echoes of the past, but the climax—the final three moves—eluded me.
            Can you uncover them? The truth lies some'w'here in the archives of chess history. The answer is a challenge for the observant, the curious, and those who dare to delve into the game’s intricate beauty.
            As the plane began its descent, I smiled, knowing some mysteries are meant to be solved by those who seek them.
            
            The game name reminds me of a movie scene maybe i will post about it someday

            https://www.chess.com/game/122344308904 (here is my imitation of the chessboard)
            """,
        'author': ' Stacy',
        'read_time': '5 min'
    },
    {
        'title': 'The Jungle Book and the Grand Chessboard of Strategy',
        'id':7,        
        'date': datetime(2025, 2, 8),
        'category': 'tech',
        'content': """
        Rudyard Kipling’s The Jungle Book is a tale of survival, adaptation, and the delicate balance of power in a world ruled by instinct and wisdom. Much like a game of chess, the jungle is a battlefield where every creature, from the mighty Shere Khan to the cunning Bagheera, plays a distinct role in the grand strategy of life. What if we viewed The Jungle Book through the lens of chess? How do its characters embody the timeless strategies of this revered game?
        The King – Mowgli
        At the heart of the story, Mowgli represents the King in chess—a figure that must be protected at all costs. While the King is not the most powerful piece, the game revolves around his survival, much like Mowgli’s journey of self-preservation in the jungle. He is vulnerable, yet the entire jungle reacts to his presence, whether to protect or hunt him.
        The Queen – Bagheera
        The Queen is the most versatile and powerful piece on the board, much like Bagheera, the black panther. He is Mowgli’s protector and guide, possessing strength, speed, and intelligence. Bagheera’s ability to maneuver through different situations mirrors the Queen’s ability to dominate the board, making calculated moves to safeguard Mowgli’s path.
        The Rook – Baloo
        Baloo, the wise and carefree bear, plays the role of the rook. The rook moves in straight lines, embodying steadfastness and reliability. Baloo offers wisdom, mentorship, and brute strength when needed. Though he may seem slow and easygoing, his role in shaping Mowgli’s understanding of the jungle is invaluable, much like how the rook provides structure and control on the chessboard.
        The Bishop – Kaa
        The hypnotic python, Kaa, aligns well with the bishop. Bishops move diagonally, often catching opponents off guard, just as Kaa’s mesmerizing gaze disarms his victims. Kaa is neither entirely friend nor foe—he is unpredictable, like a well-placed bishop that can be a game-changer when used strategically.
        The Knight – Shere Khan
        Shere Khan, the formidable tiger, embodies the knight. The knight moves in an L-shape, making it an unpredictable force on the chessboard. Similarly, Shere Khan is a looming threat, always approaching from unexpected angles. His pride and cunning nature force others to react, much like how a knight’s movement can create complex threats in a chess game.
        The Pawns – The Wolf Pack
        The wolves that raise Mowgli function like the pawns in chess. Pawns are the foundation of the game, providing structure and protection. The wolf pack nurtures Mowgli, offering him safety and guidance. Though pawns seem insignificant, they can advance and promote into a powerful piece—just as Mowgli, the jungle’s pawn, evolves into a formidable force capable of challenging even Shere Khan.
        The Endgame – A Lesson in Strategy
        Just like in chess, survival in The Jungle Book depends on strategy, alliances, and sacrifices. Every character, like a chess piece, has a unique role in shaping Mowgli’s fate. By understanding their strengths and limitations, Mowgli navigates the dangers of the jungle, much like a skilled chess player calculating their moves on the board.
        In the end, both The Jungle Book and chess teach us about patience, adaptability, and the importance of making the right moves at the right time. Whether in the dense wilderness or on the 64 squares of a chessboard, the key to victory lies in understanding the game and playing it wisely.

        https://youtu.be/CAm_bonffcQ?t=266

        """,
        'author': 'Stacy',
        'read_time': '8 min'
    },
    {
        'title': 'Weird Game',
        'id':2,
        'date': datetime(2024, 2, 5),
        'category': 'tech',
        'content': 'Quantum computing is poised to revolutionize the way we process information...',
        'author': 'Prof. Maria Rodriguez',
        'read_time': '6 min'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=POSTS)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in POSTS if post['id'] == post_id), None)
    if post is None:
        abort(404)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)