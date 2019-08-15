"""process data"""

LINE_FILEDS = ['lineID', 'speakerID', 'movieID', 'speakerName', 'text']
CONVERSATION_FILEDS = ['speaker1ID', 'speaker2ID', 'movieID', 'utterances']

linepath = './data/cornell movie-dialogs corpus/movie_lines.txt'
conversationpath = './data/cornell movie-dialogs corpus/movie_conversations.txt'

def readline(path, fields):
    with open(path, 'r') as file:
        print(type(file))

if __name__ == '__main__':
    readline(linepath, LINE_FILEDS)