# 🌱 Agriculture 4.0 Simulation with MQTT

![Python](https://img.shields.io/badge/Python-3.x-blue)
![MQTT](https://img.shields.io/badge/Protocol-MQTT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## About the Project
This project simulates an Agriculture 4.0 environment using the MQTT protocol to demonstrate indirect communication in distributed systems. It represents a smart farming scenario where virtual sensors generate environmental data and an actuator makes automated decisions based on that data. The system follows the publish-subscribe pattern, widely used in IoT applications.

## Objective
The main goal is to demonstrate how distributed components can communicate asynchronously through a broker, without direct connections between them, highlighting scalability and decoupling.

## ⚙️ System Components
- 🌡️ Temperature Sensor: simulates ambient temperature data  
- 💧 Soil Moisture Sensor: simulates soil humidity levels  
- 🚿 Irrigator (Actuator): controls irrigation based on moisture values  
- 📊 Monitor: displays all incoming data in real time  

## Architecture
Sensors → MQTT Broker → Monitor / Irrigator  

- Sensors publish data to topics  
- Monitor subscribes to all topics  
- Irrigator subscribes only to moisture data  

## How It Works
- Sensors generate random data every 2 seconds  
- Data is published to MQTT topics  
- The monitor prints all received messages  
- The irrigator makes decisions based on moisture values:  
  Moisture < 30 → Irrigation ON  
  Moisture ≥ 30 → Irrigation OFF  

## How to Run
### Requirements
- Python 3  
- paho-mqtt  

### Install dependency
pip install paho-mqtt  

### Run the system (in separate terminals)
python sensor_temperatura.py  
python sensor_umidade.py  
python monitor.py  
python irrigador.py  

## Expected Behavior
- Continuous data generation from sensors  
- Real-time monitoring of messages  
- Automatic irrigation control based on soil moisture  

## Technologies
- Python  
- MQTT (HiveMQ public broker)  
- paho-mqtt  

## Notes
This is a simplified simulation project focused on learning distributed systems concepts and IoT communication using the publish-subscribe model. It demonstrates how loosely coupled components can interact efficiently in a real-time environment.