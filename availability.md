# Viabilidade do `AgentServer Server` integrado ao `PortalBackEnd`

### Problemas encontrados

- Autenticar usuários e controlar acesso ao PortalChatbot

- Porque usar um `AgentServer Server`? e Integração com os demais serviços.


### Soluções que um `AgentServer Server` oferece

1. Centralizar e orquestrar comunicação entre o DocAgent e demais agentes.

2. Gestão de estados e contextos enviados a `LLM`

3. Autenticação unificada e feita antes da interação com o `AgentServer Server`

- redesenhar diagrama das aplicações.


```mermaid
graph TD
    subgraph Frontend
        PFE[PortalFrontEnd]
    end

    subgraph Backend
        PBE[PortalBackend]
        PBC[PortalChatbot]
    end
    
    subgraph   ModelosIA
        GEM[Gemini LLM API]
        FUT[Futuros Modelos IA]
        AgentServer
    end


    %% Conexões Frontend
    PFE -->|Requisições HTTP e WS | PBE

    
    %% Conexões Backend
    PBE <--> PBC
    PBC <-->|Envio das mensagens por comunicação WS| AgentServer
    
    %% Conexões AgentServer
    AgentServer <-->|Protocolos AgentServer ** - ** gRPC | GEM
    AgentServer <-->|Protocolos AgentServer -  gRPC| FUT

    class PFE,Chat frontend
    class PBE,AgentServer,Auth backend
    class V4D,V4F vision
    class GEM,FUT ia
    class CTX,LOGS db
```