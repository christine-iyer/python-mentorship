import pandas as pd
# Creating the DataFrame with missing "Answer" column filled in
data = {
    "Category": [
        "Historical & Political Promises"] * 5 + 
        ["Economic & Business Betrayals"] * 5 + 
        ["Literary & Mythological Betrayals"] * 5 + 
        ["Pop Culture & Entertainment Betrayals"] * 5,
    
    "Question": [
        "Which U.S. president famously promised “Read my lips: no new taxes,” only to later approve a tax increase?",
        "What was the name of the treaty signed in 1919 that was meant to secure lasting peace but ultimately contributed to World War II?",
        "What 1970s political scandal involved a president breaking his promise to be truthful about a break-in at the Democratic National Committee headquarters?",
        "Which country voted to leave the European Union in 2016 after politicians promised it would free up £350 million a week for the NHS—an assertion later discredited?",
        "Which Soviet leader promised reforms under “glasnost” and “perestroika,” only to see the USSR collapse in 1991?",

        "What major company’s 2008 slogan was “Don’t be evil,” a principle critics say was later abandoned?",
        "Which airline promised “you’ll love the way we fly” before suffering one of the worst corporate meltdowns in history in December 2022?",
        "In 1929, what financial catastrophe shattered the belief that stock market prosperity would last forever?",
        "Which fast-food chain was sued for allegedly misleading customers about its “footlong” sandwiches not actually being 12 inches?",
        "Which technology CEO promised to “revolutionize healthcare” with a pinprick blood test, only to be convicted of fraud in 2022?",

        "In Shakespeare’s Julius Caesar, which character breaks his promise of loyalty by assassinating Caesar, prompting the famous last words, “Et tu, Brute?”",
        "What biblical figure sold his birthright for a bowl of stew, later regretting the deal when his brother refused to honor it?",
        "In Game of Thrones, which character violated the sacred “Guest Right” by massacring their dinner guests at the Red Wedding?",
        "Which classic novel revolves around a doctor who breaks his oath to do no harm, creating a monstrous being in the process?",
        "In Greek mythology, which hero broke his vow never to look back while leading his wife out of the underworld, dooming her forever?",

        "Which pop star was criticized for promising no more tears left to cry—only to release another tearful breakup album?",
        "Which 2000s reality show was revealed to have broken its promise of fairness when a contestant exposed its rigged challenges?",
        "Which 1990s sitcom featured an episode about a character making a “Vow of Silence” but immediately spilling the secret?",
        "Which band famously sang, “I promise you I will learn from my mistakes” in 2003, despite releasing more sad breakup songs later?",
        "In The Godfather, what favor does Michael Corleone break his promise to deny, leading to a dramatic betrayal?"
    ],

    "Answer": [
        "George H.W. Bush",
        "Treaty of Versailles",
        "Watergate Scandal",
        "United Kingdom (Brexit)",
        "Mikhail Gorbachev",

        "Google",
        "Southwest Airlines",
        "The Stock Market Crash of 1929",
        "Subway",
        "Elizabeth Holmes (Theranos)",

        "Brutus",
        "Esau",
        "Walder Frey",
        "Frankenstein by Mary Shelley",
        "Orpheus",

        "Ariana Grande",
        "Survivor",
        "Seinfeld",
        "Coldplay",
        "Carlo Rizzi’s execution request"
    ]
}

df = pd.DataFrame(data)

# Display the DataFrame for review
print(df.head())  # Print the first 5 rows
df.to_csv("trivia_questions.csv", index=False)  # Save to CSV
