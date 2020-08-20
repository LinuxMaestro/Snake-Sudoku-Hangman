with open("engmix.txt", "r") as vocabulary:
    words = vocabulary.read().split()

# LIFE, IT WILL BE THE LIST OF "CHARACTERS" THAT SYMBOLIZES
# PLAYER'S LIFE
chances = [
"""
-----------------|
                 |
               \\0\\
                 """,
"""
-----------------|
                 |
                 0
                 """,
"""
-----------------|
                 |
                 0
                 |
                 """,
"""
-----------------|
                 |
                 0
                /|
                 """,
"""
-----------------|
                 |
                 0
                /|\\
                 """,
"""
-----------------|
                 |
                 0
                /|\\
                 /
                 """,
"""
-----------------|
                 |
                 0
                /|\\
                /\\
                 """
]
welcome_message = """Welcome to my first beginner project!
 H A N G M A N!!!"""