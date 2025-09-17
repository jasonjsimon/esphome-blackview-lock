import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import esp32_ble_client
from esphome.const import CONF_ID, CONF_BLE_CLIENT_ID

# This explicitly declares the component's dependency.
DEPENDENCIES = ['esp32_ble_client']

blackview_lock_ns = cg.esphome_ns.namespace('blackview_lock')
BlackviewLock = blackview_lock_ns.class_('BlackviewLock', cg.Component, esp32_ble_client.BLEClientBase)

# This is the modern, direct way to define the schema without outdated helpers.
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(BlackviewLock),
    cv.Required(CONF_BLE_CLIENT_ID): cv.use_id(esp32_ble_client.ESP32BLEClient),
}).extend(cv.COMPONENT_SCHEMA)

# This is the modern way to register the component with its BLE client parent.
async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    
    parent = await cg.get_variable(config[CONF_BLE_CLIENT_ID])
    cg.add(parent.register_node(var))
