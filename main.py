from flask import Flask, render_template
from paho.mqtt import client as mqtt_client

app = Flask(__name__)

broker = 'broker.emqx.io'
port = 1883
topic = 'topicName/iot'

client_id = 'test'
username = 'emqx'
password = ''

def connect_mqtt():
	client = mqtt_client.Client(client_id)
	client.username_pw_set(username, password)
	client.connect(broker, port)
	return client 

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/main', methods=['POST'])
def main():
	return render_template('main.html')

@app.route('/1', methods=['POST'])
def release():
	test_release()
	return render_template('1.html')

def test_release():
	client = connect_mqtt()
	client.loop_start()
	send_release_data(client)

@app.route('/2', methods=['POST'])
def engine():
	test_engine()
	return render_template('2.html')

def test_engine():
	client = connect_mqtt()
	client.loop_start()
	send_engine_data(client)

@app.route('/3', methods=['POST'])
def activate():
	test_activate()
	return render_template('3.html')

def test_activate():
	client = connect_mqtt()
	client.loop_start()
	send_activate_data(client)

@app.route('/4', methods=['POST'])
def ignite():
	test_ignite()
	return render_template('4.html')

def test_ignite():
	client = connect_mqtt()
	client.loop_start()
	send_ignite_data(client)

@app.route('/5', methods=['POST'])
def vent():
	test_vent()
	return render_template('5.html')

def test_vent():
	client = connect_mqtt()
	client.loop_start()
	send_vent_data(client)

@app.route('/6', methods=['POST'])
def srb():
	test_srb()
	return render_template('6.html')

def test_srb():
	client = connect_mqtt()
	client.loop_start()
	send_srb_data(client)

def send_release_data(client):
	msg = "1"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_engine_data(client):
	msg = "2"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_activate_data(client):
	msg = "3"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_ignite_data(client):
	msg = "4"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_vent_data(client):
	msg = "5"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

def send_srb_data(client):
	msg = "6"
	result = client.publish(topic, msg)
	status = result[0]
	if status == 0:
		print(f"Send {msg} to topic {topic}")

if __name__ == "__main__":
	app.run(port=5001)