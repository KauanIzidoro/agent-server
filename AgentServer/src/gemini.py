from settings import SETTINGS


class Gemini():
    """__summary__

    Class for communicate with Gemini API
    """
    
    def __init__(self, api_key=SETTINGS.GOOGLE_API_KEY, 
                 model=SETTINGS.MODEL, 
                 system_instruction=SETTINGS.SYSTEM_INSTRUCTION, 
                 response_schema=None):
        """__summary__

        Initializes an instance of the Gemini class.
        
        Args:
            api_key (str): Key to access Gemini API
            model (str, optional): Gemini LLM Model
            system_instruction (str): Instruction used to contextualize the LLM
            response_schema (ModelOutputDTO): Pydantic schema for the response
        """
        self.api_key = api_key
        self.model = model
        self.system_instruction = system_instruction
        self.response_schema = response_schema
    
    def generate_response(self, prompt, temperature=0.7, max_tokens=1024):
        """__summary__
        
        Args:
            prompt (str): O prompt para o modelo
            temperature (float, optional): Temperatura para controlar aleatoriedade. Defaults to 0.7.
            max_tokens (int, optional): Número máximo de tokens na resposta. Defaults to 1024.
            
        Returns:
            dict: Resposta do modelo, formatada de acordo com o schema quando disponível
        """
        if self.system_instruction:
            generation_config = {
                "temperature": temperature,
                "max_output_tokens": max_tokens,
                "system_instruction": self.system_instruction
            }
        else:
            generation_config = {
                "temperature": temperature,
                "max_output_tokens": max_tokens
            }
        
        response = self.client.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        raw_response = response.text
        
        if self.response_schema:
            try:
                import json
                from pydantic import ValidationError
                
                try:
                    json_response = json.loads(raw_response)
                    validated_response = self.response_schema(**json_response)
                    return validated_response.dict()
                except json.JSONDecodeError:
                    import re
                    json_match = re.search(r'```json\n(.*?)\n```', raw_response, re.DOTALL)
                    if json_match:
                        json_str = json_match.group(1)
                        json_response = json.loads(json_str)
                        validated_response = self.response_schema(**json_response)
                        return validated_response.dict()
                    else:
                        return {"raw_response": raw_response}
            except ValidationError as e:
                return {
                    "raw_response": raw_response,
                    "validation_error": str(e)
                }
        
        return {"response": raw_response}
    