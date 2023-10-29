Blockly.Python['EMG_Sensors_read'] = function (block) {
  Blockly.Python.definitions_['import_EMG_filter'] = 'import EMG_filter';

  var dropdown_axis = block.getFieldValue('value');

  var code = `EMG_filter.EMG_sensor(${dropdown_axis})\n`;
  return code;
};

Blockly.Python['EMG_Sensors_signal'] = function (block) {
  Blockly.Python.definitions_['import_EMG_SG00165'] = 'import EMG_SG00165';

  var dropdown_axis = block.getFieldValue('value');

  var code = `EMG_SG00165.EMG_sensor(${dropdown_axis})`;
  return [code, Blockly.Python.ORDER_NONE];
};

