# Acesso via Rede Local

Este guia explica como acessar a aplicação de qualquer dispositivo na sua rede local.

## 🚀 Como Acessar

### 1. Descobrir o IP da Máquina Host

Execute um dos comandos abaixo no terminal da máquina onde a aplicação está rodando:

```bash
# Opção 1: Mostrar todos os IPs
hostname -I

# Opção 2: Mostrar detalhes de rede
ip addr show

# Opção 3: Apenas IP da interface principal (geralmente)
ip route get 1 | awk '{print $7; exit}'
```

O IP geralmente estará no formato `192.168.x.x` ou `10.x.x.x`.

### 2. Iniciar a Aplicação

```bash
docker-compose up
```

Ou para rodar em background:

```bash
docker-compose up -d
```

### 3. Acessar de Outro Dispositivo

Em qualquer dispositivo conectado à **mesma rede**, abra o navegador e acesse:

```
http://<IP_DA_MAQUINA>:8080
```

**Exemplo**: Se o IP da máquina for `192.168.1.100`, acesse:
```
http://192.168.1.100:8080
```

## 🔧 Resolução de Problemas

### A aplicação não carrega

1. **Verifique se os containers estão rodando:**
   ```bash
   docker-compose ps
   ```
   Todos os serviços devem estar com status "Up".

2. **Teste o acesso local primeiro:**
   ```bash
   curl http://localhost:8080
   ```
   Se não funcionar localmente, o problema não é de rede.

3. **Verifique se a porta está escutando:**
   ```bash
   sudo netstat -tlnp | grep 8080
   ```
   ou
   ```bash
   sudo ss -tlnp | grep 8080
   ```

### Firewall bloqueando conexões

#### Ubuntu/Debian (UFW)

Verificar status:
```bash
sudo ufw status
```

Abrir porta 8080:
```bash
sudo ufw allow 8080/tcp
```

#### RHEL/CentOS/Fedora (firewalld)

Verificar portas abertas:
```bash
sudo firewall-cmd --list-ports
```

Abrir porta 8080:
```bash
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
```

#### Desabilitar firewall temporariamente (para teste)

**⚠️ Apenas para diagnóstico, não recomendado em produção:**

Ubuntu/Debian:
```bash
sudo ufw disable
```

RHEL/CentOS/Fedora:
```bash
sudo systemctl stop firewalld
```

### Dispositivos não estão na mesma rede

Certifique-se de que:
- Ambos os dispositivos estão conectados ao mesmo roteador/WiFi
- Não há isolamento de rede WiFi ativado (comum em redes de convidados)
- O IP da máquina host não mudou (IPs DHCP podem mudar)

## 📱 Testando de um Smartphone

1. Conecte o smartphone à mesma rede WiFi
2. Abra o navegador do celular
3. Digite `http://<IP_DA_MAQUINA>:8080`
4. Teste a funcionalidade de consulta de frete

## 🔍 Comandos Úteis de Diagnóstico

### Ver logs dos containers
```bash
# Todos os serviços
docker-compose logs

# Apenas frontend
docker-compose logs frontend

# Seguir logs em tempo real
docker-compose logs -f
```

### Testar conectividade de outro dispositivo

De outro dispositivo na rede, teste se a porta está acessível:

```bash
# Linux/Mac
nc -zv <IP_DA_MAQUINA> 8080

# Windows (PowerShell)
Test-NetConnection -ComputerName <IP_DA_MAQUINA> -Port 8080
```

### Verificar rotas de rede
```bash
ip route
```

## 🌐 Configurações de Rede

### Portas Utilizadas

- **8080**: Frontend (Nginx)
- **8000**: Gateway API
- **8001**: Flashlog Service
- **8002**: EntregaGov Service

Apenas a porta **8080** precisa estar acessível externamente. As outras portas são para comunicação interna entre containers.

## 💡 Dicas

- **IP Estático**: Configure um IP estático no seu roteador para a máquina host, assim o endereço não mudará
- **DNS Local**: Configure um hostname local no seu roteador (ex: `fretes.local`) para facilitar o acesso
- **Bookmarks**: Salve o endereço `http://<IP>:8080` nos favoritos dos dispositivos que você usa frequentemente
