# 引入记录日志的库
import logging
 
DOMAIN = "hachina4"
ENTITYID = DOMAIN + ".hello_world"
 
# 在python中，__name__代表模块名字
_LOGGER = logging.getLogger(__name__)
 
 
def setup(hass, config):
    """配置文件加载后，setup被系统调用."""
    attr = {"icon": "mdi:yin-yang",
            "friendly_name": "COM2",
            "slogon": "积木构建智慧空间！", }
    hass.states.set(ENTITYID, 'off', attributes=attr)
 
    def change_state(call):
        """change_state函数切换改变实体的状态."""
        # 记录info级别的日志
        _LOGGER.info("hachina's change_state service is called.")
 
        # 切换改变状态值
        if hass.states.get(ENTITYID).state == 'off':
            hass.states.set(ENTITYID, 'on', attributes=attr)
        else:
            hass.states.set(ENTITYID, 'off', attributes=attr)
 
    # 注册服务hachina.change_state
    hass.services.register(DOMAIN, 'change_state', change_state)
 
    return True