from create_vector_db import load_vector_db, query_vector_db
from llm_inference import get_inference

def song_analysis_agent(initial_song): 
    
    save_path = '/home/drdo/multi_agentic_rag/chroma_db'
    chroma_db = load_vector_db(save_path)
    initial_song = 'one love - blue'
    vector_db_query = f'Suggest a song similar to {initial_song}.'
    results = query_vector_db(chroma_db, vector_db_query)
    results = format_results(results=results)
    return results

def song_recommendation_agent(initial_song, results) : 
    prompt_agent_1 = f'''
            Context: You are an advanced AI song recommender for jamming sessions. Given a song, recommend the next song based on the available characteristics.

            The song I am currently playing is {initial_song}. what should be my next song? Your options are : {results}
            '''
    song_recommendation = get_inference(prompt_agent_1)
    song_recommendation = song_recommendation[0]['generated_text'][1]['content'].split('\n')[-1]
    return song_recommendation

def validation_and_feedback_agent(user_input, song_recommendation, session_history = []) : 
    prompt = f"""
    Context: You are an advanced AI song recommendation validator. Your task is to validate or refine song recommendations to ensure they align with the session's context.
    
    - User's input: "{user_input}"
    - Previous session history: {", ".join(session_history)}
    - Suggested song recommendation: "{song_recommendation}"
    
    Consider the following and generate a one word answer:
    1. Does the recommended song match the mood, genre, and rhythm of the session so far?
    2. Is there sufficient variety to keep the session engaging?
    3. Does the recommendation avoid repeating recent songs or clashing with the user's stated preferences?
    
    If the recommendation is suitable, confirm it. Otherwise, suggest an alternative song that better fits the session's context.
    
    """
    valid = get_inference(content=prompt)
    valid = valid[0]['generated_text'][1]['content'].split('\n')[-2] + '.' + valid[0]['generated_text'][1]['content'].split('\n')[-1]
    return valid

def format_results(results):
    prompt = ''
    for i in range(len(results)):
        result = results[i]
        content = result.page_content
        content = content[34:]
        prompt += f'{i} : {content}'
        prompt += '.'
    return prompt


if __name__ == '__main__':
    
    initial_song = 'one love - blue'
    results = song_analysis_agent(initial_song= initial_song)
    song_recommendation = song_recommendation_agent(initial_song=initial_song, results=results)
    valid = validation_and_feedback_agent(user_input= initial_song, song_recommendation=song_recommendation)
    print(valid)
    breakpoint()   