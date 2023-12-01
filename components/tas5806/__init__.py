import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import i2c
from esphome.components import output
from esphome.const import CONF_ID

CODEOWNERS = ["@bozzobrain"]
DEPENDENCIES = ["i2c"]
MULTI_CONF = True

tas5806_ns = cg.esphome_ns.namespace("tas5806")
TAS5806 = tas5806_ns.class_("TAS5806", cg.Component, i2c.I2CDevice, output.FloatOutput)
CONF_TAS5806_ID = "tas5806_id"

CONFIG_SCHEMA = ( 
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(TAS5806),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(i2c.i2c_device_schema(0x2D))
    .extend(output.FloatOutput)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])    
    # override default min power to 10%
    #if CONF_MIN_POWER not in config:
    #    config[CONF_MIN_POWER] = 0.1
    await output.register_output(var, config)
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)