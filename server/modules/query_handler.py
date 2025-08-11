from logger import logger
def query_chain(chain,user_input:str):
    try:
        logger.debug(f"Running chain with user input: {user_input}")
        result = chain({"query":user_input})
        response = {
            "response": result["result"],
            "sources": [doc.metadata.get("sources", " ") for doc in result.get("source_documents", [])]
        }
        logger.debug(f"Chain response: {response}") 
        return response
    except Exception as e:
        logger.exception(f"Error occurred while querying chain: {e}")
        raise