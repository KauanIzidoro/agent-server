# AgentServer


`AgentServer` atua como um orquestrador de agentes de `IA` especializados. A aplicação recebe mensagens de usuários via chatbot e, com base na intenção identificada, direciona a requisição para o agente mais adequado para executar a tarefa solicitada.

Utilizando a Gemini API como motor de orquestração, o sistema toma decisões sobre qual agente especializado deve processar cada tipo de solicitação. 

A arquitetura foi projetada para ser flexível e escalável, permitindo a fácil adição de novos agentes com diferentes especializações conforme necessário.

> Agentes disponíveis: 

- `DocAgent`: Especialista em analisar código fonte e gerar documentações em tempo real como fluxo de trabalho, diagramas de relacionamento entre tabelas e diagramas de classe.


```mermaid
graph TD
    subgraph Frontend
        PFE[PortalFrontEnd]
    end

    subgraph Backend
        PBE[PortalBackend]
    end
    
    subgraph   ModelosIA
        GEM[Gemini LLM API]
        FUT[Futuros Modelos IA]
        AgentServer
    end


    %% Conexões Frontend
    PFE -->|Requisições HTTP e WS | PBE

    
    %% Conexões Backend
    PBE<-->|Envio das mensagens por comunicação WS| AgentServer
    
    %% Conexões AgentServer
    AgentServer <-->|Protocolos AgentServer ** - ** gRPC | GEM
    AgentServer <-->|Protocolos AgentServer -  gRPC| FUT

    class PFE,Chat frontend
    class PBE,AgentServer,Auth backend
    class V4D,V4F vision
    class GEM,FUT ia
    class CTX,LOGS db
```


