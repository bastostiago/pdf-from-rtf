import logging
import logging.handlers

LOG_FILENAME = 'main.log'
LOG_MAX_BYTES = 5 * 1024 * 1024  # 5 MB
LOG_BACKUP_COUNT = 2  # no máximo 2 arquivos

# Configuração do logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Define um manipulador de arquivo para gravar os logs
handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME, maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT)

# Criar um handler para o terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

# Define o formato da mensagem de log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Adiciona o manipulador ao logger
logger.addHandler(handler)
logger.addHandler(stream_handler)