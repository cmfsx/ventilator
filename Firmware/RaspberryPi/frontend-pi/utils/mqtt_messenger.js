const mqtt = require('mqtt')
var database = require("./utils/database.js")
const client = mqtt.connect('mqtt://localhost:1883')

module.exports = {
  mqtt_sender: function() {
    console.log("Sender called");
  },

  mqtt_receiver: function() {
    console.log("Receiver called");
    client.on('connect', () => {
      client.subscribe('Ventilator/p1')
      client.subscribe('Ventilator/p2')
    });

    client.on('message', (topic, message) => {
      switch (topic) {
        case 'Ventilator/p1':
          return module.exports.ven_p1(message)
          p1 = database.add(10);
        case 'Ventilator/p2':
          return module.exports.ven_p2(message)
      }
      console.log('No handler for topic %s', topic)
    });
  },

  ven_p1: function(message){
    console.log('%s',message);
  },

  ven_p2: function(message){
    console.log(message);
  }
};
