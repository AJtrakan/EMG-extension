Blockly.defineBlocksWithJsonArray([
{
  "type": "EMG_Sensors_read",
  "message0": "EMG Chart Data : Sensors Set PIN %1",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "value",
      "options": [
	[
          "IN1",
          "32"
        ],
        [
          "IN2",
          "33"
        ],
        [
          "IN3",
          "34"
        ],
        [
          "IN4",
          "35"
        ]
      ]
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": "#16b5aa",
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "EMG_Sensors_signal",
  "message0": "EMG Show Data : Sensors Set PIN %1",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "value",
      "options": [
	[
          "IN1",
          "32"
        ],
        [
          "IN2",
          "33"
        ],
        [
          "IN3",
          "34"
        ],
        [
          "IN4",
          "35"
        ]
      ]
    }
  ],
  "output": "Number",
  "colour": "#16b5aa",
  "tooltip": "Get data from Sony Remote",
  "helpUrl": ""
},
]);
