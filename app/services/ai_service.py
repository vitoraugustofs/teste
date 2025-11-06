from anthropic import Anthropic
import os
from typing import Optional

# Inicializa cliente Anthropic (Claude)
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def chat_with_ai(
    message: str, 
    system_prompt: Optional[str] = None,
    model: str = "claude-3-5-sonnet-20241022",
    max_tokens: int = 1024,
    temperature: float = 1.0
) -> dict:
    """
    Envia uma mensagem para o Claude e retorna a resposta
    
    Args:
        message: Mensagem do usuário
        system_prompt: Prompt de sistema (opcional)
        model: Modelo a ser usado (claude-3-5-sonnet, claude-3-opus, etc)
        max_tokens: Número máximo de tokens na resposta
        temperature: Criatividade da resposta (0-1)
    
    Returns:
        dict com 'response', 'tokens_used' e 'model'
    """
    try:
        if system_prompt is None:
            system_prompt = "Você é um assistente útil e amigável que responde em português."
        
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            system=system_prompt,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        
        ai_response = response.content[0].text
        tokens_used = response.usage.input_tokens + response.usage.output_tokens
        
        return {
            "response": ai_response,
            "tokens_used": tokens_used,
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens,
            "model": model
        }
    
    except Exception as e:
        raise Exception(f"Erro ao chamar Claude: {str(e)}")


def chat_with_context(
    message: str,
    conversation_history: list,
    system_prompt: Optional[str] = None,
    model: str = "claude-3-5-sonnet-20241022"
) -> dict:
    """
    Chat com contexto de conversa anterior
    
    Args:
        message: Mensagem atual do usuário
        conversation_history: Lista de mensagens anteriores
            Formato: [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]
        system_prompt: Prompt de sistema
        model: Modelo Claude a usar
    
    Returns:
        dict com resposta e tokens
    """
    try:
        if system_prompt is None:
            system_prompt = "Você é um assistente útil que responde em português."
        
        # Claude exige que a primeira mensagem seja do usuário
        messages = []
        for msg in conversation_history:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        # Adiciona a mensagem atual
        messages.append({"role": "user", "content": message})
        
        response = client.messages.create(
            model=model,
            max_tokens=1024,
            temperature=1.0,
            system=system_prompt,
            messages=messages
        )
        
        ai_response = response.content[0].text
        tokens_used = response.usage.input_tokens + response.usage.output_tokens
        
        return {
            "response": ai_response,
            "tokens_used": tokens_used,
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens
        }
    
    except Exception as e:
        raise Exception(f"Erro ao chamar Claude: {str(e)}")


def analyze_user_query(query: str) -> dict:
    """
    Analisa uma query do usuário e classifica a intenção
    
    Returns:
        dict com 'intent', 'confidence' e análise
    """
    try:
        system_prompt = """Você é um analisador de intenções. 
        Analise a mensagem do usuário e responda APENAS no formato JSON:
        {"intent": "pergunta|ajuda|reclamacao|elogio|outro", "confidence": 0.0-1.0}"""
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=200,
            temperature=0.3,
            system=system_prompt,
            messages=[
                {"role": "user", "content": query}
            ]
        )
        
        import json
        result = json.loads(response.content[0].text)
        
        return result
    
    except Exception as e:
        return {"intent": "unknown", "confidence": 0.0, "error": str(e)}


def get_available_models() -> list:
    """
    Retorna lista de modelos Claude disponíveis
    """
    return [
        {
            "id": "claude-3-5-sonnet-20241022",
            "name": "Claude 3.5 Sonnet",
            "description": "Mais inteligente, melhor para tarefas complexas"
        },
        {
            "id": "claude-3-5-haiku-20241022", 
            "name": "Claude 3.5 Haiku",
            "description": "Mais rápido e econômico"
        },
        {
            "id": "claude-3-opus-20240229",
            "name": "Claude 3 Opus",
            "description": "Modelo anterior de alta performance"
        }
    ]