import string
from collections import Counter

def analyze_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
        return

    # Basic stats
    num_lines = text.count("\n") + 1 if text else 0
    num_chars = len(text)
    words = text.split()
    num_words = len(words)

    # Clean words for frequency analysis (remove punctuation, lowercase)
    translator = str.maketrans("", "", string.punctuation)
    cleaned_words = [w.lower().translate(translator) for w in words if w.strip()]
    
    word_freq = Counter(cleaned_words)

    # Print structured results
    print("📊 Text File Analysis Report (Project: JKUAD0910)")
    print("=" * 50)
    print(f"Lines:       {num_lines}")
    print(f"Words:       {num_words}")
    print(f"Characters:  {num_chars}")
    print("\n🔝 Top 10 Most Common Words:")
    print("-" * 50)
    for word, count in word_freq.most_common(10):
        print(f"{word:15} {count}")

    print("\n✅ Analysis complete. Tagged under: JKUAD0910")

if __name__ == "__main__":
    filename = input("Enter filename (e.g., sample.txt): ").strip()
    analyze_file(filename)
