strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''

for word in strings:
  sentence += word + " "

# Now trim the trailing space
# or sentence = sentence.strip()
sentence = sentence[:-1]

print("Concatenation via for loop: %s" % sentence)
print("Concatenation via str.join: %s" % " ".join(strings))
