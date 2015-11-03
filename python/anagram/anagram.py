def detect_anagrams(word, list_words):
		return [w for w in list_words if word.lower() != w.lower() and sorted(word.lower()) == sorted(w.lower())]
		

	
