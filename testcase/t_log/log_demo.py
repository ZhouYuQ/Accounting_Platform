# 1.导入Logging包
import logging

# 2.设置配置信息(设置了日志的级别和日志输出的格式）
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")

# 3.定义日志名称getlogger
logger = logging.getLogger("log_demo")

# 4.info，debug
logger.info("info")
logger.debug("debu")
logger.warning("www")
