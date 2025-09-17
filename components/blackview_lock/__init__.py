import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import esp32_ble_client
from esphome.const import CONF_ID

blackview_lock_ns = cg.esphome_ns.namespace('blackview_lock')
BlackviewLock = blackview_lock_ns.class_('BlackviewLock', cg.Component, esp32_ble_client.BLEClientNode)

# This schema is what defines the valid options for your component in YAML
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(BlackviewLock),
}).extend(esp32_ble_client.BLE_CLIENT_SCHEMA) # This line adds the "ble_client_id" option

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await esp32_ble_client.register_ble_node(var, config)
