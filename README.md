# Repositório de estudos Ros2 (novos projetos_em_breve)
---

##  O que tem por aqui?



###  1. Simulação e Visualização

* **`my_robot_bringup`**: O "botão de ligar" do sistema. Lança o robô no **Gazebo Sim**, carrega o mundo de testes e configura as pontes de comunicação.
* **`my_robot_description`**: Onde o robô ganha vida. Usei **URDF/Xacro** para modelar a base móvel e o braço robótico. Inclui as configurações para visualização no **RViz2**.
* **`tr_robot_bringup`**: Testes avançados com automação de parâmetros via arquivos YAML.

### 2. Interfaces Personalizadas

* **`my_robot_interfaces`**: Definição de mensagens (`.msg`) e serviços (`.srv`) customizados, como o status de hardware e comandos para controle de LEDs e captura de entidades.

### 3. Lógica e Código (C++ e Python)

* **`meu_cpp` & `meu_py**`: Implementações equivalentes nas duas linguagens para comparar performance e agilidade, cobrindo sistemas de notícias, contadores e monitoramento de hardware.

### 4. Projeto Prático: Controle no Turtlesim

Um sistema de controle em malha fechada aplicado ao simulador clássico do ROS:

* **`turtle_controller`**: Um nó que faz a tartaruga principal perseguir alvos automaticamente.
* **`turtle_spawn`**: Gerencia o surgimento de novas tartarugas em posições aleatórias através de serviços.

### Desafio Final: Robô com Braço Articulado

Este é um robô composto por uma base móvel e um braço articulado de 2 eixos, integrado como o ápice do aprendizado:

* **Modelagem do Braço**: Adição de um suporte (`arm_base_link`) e dois elos cilíndricos: antebraço (`forearm_link`) e mão (`hand_link`).
* **Controle e Dinâmica**: Implementação de juntas revolutas com fricção e amortecimento (0.3), controladas por plugins de posição no Gazebo com ganhos P de 5.0 e 3.0.

---

## Como rodar na sua máquina

### Pré-requisitos

Você vai precisar do **ROS 2 (Humble ou Jazzy)** e do simulador **Gazebo**. Instale as dependências com:

```bash
sudo apt install ros-$ROS_DISTRO-ros-gz ros-$ROS_DISTRO-xacro ros-$ROS_DISTRO-ros-gz-bridge

```

### Passo a passo

1. **Compilação:**
```bash
colcon build --symlink-install
source install/setup.bash

```


2. **Visualização no RViz2:**
```bash
ros2 launch my_robot_description display.launch.xml

```


3. **Simulação Completa (Robô + Braço):**
```bash
ros2 launch my_robot_bringup my_robot_gazebo.launch.xml

```


4. **Projeto Turtlesim:**
```bash
# Terminal 1: ros2 run turtlesim turtlesim_node
# Terminal 2: ros2 run turtlesim_catch turtle_controller

```



---

## Aprendizados principais

* **Base do ROS 2**: Domínio de nós, tópicos, serviços e parâmetros.
* **URDF, Xacro & RViz**: Criação e visualização de modelos robóticos modulares e transformações (TFs).
* **Simulação Física**: Uso do Gazebo Sim para testar controladores e dinâmica real.
* **Integração**: Configuração de pontes (`bridges`) para conectar o simulador à lógica do ROS.

---

