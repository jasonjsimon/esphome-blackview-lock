import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import esp32_ble_client
from esphome.const import CONF_ID

blackview_lock_ns = cg.esphome_ns.namespace('blackview_lock')
# The only change is BLEClientNode -> BLEClientBase in the line below
BlackviewLock = blackview_lock_ns.class_('BlackviewLock', cg.Component, esp32_ble_client.BLEClientBase)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(BlackviewLock),
}).extend(esp32_ble_client.BLE_CLIENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await esp32_ble_client.register_ble_node(var, config)
