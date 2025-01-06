from agents import song_analysis_agent, song_recommendation_agent, validation_and_feedback_agent

session_history = []
initial_song = 'one love - blue with popularity 0.63, energy 0.72 and danceability 0.68.'

while True:
    # Step 1: Analyze the song and fetch similar options
    results = song_analysis_agent(initial_song=initial_song)
    
    # Step 2: Get a song recommendation
    song_recommendation = song_recommendation_agent(initial_song=initial_song, results=results)
    
    # Step 3: Validate the recommendation
    validation = validation_and_feedback_agent(user_input=initial_song, song_recommendation=song_recommendation, session_history=session_history)
    
    print(f"Initial Song: {initial_song}")
    print(f"Recommended Song: {song_recommendation}")
    print(f"Validation Result: {validation}")
    breakpoint()
    # Add the validated song to session history
    session_history.append(initial_song)
    
    # Move to the next song for the loop
    initial_song = validation
    
    # Optional: Add a break condition to avoid infinite loops
    if len(session_history) > 10:  # Example: stop after 10 songs
        print("Session reached the maximum number of songs.")
        break