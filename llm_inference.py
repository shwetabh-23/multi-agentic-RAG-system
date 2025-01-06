from transformers import pipeline

# Load the model once
llm_pipeline = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

def get_inference(content, pipe=llm_pipeline):
    """
    Generate inference using a preloaded pipeline.
    
    Args:
        content (str): The content to send to the model.
        pipe: The preloaded pipeline for text generation.
    
    Returns:
        str: The model's response.
    """
    messages = [
        {"role": "user", "content": f'{content}'},
    ]
    return pipe(messages)

# Example usage
if __name__ == "__main__":
    content = "The song I am currently playing is 'One Love by Blue'. What should be the next song?"
    response = get_inference(content)
    print(response)
