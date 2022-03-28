from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 4995761
    API_HASH = "586acd08f88addcab2e5c0a96be70b99"
    # the name to display in your alive message
    ALIVE_NAME = "sesky"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://postgres:Ayushcha12@localhost:5432/catuserbot"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1AZWarzoBu42cgrAte2oQORMa8uGK4RCusjPajpnTe25mNz4-tS7AS0gZI5GjudRUcATXQv4_3J5Cclsjy3VzCMqH18-FuKo07Xpj_neNRtDVTjQ50Qm-Z96zMybGIHrZzKwxqp37A0aJ9RUHkoK23R2CcGa8bFJBWL5xbbCaYFLZOudLHEbgp6ubqe58HDQnNqeXfjxgjIbslblWeJSq5Pjhyy1eiXBvTlyzfe2DkReXZdGOMys1nbAH216hpjj4ZVRJYb1McoCF9yylLSro9tVntjc7u9-eECycqMsUp1KVRdOrlidLCu48Z_G5UVTagXx-AWj7yasvtA_N_Z60DxzZKo3j648=
"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5224375142:AAF2GtIMKvbeSJfu-FocxJLrvf1QVCKrS1E"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -622952146
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
