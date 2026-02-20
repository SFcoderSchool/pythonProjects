#twitch chat emote system using dictionarys, translating words to specific emojis in a paragragh

emojis = {
  "happy": "😊",
  "smile": "😄",
  "grin": "😁",
  "laugh": "😂",
  "joy": "🤣",
  "wink": "😉",
  "love": "😍",
  "kiss": "😘",
  "cool": "😎",
  "thinking": "🤔",
  "confused": "😕",
  "surprised": "😲",
  "shocked": "😱",
  "sad": "😢",
  "cry": "😭",
  "angry": "😠",
  "rage": "🤬",
  "sleepy": "😴",
  "sick": "🤒",
  "neutral": "😐"
}
keywords = emojis.keys()
keywords = list(keywords)

phrase = "I am happy today"

while True:
  phrase = input("How are you? ")
  phrase = phrase.lower()

  words = phrase.split(" ")
  new_phrase = []

  for i in range(len(words)):
    if words[i] in keywords:
      new_phrase.append(emojis[words[i]])
    else:
      new_phrase.append(words[i])

  new_phrase = " ".join(new_phrase)
  print("phrase with emojis:")
  print(new_phrase)